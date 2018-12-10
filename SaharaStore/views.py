import random

from django.shortcuts import render, redirect

# Create your views here.
from product.models import ProductCategory, Product


def view_homepage(request, category=None):
    categories = ProductCategory.objects.all()
    all_products = Product.objects.all()
    subset = 10

    if not category:
        products = all_products if all_products.count() < subset else Product.objects.order_by('?')[subset]
    else:
        products = all_products.filter(category__name=category)
    return render(request, 'index.html', {'categories': categories, 'products': products, 'current_category': category})
