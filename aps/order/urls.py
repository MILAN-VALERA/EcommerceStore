from django.urls import path

from . import views 

urlpatterns = [
    path('<str:prodId>/',views.orderProd),
]