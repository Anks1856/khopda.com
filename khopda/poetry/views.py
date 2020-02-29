from django.shortcuts import render
from django.http import HttpResponse
from . import urls
# Create your views here.

def poetry(request):
    return HttpResponse("<h1>poetry</h1>")

