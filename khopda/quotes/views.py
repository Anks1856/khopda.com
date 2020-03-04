from django.shortcuts import render
from django.http import HttpResponse
from .models import Quotes
# Create your views here.
def quote(request):
    quotes = Quotes.objects.all()
    return render(request,'quotes/Quotes.html',{'quotes':quotes})