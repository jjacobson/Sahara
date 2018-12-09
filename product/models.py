from django.db import models

# Create your models here.
class ProductCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    description = models.CharField(max_length=255)
    name = models.CharField(max_length=80)
    height = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    width = models.IntegerField(blank=True, null=True)
    depth = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    category = models.ForeignKey('ProductCategory', on_delete=models.CASCADE)
