from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.postgres.fields import ArrayField
from django.db.models.fields.related import ForeignKey

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100,blank=False)
    phone = models.CharField(max_length=11,blank=False)
    address = models.CharField(max_length=1000,blank=True,default='')

    class Meta:
        ordering = ['name']


class ServiceOrder(models.Model):
    customer_id=ForeignKey(Customer,on_delete=CASCADE)
    date = models.DateField(auto_now=True)
