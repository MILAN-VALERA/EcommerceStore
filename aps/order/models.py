from django.db import models
from aps.user.models import User
# Create your models here.
class Order(models.Model):

    orderId = models.AutoField(primary_key=True)
    userId = models.ForeignKey(User,on_delete=models.CASCADE)
    orderDate = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.orderId)