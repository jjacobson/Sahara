from django.shortcuts import render, redirect

# Create your views here.
from product.models import ProductCategory, Product


def view_homepage(request):
    categories = ProductCategory.objects.all()
    products = Product.objects.all()

    return render(request, 'index.html', {'categories': categories, 'products': products})
