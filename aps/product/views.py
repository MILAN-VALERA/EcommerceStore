from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Product
def productList(request):

    products = Product.objects.all()
    params = {'product':products}
    
    return render(request,'index.html',params)
