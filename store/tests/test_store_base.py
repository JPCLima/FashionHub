from django.test import TestCase
from store.models import Customer, Product, Category
from django.contrib.auth.models import User


class StoreTestBase(TestCase):
    CLOTHING_CATEGORIES = {
            'Shirts': Category.SHIRTS,
            'Sweater': Category.SWEATER,
            'T-shirt': Category.T_SHIRT,
            'Jacket': Category.JACKET,
            }

    def setUp(self) -> None:
        self.customer = self.create_customer()
        self.product = self.create_product()
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
        category = StoreTestBase.CLOTHING_CATEGORIES.get(name)
        return Category.objects.create(name=category)

    def create_product(self,
                       name='Jacket',
                       price='20.99',
                       category=None):

        if category is None:
            category = {'name': Category.SHIRTS}

        return Product.objects.create(
            name=name,
            price=price,
            category=self.create_category(**category))
