from store.tests.test_store_base import StoreTestBase
from django.core.exceptions import ValidationError
from store.models import Category, Product


class ProductModelTest(StoreTestBase):

    def setUp(self) -> None:
        self.product = self.create_product()
        return super().setUp()

    def test_store_product_name_max_lenght(self):
        field_name_lenght = Product._meta.get_field('name').max_length
        self.assertEqual(field_name_lenght, 200)

    def test_store_product_unique_name(self):
        # Create a category
        category, _ = Category.objects.get_or_create(name='Shirts')

        # Create an original product
        original_product = Product(
            name='Unique Black Shirt',
            price=30.22,
            category=category)
        original_product.full_clean()
        original_product.save()

        # Attempt to create a duplicate product
        with self.assertRaises(ValidationError):
            duplicate_prod = Product(
                name='Unique Black Shirt',
                price=30.22,
                category=category)
            duplicate_prod.full_clean()

    def test_store_invalid_price_raises_validation_error(self):
        # Create new product with negative value
        prod_neg_price = self.create_product(
            name='Blue Shirt',
            price=-59.99,
        )

        # Validation of the price
        with self.assertRaises(ValidationError):
            prod_neg_price.full_clean()

    def test_store_product_positive_price(self):
        prod_valid_price = self.create_product(
            name='validProduct',
            price=29.99
        )
        prod_valid_price.full_clean()

    def test_store_product_field_is_null_or_blank(self):
        product = Product.objects.get(name='Black Shirt')
        field = product._meta.get_field('name')
        self.assertFalse(field.null)
        self.assertFalse(field.blank)

    def test_store_product_has_correct_category(self):
        # Create new product and save it to database
        new_product = self.create_product(
            name='Red Shirt',
            price=59.99,
        )
        new_product.full_clean()
        new_product.save()

        # Check if they are the same
        self.assertEqual(new_product.category.name, 'Shirts')

    def test_store_product_string_representation(self):
        self.assertEqual(str(self.product), str(self.product.name))
