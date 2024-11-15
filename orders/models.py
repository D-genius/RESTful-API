from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=255)
    phone = models.BigIntegerField(unique=True)
    email = models.EmailField(max_length=254)
    code = models.CharField(max_length=100, unique=True ,auto_created= True)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    item = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    time = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-time']
    def __str__(self):
        return self.item