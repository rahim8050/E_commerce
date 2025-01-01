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

    return HttpResponse(f"the product is  {obj.pk}")

def home(request):
     return render(request,'Master.html')