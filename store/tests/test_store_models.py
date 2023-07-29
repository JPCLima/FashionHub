from store.models import Customer
from django.core.exceptions import ValidationError
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

    def test_customer_invalid_email_raises_validation_error(self):
        # Define new user to avoid duplication
        user_no_email = {
            'username': 'NoEmailUsername',
            'password': 'password123',
        }

        # Create new customer
        customer = self.create_customer(
            user=user_no_email,
            name='customerInvalidEmail',
            email='this is an invalid email')

        # Validation
        with self.assertRaises(ValidationError):
            customer.full_clean()

    def test_customer_blank_email_validation_error(self):
        # Define new user to avoid duplication
        user_no_email = {
            'username': 'NoEmailUsername',
            'password': 'password123',
        }

        # Create customer with blanck email
        customer = self.create_customer(
            user=user_no_email,
            name='UserBlankEmail',
            email=''
        )

        # Validation
        with self.assertRaises(ValidationError):
            customer.full_clean()

    def test_customer_string_represenation(self):
        expected_string = 'testcustomer'
        self.assertEqual(str(self.customer), expected_string)
