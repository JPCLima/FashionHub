from django.urls import path
from . import views

# Namespacing of the app
app_name = 'store'

# Routes
urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.productList, name='products'),
    path('products/search', views.search, name='search'),
    path('cart/', views.cart, name='cart'),
    path('update_item/', views.update_item, name='update_item'),
    path('checkout/', views.checkout, name='checkout'),
    path('products/<int:id>/', views.product, name='product'),
    path('products/category/<int:category_id>/',
         views.category,
         name='category')
]
