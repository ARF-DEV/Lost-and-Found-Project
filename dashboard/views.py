from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, 'dashboard/index.html')


def staff(request):
    return render(request, 'dashboard/staff.html')


def found(request):
    return render(request, 'dashboard/found.html')


def lost(request):
    return render(request, 'dashboard/lost.html')


def solved(request):
    return render(request, 'dashboard/solved.html')
