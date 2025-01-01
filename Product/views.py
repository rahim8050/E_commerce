from django import http
from django.shortcuts import render
from django.http import HttpResponse,Http404
from Product.models import Product
# Create your views here.
def home_view():
    return
def product_detail(request,id):
    obj = Product.objects.get(id=id)
    try:
      obj = Product.objects.get(id=id)
    except Product.DoesNotExist:
     raise Http404

    return HttpResponse(f"the product is  {obj.id}")

def home(request):
     return render(request,'Master.html')