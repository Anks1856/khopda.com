from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login(request):
    # return HttpResponse("<h1>Login</h1>")
    return render(request, '/account/templates/account/home.html')

def signin(request):
    return HttpResponse("<h1>signin</h1>")

def logout(request):
    return HttpResponse("<h1>logout</h1>")
