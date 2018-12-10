from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from product.models import Product
from users.models import Address


class Cart(models.Model):
    products = models.ManyToManyField(Product)
    count = models.PositiveIntegerField(default=0)
    total = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return "User: {} has {} items in their cart. Their total is ${}".format(self.owner, self.count, self.total)


class Entry(models.Model):
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, null=True, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()


class Transaction(models.Model):
    #seller = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    buyer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)


class Receipt(models.Model):
    #sell_date = models.DateTimeField()
    #ship_date = models.DateTimeField()
    #ship_company = models.CharField(max_length=100)
    #ship_track = models.CharField(max_length=40)
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)


class Review(models.Model):
    title = models.CharField(max_length=50)
    body = models.CharField(max_length=255)
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    #receipt = models.ForeignKey(Receipt, on_delete=models.CASCADE)
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)



@receiver(post_save, sender=Entry)
def update_cart(sender, instance, **kwargs):
    line_cost = instance.quantity * instance.product.price
    instance.cart.total += line_cost
    instance.cart.count += instance.quantity
    instance.cart.save()


@receiver(post_delete, sender=Entry)
def delete_cart_products(sender, instance, **kwargs):
    line_cost = instance.quantity * instance.product.price
    instance.cart.total -= line_cost
    instance.cart.count -= instance.quantity
    instance.cart.save()
