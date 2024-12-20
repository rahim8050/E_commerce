from django.shortcuts import render
from django.http import HttpResponse
from Product.models import Product
# Create your views here.
def home_view():
    return
def product_detail(request,*args,**kwargs):
    obj = Product.objects.get(id=1)
    return HttpResponse(f"product detail {obj.id}")