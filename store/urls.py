from django.urls import path
from .views import cart, checkout, product, productList, store

# Namespacing of the app
app_name = 'store'

# Routes
urlpatterns = [
    path('', store, name='store'),
    path('productList', productList, name='productList'),
    path('product/<str:pk>', product, name='product'),
    path('cart', cart, name='cart'),
    path('checkout', checkout, name='checkout'),
]
