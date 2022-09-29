from django.urls import path
from django.contrib import admin
from.import views
#this is called configure with urls(sub-process)
urlpatterns = [
    path('',views.greet),
    path('demo.html',views.thank)
    ]