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

from . import views as homepage_views
from product import views as product_views
from profile import views as profile_views
from cart import views as cart_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # new
    path('list-item/', product_views.sell_item, name='list-item'),
    path('update-item/<int:pk>', product_views.update_item, name='update_item'),
    path('product/<int:pk>', product_views.product_detail_view, name='product'),
    path('submit-review/<int:pk>', product_views.submit_review_view, name='submit_review_view'),
    path('delete-item/<int:pk>', product_views.delete_view, name='delete_view'),
    path('checkout/', cart_views.checkout_view, name='checkout_view'),
    path('delete-cart-item/<int:pk>', cart_views.delete_cart_view, name='delete_cart_view'),
    path('add-to-cart/<int:pk>', cart_views.add_to_cart_view, name='add_to_cart_view'),
    path('cart/', cart_views.cart_view, name='cart'),
    path('profile/<int:pk>', profile_views.profile_view, name='profile'),
    path('category/<str:category>', homepage_views.view_homepage, name='index'),
    path('', homepage_views.view_homepage, name='index'),

]
