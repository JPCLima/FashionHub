from django.test import TestCase
from store.models import Customer, Category, Product, Order, OrderItem, ShippingAddress  # noqa: E501
from django.contrib.auth.models import User


class StoreTestBase(TestCase):
    def setUp(self) -> None:
        self.customer = self.create_customer()
        return super().setUp()

    def create_user(self,
                    username='testuser',
                    password='testpass'):
        return User.objects.create(
            username=username,
            password=password)

    def create_customer(self,
                        user=None,
                        name='testcustomer',
                        email='testemail@email.com'):
        if user is None:
            user = {}

        return Customer.objects.create(
            user=self.create_user(**user),
            name=name,
            email=email
        )

    def create_category(self, name='Shirts'):
        category, _ = Category.objects.get_or_create(name=name)
        return category

    def create_product(self,
                       name='Black Shirt',
                       price=20.99,
                       category=None):

        if category is None:
            category, _ = Category.objects.get_or_create(name='Shirts')

        return Product.objects.create(
            name=name,
            price=price,
            category=category)

    def create_order(self,
                     customer=None,
                     date_ordered=None,
                     complete=False):
        if customer is None:
            customer = self.customer

        return Order.objects.create(
            customer=customer,
            date_ordered=date_ordered,
            complete=complete,
        )

    def create_order_item(self,
                          product=None,
                          order=None,
                          quantity=1):
        return OrderItem.objects.create(
            product=self.product,
            order=self.order,
            quantity=0
        )

    def create_shipping_address(self,
                                customer=None,
                                order=None,
                                address='addresstest',
                                city='citytest',
                                state='statetest',
                                zipcode='123456'):
        if customer is None:
            customer = self.customer

        return ShippingAddress(
            customer=customer,
            order=self.order,
            address=address,
            city=city,
            state=state,
            zipcode=zipcode
        )
