from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    productName = models.CharField(max_length=200, null=True, blank=True)
    Description = models.CharField(max_length=500, null=True, blank=True)
    
    def __str__(self) -> str:
        return self.productName
    
    