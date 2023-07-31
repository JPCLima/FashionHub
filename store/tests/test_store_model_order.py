from store.tests.test_store_base import StoreTestBase
from datetime import timedelta
from django.utils import timezone


class OrderModelTest(StoreTestBase):

    def test_store_order_date_ordered_auto_populated(self):
        # Create a new order
        order = self.create_order()

        now = timezone.now()
        delta = timedelta(seconds=1)
        self.assertIsNotNone(order.date_ordered)
        self.assertGreaterEqual(order.date_ordered, now - delta)
        self.assertLessEqual(order.date_ordered, now)

    def test_store_order_default_complete_value(self):
        # Create a new order
        order = self.create_order()

        # Check if transition if is null
        self.assertFalse(order.complete)

    def test_store_transition_id_null(self):
        # Create a new order
        order = self.create_order()

        self.assertIsNone(order.transation_id)

    def test_store_order_string_representation(self):
        order = self.create_order()
        self.assertEqual(str(order), str(order.id))
