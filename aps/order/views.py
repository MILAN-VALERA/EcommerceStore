from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from aps.product.models import Product
def orderProd(request,prodId):
    productData = Product.objects.filter(productId=prodId)
 
    
    return render(request,'order.html',{'product':productData})

    