from functools import reduce

from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from cart.models import Cart, Review, Receipt, Transaction
from product.forms import ProductForm, ReviewForm
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
    reviews = Review.objects.all().filter(product=product)
    form = ReviewForm()

    c = [pk]
    transaction = reduce(lambda qs, key: qs.filter(pk=pk), c, Transaction.objects.all())
    size = transaction.count()

    reviewed = not Review.objects.all().filter(product=product, reviewer=request.user).count() == 0
    total_stars = 0
    for review in reviews:
        total_stars += review.rating

    rating = total_stars / reviews.count()

    return render(request, 'product/product.html',
                  context={'product': product, 'form': form, 'reviews': reviews, 'size': size, 'reviewed': reviewed,
                           'rating': rating})


def delete_view(request, pk):
    profile = request.user
    product = get_object_or_404(Product, pk=pk)

    seller = product.seller
    if not product == seller:
        return redirect('index')

    product.delete()
    products = profile.product_set.all()
    return render(request, 'profile/profile.html', context={'profile': profile, 'products': products})


def submit_review_view(request, pk):
    if request.method == "POST":
        form = ReviewForm(request.POST)

        # todo dear god fix this mess
        c = [pk]
        transaction = reduce(lambda qs, key: qs.filter(pk=pk), c, Transaction.objects.all())
        print(transaction)
        receipt = get_object_or_404(Receipt, transaction=transaction[0])
        product = get_object_or_404(Product, pk=pk)
        if form.is_valid():
            review = form.save(commit=False)
            review.receipt = receipt
            review.product = product
            review.reviewer = transaction[0].buyer
            review.save()
            return redirect('product', pk=pk)
        else:
            print(form.errors)
            print(request.POST)

    return redirect('product', pk)
