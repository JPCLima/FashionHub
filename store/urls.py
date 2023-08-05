from django.urls import path
from . import views

# Namespacing of the app
app_name = 'store'

# Routes
urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.productList, name='products'),
    path('products/category/<int:category_id>/',
         views.category,
         name='category'),
    path('products/<int:id>/', views.product, name='product'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
]
