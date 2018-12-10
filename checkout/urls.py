from django.conf.urls import url
from .views import checkout

urlpattersn = [
    url(r'^$', checkout, name='checkout'),
    ]