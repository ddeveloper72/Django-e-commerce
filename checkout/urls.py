from django.urls import path
from checkout import views

urlpatterns = [
    path('', views.checkout, name='checkout')
    ]