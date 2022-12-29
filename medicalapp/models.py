from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
import uuid
from django.db import models

# Create your models here.


class login(models.Model):
    username=models.EmailField(max_length=20)
    password=models.CharField(max_length=8)


def __str__(self):
    return self.username






class Medicine(models.Model):
  name = models.CharField('name',max_length=100)
  description = models.CharField(max_length=200)
  price = models.DecimalField('price',max_digits=10, decimal_places=2)
  expdate=models.DateField(max_length=7,null=True)

def __str__(self):
    return self.name