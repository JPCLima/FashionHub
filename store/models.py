from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


class Customer(models.Model):
    user = models.ForeignKey(User,
                             null=True,
                             blank=True,
                             on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.name


class Category(models.Model):

    SHIRTS = 'Shirts'
    SWEATER = 'Sweater'
    T_SHIRT = 'T-shirt'
    JACKET = 'Jacket'

    CLOTHING_CATEGORIES = [
        (SHIRTS, 'Shirts'),
        (SWEATER, 'Sweater'),
        (T_SHIRT, 'T-shirt'),
        (JACKET, 'Jacket'),
    ]

    name = models.CharField(
        max_length=65,
        unique=True,
        choices=CLOTHING_CATEGORIES)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200, unique=True)
    price = models.FloatField(validators=[MinValueValidator(0.0)])
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True,
        default=None,
    )

    def __str__(self):
        return self.name


# Order
# OrderItem
# Shipping
