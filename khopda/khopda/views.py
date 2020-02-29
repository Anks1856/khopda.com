# from django import urls
from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1>Home</h1>")
