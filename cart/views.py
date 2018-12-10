from django.shortcuts import render, get_object_or_404

# Create your views here.
from cart.models import Cart, Entry
from product.models import Product


def add_to_cart_view(request, pk):
    profile = request.user
    product = get_object_or_404(Product, pk=pk)

    cart, created = Cart.objects.get_or_create(owner=profile)

    Entry.objects.create(product=product, cart=cart, quantity=1)
    list_of_entries = Entry.objects.filter(cart=cart)

    print('after', cart, 'entries: ', list_of_entries)

    return render(request, 'product/product.html', context={'product': product})


def cart_view(request):
    profile = request.user
    cart, created = Cart.objects.get_or_create(owner=profile)


    return render(request, 'product/product.html', context={'product': product})
