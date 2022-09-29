from curses import longname
from email.headerregistry import Address
from itertools import product
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from .models import Products

def greet(request):
    if request.method =="POST":
        fname=request.POST['fname']
        Address= request.POST['Address']
        Mobile =request.POST['Mobile']
        email1 = request.POST['email1']
        password = request.POST['password']
        product = Products(fname=fname,Address=Address,Mobile=Mobile,email1=email1,password=password)
        product.save()
    return render(request,'index.html')
def thank(request):
    return render(request,'demo.html')

