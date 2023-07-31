from django.urls import reverse, resolve
from store import views
from store.tests.test_store_base import StoreTestBase
from store.models import Category


class StoreProductListTest(StoreTestBase):

    def test_list_products_view_function_is_correct(self):
        view = resolve(reverse('store:productList'))
        self.assertIs(view.func, views.productList)

    def test_list_products_view_loads_correct_template(self):
        # Create product
        product = self.create_product()
        product.save()

        # Get response
        response = self.client.get(reverse('store:productList'))
        self.assertTemplateUsed(response=response,
                                template_name='store/pages/product_list.html')

    def test_list_products_view_get_status_200(self):
        product = self.create_product()
        product.save()
        response = self.client.get(reverse('store:productList'))
        self.assertEqual(response.status_code, 200)

    def test_list_products_view_get_status_404(self):
        response = self.client.get(reverse('store:productList'))
        self.assertEqual(response.status_code, 404)

    def test_product_list_view_loads_content(self):
        # Get product
        self.create_product()

        # Get response
        response = self.client.get(reverse('store:productList'))
        response_context = response.context['products']

        self.assertEqual(response_context[0].name, 'Black Shirt')
        self.assertEqual(response_context[0].price, 20.99)
        self.assertEqual(response_context[0].category.name,
                         Category.SHIRTS)
