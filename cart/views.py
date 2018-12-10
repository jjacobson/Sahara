from django.shortcuts import render, get_object_or_404, redirect

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
    list_of_entries = Entry.objects.filter(cart=cart)

    cart_products = {}
    for entry in list_of_entries:
        key = entry.product.pk
        if key in cart_products:
            cart_products[key]['quantity'] += entry.quantity
        else:
            cart_products[key] = {'name': entry.product.name, 'price': entry.product.price, 'quantity': entry.quantity,
                                  'description': entry.product.description}
    return render(request, 'cart/cart.html', context={'cart_products': cart_products})


def delete_cart_view(request, pk):
    profile = request.user
    product = get_object_or_404(Product, pk=pk)
    cart, created = Cart.objects.get_or_create(owner=profile)
    list_of_entries = Entry.objects.filter(cart=cart, product=product)

    for entry in list_of_entries:
        entry.delete()

    return redirect('cart')
