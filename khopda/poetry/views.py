from django.shortcuts import render
from django.http import HttpResponse
from . import urls
from.models import Poetry

# Create your views here.

def poetry(request):
    poetries = Poetry.objects.all()

    return render(request,'poetry/poetry.html',{'poetries':poetries})
