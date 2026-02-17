from django.db import models
from django.core.validators import MinValueValidator , MaxValueValidator
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Supllier(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Manufacturer(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name

class Product(models.Model):
    article = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    unit = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    supplier = models.ForeignKey(
        Supllier,
        on_delete=models.PROTECT,
        related_name = 'product',
    )
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete = models.PROTECT,
        related_name = 'product'
    )
    category = models.ForeignKey(
        Category,
        on_delete = models.PROTECT,
        related_name = 'product'
    )
    discount = models.PositiveIntegerField(
        default = 0,
        validators = [MinValueValidator(0), MaxValueValidator(99)]
    )
    quantity = models.PositiveIntegerField(default = 0)
    description = models.TextField(blank = True)
    image = models.ImageField(
        upload_to = 'products',
        blank = True,
        null = True,

    )
    def __str__(self):
        return self.name