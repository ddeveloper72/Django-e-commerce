from django.urls import path, re_path
from cart import views

urlpatterns = [
    path('', views.view_cart,
         name='view_cart'),
    re_path(r'^add/(?P<id>\d+)', views.add_to_cart,
            name='add_to_cart'),
    re_path(r'^adjust/(?P<id>\d+)', views.adjust_cart,
            name='adjust_cart')
    ]