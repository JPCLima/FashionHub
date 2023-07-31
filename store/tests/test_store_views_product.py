from django.urls import reverse, resolve
from store import views
from store.tests.test_store_base import StoreTestBase
from store.models import Category


class StoreProductTest(StoreTestBase):
    def test_store_product_view_function_is_correct(self):
        view = resolve(reverse('store:product', kwargs={'id': 1}))
        self.assertIs(view.func, views.product)

    def test_store_product_view_loads_correct_template(self):
        # Create product
        product = self.create_product()
        product.save()

        # Get response
        response = self.client.get(reverse('store:product', kwargs={'id': 1}))
        self.assertTemplateUsed(response=response,
                                template_name='store/pages/product.html')

    def test_store_product_view_status_200(self):
        # Create product
        product = self.create_product()
        product.save()

        # Get response
        response = self.client.get(reverse('store:product', kwargs={'id': 1}))
        self.assertEqual(response.status_code, 200)

    def test_store_product_view_status_404(self):
        # Get response
        response = self.client.get(reverse('store:product', kwargs={'id': 1}))
        self.assertEqual(response.status_code, 404)

    def test_store_product_view_loads_content(self):
        # Create product
        product = self.create_product()
        product.save()

        # Get response
        response = self.client.get(reverse('store:product', kwargs={'id': 1}))
        response_context = response.context['product']

        self.assertEqual(response_context.name, 'Black Shirt')
        self.assertEqual(response_context.price, 20.99)
        self.assertEqual(response_context.category.name,
                         Category.SHIRTS)
