from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Relationship
# Create your views here.
def relation(request):
    relations = Relationship.objects.all()
    return render(request,'relationship/relation.html',{'relations':relations})
    # return HttpResponse("<h1>Relationship</h1>")

def detail(request,post_id):
    detail_post = get_object_or_404(Relationship,pk=post_id)
    return render(request,'relationship/detailpost.html',{'detail_post':detail_post})
