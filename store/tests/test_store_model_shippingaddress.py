from store.models import ShippingAddress
from django.core.exceptions import ValidationError
from parameterized import parameterized
from store.tests.test_store_base import StoreTestBase


class ShippingAddressModelTest(StoreTestBase):

    def setUp(self) -> None:
        super().setUp()
        self.product = self.create_product()
        self.order = self.create_order()
        self.order_item = self.create_order_item()
        self.shipping_address = self.create_shipping_address()

    def test_store_shipping_address_creation(self):
        self.assertIsInstance(self.shipping_address, ShippingAddress)
        self.assertEqual(self.shipping_address.order.complete, False)
        self.assertEqual(self.shipping_address.order.customer.name,
                         'testcustomer')
        self.assertEqual(self.shipping_address.address, 'addresstest')
        self.assertEqual(self.shipping_address.city, 'citytest')
        self.assertEqual(self.shipping_address.state, 'statetest')
        self.assertEqual(self.shipping_address.zipcode, '123456')

    @parameterized.expand([
        ('address', 200),
        ('city', 200),
        ('state', 200),
        ('zipcode', 200),
    ])
    def test_store_shiiping_address_max_lenght(self, field, max_length):
        setattr(self.shipping_address, field, 'A' * (max_length + 1))
        with self.assertRaises(ValidationError):
            self.shipping_address.full_clean()

    def test_store_order_item_string_represenation(self):
        self.assertEqual(str(self.shipping_address), 'testcustomer')
