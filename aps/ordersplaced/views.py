from django.shortcuts import render

# Create your views here.

def ordersplaced(request):

    return render(request,'orderPlaced.html')