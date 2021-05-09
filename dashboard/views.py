from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import LaporanForm
# Create your views here.


@login_required()
def index(request):
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
    else:
        form = LaporanForm()

    context = {
        'form' : form
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
    items = Laporan.objects.filter(status='found')

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
    items = Laporan.objects.filter(status='lost')

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
    # belom
    return render(request, 'dashboard/solved.html')
