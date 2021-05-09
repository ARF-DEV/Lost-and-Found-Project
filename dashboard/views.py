from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import *
# Create your views here.


@login_required()
def index(request):
    return render(request, 'dashboard/index.html')


@login_required()
def staff(request):
    return render(request, 'dashboard/staff.html')


@login_required()
def found(request):
    #db_query = "SELECT * FROM laporan WHERE laporan.status='lost' "
    #items = Laporan.objects.raw(db_query)
    items = Laporan.objects.filter(status='lost')

    context = {
        'items': items,
    }

    return render(request, 'dashboard/found.html', context)


@login_required()
def lost(request):
    return render(request, 'dashboard/lost.html')


@login_required()
def solved(request):
    return render(request, 'dashboard/solved.html')
