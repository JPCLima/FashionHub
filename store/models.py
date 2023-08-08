from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


class Customer(models.Model):
    user = models.OneToOneField(User,
                                null=True,
                                blank=True,
                                on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200)

    class Meta:
        verbose_name = "Customer"

    def __str__(self):
        return self.name

    def get_cart(self):
        return self.order_set.filter(complete=False).first()


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
    image = models.ImageField(upload_to='store/images/%Y/%m/%d/',
                              blank=True,
                              default='')

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

    @property
    def get_cart_items(self):
        return sum(item.quantity for item in self.orderitem_set.all())

    @property
    def get_cart_total(self):
        order_items = self.orderitem_set.all()
        total = sum([item.get_total for item in order_items])
        return total


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

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


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
