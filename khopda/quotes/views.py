from django.shortcuts import render
from django.http import HttpResponse
from .models import Quotes
# Create your views here.


def love(request):
    quotes = Quotes.objects.all()
    return render(request,'quotes/qlove.html',{'quotes':quotes})

def motivation(request):
    quotes = Quotes.objects.all()
    return render(request,'quotes/qmotivation.html',{'quotes':quotes})

def attitude(request):
    quotes = Quotes.objects.all()
    return render(request,'quotes/qattitude.html',{'quotes':quotes})

def life(request):
    quotes = Quotes.objects.all()
    return render(request,'quotes/qlife.html',{'quotes':quotes})

def friendship(request):
    quotes = Quotes.objects.all()
    return render(request,'quotes/qfriendship.html',{'quotes':quotes})

def god(request):
    quotes = Quotes.objects.all()
    return render(request,'quotes/qgod.html',{'quotes':quotes})

