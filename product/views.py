from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from product.forms import ProductForm
from .models import ProductCategory, Product


def sell_item(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            product.save()
            return redirect('product', pk=product.pk)
        else:
            print(request.POST)
    else:
        form = ProductForm()
    return render(request, 'product/list-item.html', {'form': form})


def product_detail_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product/product.html', context={'product': product})
