from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from cart.models import Cart
from product.forms import ProductForm
from .models import ProductCategory, Product


def sell_item(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = request.user
            product.save()
            return redirect('product', pk=product.pk)
        else:
            print(request.POST)
    else:
        form = ProductForm()
    return render(request, 'product/list-item.html', {'form': form})


def update_item(request, pk):
    product = get_object_or_404(Product, pk=pk)
    user = product.seller
    if not user == request.user:
        return redirect('index')

    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            updated_product = form.save(commit=False)
            updated_product.seller = request.user
            updated_product.save()
            return redirect('product', pk=updated_product.pk)
        else:
            print(request.POST)
    else:
        data = {'name': product.name, 'price': product.price, "description": product.description,
                "height": product.height, "width": product.width, "depth": product.depth,
                "category": product.category}
        form = ProductForm(initial=data)

    return render(request, 'product/update-item.html', {'form': form, 'product': product})


def product_detail_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product/product.html', context={'product': product})


def delete_view(request, pk):
    profile = request.user
    product = get_object_or_404(Product, pk=pk)

    seller = product.seller
    if not product == seller:
        return redirect('index')

    product.delete()
    products = profile.product_set.all()
    return render(request, 'profile/profile.html', context={'profile': profile, 'products': products})