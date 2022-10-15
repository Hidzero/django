from django.urls import path
from . import views

urlpatterns = [
    path('', views.home ),
    path('shop/', views.shop),
    path('about_us/', views.about_us)
]
