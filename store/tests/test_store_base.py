from django.test import TestCase
from store.models import Customer
from django.contrib.auth.models import User


class StoreTestBase(TestCase):
    def setUp(self) -> None:
        self.customer = self.create_customer()
        return super().setUp()

    def create_user(self):
        return User.objects.create(
            username='testuser',
            password='testpass')

    def create_customer(self):
        return Customer.objects.create(
            user=self.create_user(),
            name='testcustomer',
            email='testemail'
        )
