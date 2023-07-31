from django.shortcuts import get_list_or_404, render
from .models import Product


def home(request):
    context = {}
    return render(request, 'store/pages/home.html', context=context)


def productList(request):
    products = get_list_or_404(
        Product.objects.all().order_by('-id')
    )
    context = {'products': products}
    return render(request, 'store/pages/product_list.html', context=context)


def product(request, pk):
    context = {}
    return render(request, 'store/pages/product.html', context=context)


def cart(request):
    context = {}
    return render(request, 'store/pages/cart.html', context=context)


def checkout(request):
    context = {}
    return render(request, 'store/pages/checkout.html', context=context)
