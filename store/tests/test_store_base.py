from django.test import TestCase
from store.models import Customer
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
