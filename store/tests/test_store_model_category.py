from store.models import Category
from django.core.exceptions import ValidationError
from store.tests.test_store_base import StoreTestBase


class CategoryModelTest(StoreTestBase):
    def setUp(self) -> None:
        self.category = self.create_category(name='Shirts')
        return super().setUp()

    def test_store_category_name_max_length_validation(self):
        category_name = self.category.name
        self.assertEqual(category_name, 'Shirts')

    def test_store_category_name_max_length(self):
        category_maxlen = self.category._meta.get_field('name').max_length
        self.assertEqual(category_maxlen, 65)

    def test_store_category_name_is_required_validation(self):
        # Create a category without name
        cat_no_name = Category.objects.create()

        # Validation
        with self.assertRaises(ValidationError):
            cat_no_name.full_clean()

    def test_store_category_is_unique(self):
        # Create a category
        original_category = self.create_category(name='Test Shirts')
        original_category.save()

        # Attempt to create a duplicate category
        duplicate_category = Category(name='Test Shirts')
        with self.assertRaises(ValidationError):
            duplicate_category.full_clean()

    def test_customer_string_represenation(self):
        self.assertEqual(str(self.category), str(self.category.name))
