from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from .forms import LaporanForm
from django.db.models import Count
# Create your views here.


@login_required()
def index(request):
    #------------- FOMR---------------------
    if request.method == 'POST':
        form = LaporanForm(request.POST, request.FILES)
        if form.is_valid():
            new_barang = Barang(
                nama_barang = form.cleaned_data['nama_barang'],
                jenis_barang = form.cleaned_data['jenis_barang']
            )
            new_barang.save()
            new_laporan = Laporan(
                status = form.cleaned_data['status'],
                deskripsi_barang = form.cleaned_data['deskripsi'],
                lokasi = form.cleaned_data['lokasi'],
                image = form.cleaned_data.get('foto'),
                    
                barang_id = new_barang,
                user_id = request.user
            )
            new_laporan.save()
            return redirect('dashboard-index')
    else:
        form = LaporanForm()

    #ambil data laporan untuk chart berdasarkan status
    #select status,count(status) as dcount from laporan group by status
    data_status = Laporan.objects.values('status').annotate(dcount=Count('status'))
    item_status = []
    label_status = []
    for isi in data_status:
        label_status.append(isi['status'])
        item_status.append(isi['dcount'])

    #ambil data barang untuk chart berdasarkan jenis barang
    #select jenis_barang,count(jenis_barang) as dcount from laporan group by jenis_barang
    data_kategori = Barang.objects.values('jenis_barang').annotate(dcount=Count('jenis_barang'))
    item_kategori = []
    label_kategori = []
    for isi in data_kategori:
        label_kategori.append(isi['jenis_barang'])
        item_kategori.append(isi['dcount'])

    #ambil data laporan untuk chart berdasarkan lokasi
    #select lokasi,count(lokasi) as dcount from laporan group by lokasi
    data_lokasi = Laporan.objects.values('lokasi').annotate(dcount=Count('lokasi'))
    item_lokasi = []
    label_lokasi = []
    for isi in data_lokasi:
        label_lokasi.append(isi['lokasi'])
        item_lokasi.append(isi['dcount'])

    data_solved = Laporan.objects.values('isSolved').annotate(dcount=Count('isSolved'))
    print(data_solved)
    item_solved = []
    for isi in data_solved:
        item_solved.append(isi['dcount'])
    print(item_solved)
    context = {
        'form' : form,
        'data' : data_status,
        'label_status': label_status,
        'item_status' : item_status,
        'label_kategori': label_kategori,
        'item_kategori': item_kategori,
        'label_lokasi': label_lokasi,
        'item_lokasi' : item_lokasi,
        'item_solved' : item_solved,
    }
    return render(request, 'dashboard/index.html', context)


@login_required()
def staff(request):
    return render(request, 'dashboard/staff.html')


@login_required()
def found(request):
    # db_query = "SELECT * FROM laporan NATURAL JOIN
    # (SELECT * FROM auth_user NATURAL JOIN barang)
    # WHERE status='FOUND'; "

    #items = Laporan.objects.raw(db_query)
    items = Laporan.objects.filter(status='found', isSolved=False)

    #-------------------- Laporan Form-------------------
    if request.method == 'POST':
        form = LaporanForm(request.POST, request.FILES)
        if form.is_valid():
            new_barang = Barang(
                nama_barang = form.cleaned_data['nama_barang'],
                jenis_barang = form.cleaned_data['jenis_barang']
            )
            new_barang.save()
            new_laporan = Laporan(
                status = form.cleaned_data['status'],
                deskripsi_barang = form.cleaned_data['deskripsi'],
                lokasi = form.cleaned_data['lokasi'],
                image = form.cleaned_data.get('foto'),
                    
                barang_id = new_barang,
                user_id = request.user
            )
            new_laporan.save()
            messages.success(request, f'{new_barang.nama_barang} berhasil ditambahkan' )
            return redirect('dashboard-found')
    else:
        form = LaporanForm()
    #-------------------- END Laporan Form-------------------
    
    context = {
        'items': items,
        'form' : form,
    }

    return render(request, 'dashboard/found.html', context)


@login_required()
def lost(request):
    # db_query = "SELECT * FROM laporan NATURAL JOIN
    # (SELECT * FROM auth_user NATURAL JOIN barang)
    # WHERE status='LOST'; "

    #items = Laporan.objects.raw(db_query)
    items = Laporan.objects.filter(status='lost', isSolved=False)

    #-------------------- Laporan Form-------------------
    if request.method == 'POST':
        form = LaporanForm(request.POST, request.FILES)
        if form.is_valid():
            new_barang = Barang(
                nama_barang = form.cleaned_data['nama_barang'],
                jenis_barang = form.cleaned_data['jenis_barang']
            )
            new_barang.save()
            new_laporan = Laporan(
                status = form.cleaned_data['status'],
                deskripsi_barang = form.cleaned_data['deskripsi'],
                lokasi = form.cleaned_data['lokasi'],
                image = form.cleaned_data.get('foto'),
                    
                barang_id = new_barang,
                user_id = request.user
            )
            new_laporan.save()
            messages.success(request, f'{new_barang.nama_barang} berhasil ditambahkan' )
            return redirect('dashboard-lost')
    else:
        form = LaporanForm()
    #-------------------- END Laporan Form-------------------

    context = {
        'items': items,
        'form' : form,
    }
    return render(request, 'dashboard/lost.html', context)


@login_required()
def solved(request):
    # db_query = "SELECT * FROM laporan NATURAL JOIN
    # (SELECT * FROM auth_user NATURAL JOIN barang)
    # WHERE isSolve=true; "

    #items = Laporan.objects.raw(db_query)
    items = Laporan.objects.filter(isSolved=True)
    context = {
        'items': items,
    }
    return render(request, 'dashboard/solved.html', context)


def laporan_solve(request, pk):
    item = Laporan.objects.get(id=pk)
    if request.method=='POST':
        item.isSolved = True
        item.save()
        return redirect('dashboard-solved')
    return render(request, 'dashboard/laporan_solve.html')

def laporan_detail(request, pk):
    laporan = Laporan.objects.get(id=pk)

    #-------------------- Laporan Form-------------------
    if request.method == 'POST':
        form = LaporanForm(request.POST, request.FILES)
        if form.is_valid():
            new_barang = Barang(
                nama_barang = form.cleaned_data['nama_barang'],
                jenis_barang = form.cleaned_data['jenis_barang']
            )
            new_barang.save()
            new_laporan = Laporan(
                status = form.cleaned_data['status'],
                deskripsi_barang = form.cleaned_data['deskripsi'],
                lokasi = form.cleaned_data['lokasi'],
                image = form.cleaned_data.get('foto'),
                    
                barang_id = new_barang,
                user_id = request.user
            )
            new_laporan.save()
            messages.success(request, f'{new_barang.nama_barang} berhasil ditambahkan' )
            return redirect('dashboard-found')
    else:
        form = LaporanForm()
    #-------------------- END Laporan Form-------------------
    context = {
        'laporan' : laporan,
        'form' : form,
    }
    return render(request, 'dashboard/laporan_detail.html', context)