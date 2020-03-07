from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Relationship
# Create your views here.
# def relation(request):
#     relations = Relationship.objects.all()
#     return render(request,'relationship/relation.html',{'relations':relations})
#     # return HttpResponse("<h1>Relationship</h1>")

def detail(request,post_id):
    detail_post = get_object_or_404(Relationship,pk=post_id)
    return render(request,'relationship/detailpost.html',{'detail_post':detail_post})

def love(request):
    relations = Relationship.objects.all()
    return render(request,'relationship/rlove.html',{'relations':relations})

def crush(request):
    relations = Relationship.objects.all()
    return render(request,'relationship/rcrush.html',{'relations':relations})

def mom(request):
    relations = Relationship.objects.all()
    return render(request,'relationship/rmom.html',{'relations':relations})

def dad(request):
    relations = Relationship.objects.all()
    return render(request,'relationship/rdad.html',{'relations':relations})

def bro(request):
    relations = Relationship.objects.all()
    return render(request,'relationship/rbro.html',{'relations':relations})

def bestfrd(request):
    relations = Relationship.objects.all()
    return render(request,'relationship/rbestfrd.html',{'relations':relations})

def relative(request):
    relations = Relationship.objects.all()
    return render(request,'relationship/rrelative.html',{'relations':relations})

def hatter(request):
    relations = Relationship.objects.all()
    return render(request,'relationship/rhatter.html',{'relations':relations})

def teacher(request):
    relations = Relationship.objects.all()
    return render(request,'relationship/rteacher.html',{'relations':relations})

def rol(request):
    relations = Relationship.objects.all()
    return render(request,'relationship/rrol.html',{'relations':relations})

def sup(request):
    relations = Relationship.objects.all()
    return render(request,'relationship/rsupport.html',{'relations':relations})

def clg(request):
    relations = Relationship.objects.all()
    return render(request,'relationship/rcolg.html',{'relations':relations})
