from django.shortcuts import render
from django.http import HttpResponse
from . import urls
from.models import Poetry

# Create your views here.

def love(request):
    poetries = Poetry.objects.all()
    return render(request,'poetry/plove.html',{'poetries':poetries})

def motivational(request):
    poetries = Poetry.objects.all()
    return render(request,'poetry/pmotivation.html',{'poetries':poetries})

def attitude(request):
    poetries = Poetry.objects.all()
    return render(request,'poetry/pattitude.html',{'poetries':poetries})

def life(request):
    poetries = Poetry.objects.all()
    return render(request,'poetry/plife.html',{'poetries':poetries})

def friendship(request):
    poetries = Poetry.objects.all()
    return render(request,'poetry/pfriendship.html',{'poetries':poetries})

def gods(request):
    poetries = Poetry.objects.all()
    return render(request,'poetry/pgod.html',{'poetries':poetries})

def mother(request):
    poetries = Poetry.objects.all()
    return render(request,'poetry/pmother.html',{'poetries':poetries})

def nature(request):
    poetries = Poetry.objects.all()
    return render(request,'poetry/pnature.html',{'poetries':poetries})

