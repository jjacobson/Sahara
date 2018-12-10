from django.shortcuts import get_object_or_404, render

from product.models import Product
from users.models import CustomUser


def profile_view(request, pk):
    profile = get_object_or_404(CustomUser, pk=pk)
    products = profile.product_set.all()
    return render(request, 'profile/profile.html', context={'profile': profile, 'products': products})
