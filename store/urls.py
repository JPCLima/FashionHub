from django.urls import path

from .views import product, productList, store

urlpatterns = [
    path('', store, name='store'),
    path('productList', productList, name='productList'),
    path('product/<str:pk>', product, name='product'),
]