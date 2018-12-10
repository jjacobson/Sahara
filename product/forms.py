from django import forms

from cart.models import Review
from .models import Product, ProductCategory


class ProductForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'inputName',
            'placeholder': 'Name',
            'aria-label': 'Name'
        }
    ))

    price = forms.CharField(widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'id': 'inputPrice',
            'aria-label': 'Price'
        }
    ))

    description = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'id': 'inputDescription',
            'placeholder': 'Description',
            'rows': '3',
            'aria-label': 'Description'
        }
    ))

    height = forms.CharField(widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'id': 'inputHeight',
            'placeholder': 'Height',
            'aria-label': 'Height'
        }
    ))

    width = forms.CharField(widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'id': 'inputWidth',
            'placeholder': 'Depth',
            'aria-label': 'Depth'
        }
    ))

    depth = forms.CharField(widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'id': 'inputDepth',
            'placeholder': 'Depth',
            'aria-label': 'Depth'
        }
    ))

    category = forms.ModelChoiceField(queryset=ProductCategory.objects.all(), empty_label=None,
                                      widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Product
        fields = ('name', 'price', 'description', 'height', 'width', 'depth', 'category')


class ReviewForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control title',
            'id': 'inputTitle',
            'placeholder': 'Review Title',
            'aria-label': 'Title'
        }
    ))

    body = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'id': 'inputDescription',
            'placeholder': 'Description',
            'rows': '3',
            'aria-label': 'Description'
        }
    ))

    rating = forms.CharField(widget=forms.NumberInput(
        attrs={
            'class': 'hidden',
            'id': 'inputRating',
            'aria-label': 'Rating'
        }
    ))

    class Meta:
        model = Review
        fields = ('title', 'body', 'rating')
