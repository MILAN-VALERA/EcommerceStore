from django.db import models
from aps.product.models import Product
from aps.order.models import Order
# Create your models here.

class OrderDetail(models.Model):
    orderDetailId = models.AutoField(primary_key=True)
    orderId = models.ForeignKey(Order,on_delete= models.CASCADE)
    productId = models.ForeignKey(Product,on_delete = models.CASCADE)
    orderAmount = models.CharField(max_length=100)
    orderDate = models.DateTimeField(auto_now_add=True)
    orderShipAdd = models.CharField(max_length=100)
    quantity = models.CharField(max_length=10)
    paymentMethod = models.CharField(max_length=20,default="CreditCard")

    def __str__(self):
        return str(self.orderDetailId)

