# django_framework
This Repository is about Django framework implemented in ecommerce 
Now-a-days most of the company describes django framework, because it is fullstack framework
used to connect frontend and backend, simply it acts as a intermediate bridge 
In this repository it will connect both font-end and back-end, it is example webpage 
note:
Django was created in 2003 by Python programmers Adrian Holovaty and Simon Willison

For install django in you computer or pc follow the below steps:

`
  steps: 
    a) first you should create a empty folder in your local storage 
    b) open a code editor either visual studio or pycharm 
    c) open the teminal in that editor by pressing ctrl+ tag (in windows)
    d) In that terminal type pip install Django 
    e) after installation od Django 
    f) If you what to built the new enviroment follow the below commands:
            1) Py -3 -m venv.env
            2) .env\Scripts\activate
            3) After running the above comments it will glow green color in terminal 
      If you also run without creating a new enviroment, enviroment is nothing but new setup which is like a new home
    g) After that create folder by using the commands:
          Django-admin startproject name_of_your_folder     # you can give any name without leaving white space
    h) After creating the folder, check some files are present in it, open terminal and give python manage.py runserver 
        it will generate the a local ip address copy that and paste in a browser it will run with the symbol of rocket 
        
        
        
    i) After the above steps : 
      give the command:
            i) python manage.py startapp your_app_name 
            it will create a another folder in the previous folder downloaded 
            In that there are many files like 
            admin.py,models.py,apps.py,views.py etc.,
            
            In that same folder create a  folder templates create a html page, and also it that create a another folder named static in 
            that creata a external css files 
            
      ii) after creating that open views.py in that :
      write :
      
      
        from urllib import request
        from django.shortcuts import render
        from django.http import HttpResponse
        
        
        def greet(request):
           return render(request,'index.html')            #index.html is the file i have create din templates folder
           
           iii)
           After that open urls.py in first created folder
           In that write the below code:
           
           
           from django.urls import path
          from django.contrib import admin
          from.import views
          #this is called configure with urls(sub-process)
          urlpatterns = [
              path('',views.greet)
              ]
              
              
              In urls.py is used to connect the html fiel with browser
              In views.py is used to display the html content in front-end
              
             
             iv) If errors occurs means eg:
             Template error
             Open settings.py in that in 40th line (intalled apps :)
             add your 2nd folder name under single cotes('name')
             After that run it by using command:
              Python manage.py runserver 
              In case if you want to connect with backend refer my files (models.py)
              
              Thank you
