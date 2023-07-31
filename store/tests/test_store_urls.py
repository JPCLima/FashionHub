from django.test import TestCase
from django.urls import reverse


class StoreURLsTest(TestCase):

    def test_store_home_url_is_correct(self):
        home_url = reverse('store:home')
        self.assertEqual(home_url, '/')

    def test_store_product_list_url_is_correct(self):
        product_list_url = reverse('store:products')
        self.assertEqual(product_list_url, '/products/')

    def test_store_product_details_url_is_correct(self):
        product_url = reverse('store:product', kwargs={'id': 1})
        self.assertEqual(product_url, '/products/1/')

    def test_store_cart_url_is_correct(self):
        cart_url = reverse('store:cart')
        self.assertEqual(cart_url, '/cart')

    def test_store_checkout_url_is_correct(self):
        checkout_url = reverse('store:checkout')
        self.assertEqual(checkout_url, '/checkout')
