from django import views
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def shop(request):
    return render(request, 'shop.html')

def about_us(request):
    return render(request, 'about_us.html')




