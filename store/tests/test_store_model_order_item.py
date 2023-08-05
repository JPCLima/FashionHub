from store.models import OrderItem
from django.core.exceptions import ValidationError
from store.tests.test_store_base import StoreTestBase


class OrderItemModelTest(StoreTestBase):

    def setUp(self) -> None:
        super().setUp()
        self.product = self.create_product()
        self.order = self.create_order()
        self.order_item = self.create_order_item()

    def test_store_order_item_creation(self):
        self.assertIsInstance(self.order_item, OrderItem)
        self.assertEqual(self.order_item.product.name, 'Black Shirt')
        self.assertEqual(self.order_item.order.customer.name, 'testcustomer')
        self.assertEqual(self.order_item.quantity, 1)

    def test_store_order_item_quantity_blank_null(self):
        field_quantity = self.order_item._meta.get_field('quantity')
        self.assertTrue(field_quantity.blank)
        self.assertTrue(field_quantity.null)
        self.assertEqual(field_quantity.default, 0)

    def test_store_order_item_negative_quantity_raises_validation_error(self):
        self.order_item.quantity = -2
        with self.assertRaises(ValidationError):
            self.order_item.full_clean()

    def test_store_order_item_zero_quantity(self):
        self.order_item.quantity = 0
        self.order_item.full_clean()

    def test_store_order_item_string_represenation(self):
        self.assertEqual(str(self.order_item), 'Black Shirt')
