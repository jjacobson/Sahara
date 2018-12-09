"""SaharaStore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # new
    path('list-item/', TemplateView.as_view(template_name='product/list-item.html'), name='list-item'),
    path('product/', TemplateView.as_view(template_name='product/product.html'), name='product'),
    path('cart/', TemplateView.as_view(template_name='cart/cart.html'), name='cart'),
    path('user_profile/', TemplateView.as_view(template_name='user_profile/profile.html'), name='profile'),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
]
