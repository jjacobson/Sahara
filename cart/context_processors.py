from cart.models import Cart


def cart_processor(request):
    cart = None
    if not request.user.is_anonymous:
        cart, created = Cart.objects.get_or_create(owner=request.user)

    return {'cart': cart}
