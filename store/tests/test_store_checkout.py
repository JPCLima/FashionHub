from django.urls import reverse, resolve
from store import views
from store.tests.test_store_base import StoreTestBase


class StoreCheckoutViewTest(StoreTestBase):
    def setUp(self) -> None:
        super().setUp()
        self.client.login(username='testuser',
                          password='testpass')

    def test_store_checkout_view_function_is_correct(self):
        view = resolve(reverse('store:checkout'))
        self.assertIs(view.func, views.checkout)

    def test_store_checkout__view_authenticated_user(self):
        response = self.client.get(reverse('store:checkout'))
        self.assertEqual(response.status_code, 200)

    def test_store_checkout_view_guest_user_content(self):
        self.client.logout()

        response = self.client.get(reverse('store:cart'))
        self.assertEqual(response.context['order']['get_cart_total'], 0)
        self.assertEqual(response.context['order']['get_cart_items'], 0)

        self.assertContains(response, 'Order Total: 0')
        self.assertContains(response, 'Items: 0')
