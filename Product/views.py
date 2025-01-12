from django import http
from django.shortcuts import render
from django.http import HttpResponse,Http404
from Product.models import Product
# Create your views here.
def home_view():
    return
def product_detail(request,pk):
    # tit=Product.objects.get(id=id)
    # return HttpResponse({tit.id})
    obj = Product.objects.get(pk=pk)
    try:
      obj = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
     raise Http404

    return render(request,"products/views.html",{"object":obj})
def product_list(request,*args,**kwargs):
    qs = Product.objects.all()
    context ={"object_list": qs}
    return render(request,"products/list.html",context)

def home(request,*args,**kwargs):
     context ={"data": "hello"}
     return render(request,'Master.html',context)


def base(request,*args,**kwargs):

    return render(request,'base.html')

def bad_view(request,*args,**kwargs):
    print(request.GET)
    return HttpResponse("do not touch this")
def signup(request):
    return render(request,'SignupForm.html')
def contactus(request):
    return render(request,'contact.html')


def logins(request):
    return render (request,'LoginFormTemplate.html')


def viewed(request):
    return render(request,'view.html')


def homes(request):
    return render(request,'home.html')