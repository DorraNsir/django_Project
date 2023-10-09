from django.shortcuts import render
#from django.http import HttpResponse
# Create your views here.
def index(request):
    #return HttpResponse('Hello world')
    x={'name':'dorra','age':43657568769879}
    return render(request,'pages/index.html',x)   
def base(request):
    #return HttpResponse('about page')
    return render(request,'base.html')   
def about(request):
    #return HttpResponse('about page')
    x={'name':'ttt','age':43657568769879}
    return render(request,'pages/about.html',x)   
