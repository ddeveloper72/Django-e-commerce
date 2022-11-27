from django.urls import path
from products import views

urlpatterns = [
    path('', views.all_products, name='products')
]
