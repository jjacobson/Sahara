from django.shortcuts import render, redirect

# Create your views here.
from product.forms import ProductForm
from .models import ProductCategory

def sell_item(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            print('valid form, saving')
            product = form.save()
            product.save()
            return redirect('index')
        else:
            print(form.errors)
            print(request.POST)
            print('invalid form')
    else:
        form = ProductForm()
    return render(request, 'product/list-item.html', {'form': form})
