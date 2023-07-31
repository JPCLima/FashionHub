from django.urls import reverse, resolve
from store import views
from store.tests.test_store_base import StoreTestBase


class StoreCategoryTest(StoreTestBase):
    def test_store_category_view_function_is_correct(self):
        view = resolve(reverse('store:category', kwargs={'category_id': 1}))
        self.assertIs(view.func, views.category)

    def test_store_category_view_loads_correct_template(self):
        # Create product
        product = self.create_product()
        product.save()

        # Get response
        response = self.client.get(reverse('store:category',
                                           kwargs={'category_id': 1}))
        self.assertTemplateUsed(response=response,
                                template_name='store/pages/product_list.html')

    def test_store_category_view_status_200(self):
        # Create product
        product = self.create_product()
        product.save()

        # Get response
        response = self.client.get(reverse('store:category',
                                           kwargs={'category_id': 1}))
        self.assertEqual(response.status_code, 200)

    def test_store_product_view_status_404(self):
        # Get response
        response = self.client.get(reverse('store:category',
                                           kwargs={'category_id': 1}))
        self.assertEqual(response.status_code, 404)
