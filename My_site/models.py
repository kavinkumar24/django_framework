from curses import longname
import email
from tabnanny import verbose
from django.db import models


class Products(models.Model):
    fname = models.CharField(max_length=250)
    Address= models.CharField(max_length=200)
    Mobile = models.IntegerField()
    email1 = models.EmailField(max_length=254)
    password = models.EmailField(max_length= 250)
    
    