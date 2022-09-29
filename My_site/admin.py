from django.contrib import admin
from .models import Products

class  ProductAdmin(admin.ModelAdmin):
    list_display =('fname','Address','Mobile','email1','password')
admin.site.register(Products,ProductAdmin)

# Register your models here.
