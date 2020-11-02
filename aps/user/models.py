from django.db import models

# Create your models here.
class User(models.Model):

    userId   = models.AutoField(primary_key=True)
    userName = models.CharField(max_length=100)
    userAge  = models.CharField(max_length=10)
    userMaxPurchase = models.CharField(max_length=1000)
    createDate = models.DateTimeField(auto_now_add=True)
    totalOrderPlaced = models.CharField(max_length=10,default=0)
    userPhone = models.CharField(max_length=10)
    usermailId = models.CharField(max_length=100)
    userPassword = models.CharField(max_length=20)
    userAddress = models.CharField(max_length=200)
    pincode = models.CharField(max_length=10)
    creditCard_1 = models.CharField(max_length=20,default="")
    creditCard_2 = models.CharField(max_length=20,default="")
    creditCard_3 = models.CharField(max_length=20,default="")
    creditCard_4 = models.CharField(max_length=20,default="")
     

    def __str__(self):
        return self.userName
    