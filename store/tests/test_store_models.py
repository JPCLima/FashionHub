from store.models import Customer

from store.tests.test_store_base import StoreTestBase


class CustomerModelsTest(StoreTestBase):
    def test_customer_field_is_null_or_black(self):
        customer = Customer.objects.get(id=1)
        field = customer._meta.get_field('user')
        self.assertTrue(field.null)
        self.assertTrue(field.blank)

    def test_customer_name_field_max_lenght(self):
        customer = Customer.objects.get(id=1)
        max_lenght_name = customer._meta.get_field('name').max_length
        self.assertEqual(max_lenght_name, 200)

    def test_customer_email_field_max_lenght(self):
        customer = Customer.objects.get(id=1)
        max_lenght_email = customer._meta.get_field('email').max_length
        self.assertEqual(max_lenght_email, 200)
