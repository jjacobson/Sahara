from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from product.models import Product


class Cart(models.Model):
    products = models.ManyToManyField(Product)
    count = models.PositiveIntegerField(default=0)
    total = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return "User: {} has {} items in their cart. Their total is ${}".format(self.owner, self.count, self.total)


class Entry(models.Model):
    product = models.ForeignKey(Product, null=True, on_delete='CASCADE')
    cart = models.ForeignKey(Cart, null=True, on_delete='CASCADE')
    quantity = models.PositiveIntegerField()


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
