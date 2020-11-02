from django.db import models

# Create your models here.

class Product(models.Model):
    productId = models.AutoField(primary_key=True)
    productName = models.CharField(max_length=100)
    productDesc = models.CharField(max_length=200)
    productStock = models.CharField(max_length=10,default=0)
    productPrice = models.CharField(max_length=10,default=0)
    productImage = models.ImageField()
    createDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.productName