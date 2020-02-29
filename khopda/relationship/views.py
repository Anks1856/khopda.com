from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def relation(request):
    return HttpResponse("<h1>Relationship</h1>")

