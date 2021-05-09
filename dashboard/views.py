from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import LaporanForm, BarangForm
# Create your views here.


@login_required()
def index(request):
    return render(request, 'dashboard/index.html')


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

    context = {
        'items': items,
    }

    return render(request, 'dashboard/found.html', context)


@login_required()
def lost(request):
    # db_query = "SELECT * FROM laporan NATURAL JOIN
    # (SELECT * FROM auth_user NATURAL JOIN barang)
    # WHERE status='LOST'; "

    #items = Laporan.objects.raw(db_query)
    items = Laporan.objects.filter(status='lost')

    context = {
        'items': items,
    }
    return render(request, 'dashboard/lost.html', context)


@login_required()
def solved(request):
    # belom
    return render(request, 'dashboard/solved.html')
