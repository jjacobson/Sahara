import random

from django.shortcuts import render, redirect

# Create your views here.
from product.models import ProductCategory, Product


def view_homepage(request, category=None):
    categories = ProductCategory.objects.all()
    all_products = Product.objects.all()
    subset = 8

    if not category:
        if all_products.count() < subset:
            products = all_products
        else:
            tmp = Product.objects.values_list('id', flat=True)
            my_ids = list(tmp)
            rand_ids = random.sample(my_ids, subset)
            products = Product.objects.filter(id__in=rand_ids)
    else:
        products = all_products.filter(category__name=category)

    print(products)
    return render(request, 'index.html', {'categories': categories, 'products': products, 'current_category': category})
