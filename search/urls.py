from django.urls import path
from search import views

urlpatterns = [
    path('', views.do_search, name='search')
]
