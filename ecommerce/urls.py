"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path
from django.contrib import admin
from django.views.static import serve
from django.conf import settings
from products.views import all_products
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from .settings import MEDIA_ROOT

favicon_view = RedirectView.as_view(url='favicon/favicon.ico', permanent=True)

urlpatterns = [
    path('favicon.ico/', favicon_view, name="favicon"),
    path('admin/', admin.site.urls),
    path('', all_products, name='index'),
    path('accounts/', include('accounts.urls')),
    path('products/', include('products.urls')),
    path('cart/', include('cart.urls')),
    path('checkout/', include('checkout.urls')),
    path('search/', include('search.urls')),
    re_path('media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT})
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)