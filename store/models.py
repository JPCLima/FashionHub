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

    class Meta:
        verbose_name = "Customer"

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

    class Meta:
        verbose_name_plural = "Categories"

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


class Order(models.Model):
    customer = models.ForeignKey(Customer,
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transation_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    product = models.ForeignKey(Product,
                                on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order,
                              on_delete=models.SET_NULL,
                              null=True)
    quantity = models.IntegerField(validators=[MinValueValidator(0)],
                                   default=0,
                                   null=True,
                                   blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer,
                                 on_delete=models.SET_NULL,
                                 blank=True,
                                 null=True)
    order = models.ForeignKey(Order,
                              on_delete=models.SET_NULL,
                              blank=True,
                              null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer.name
