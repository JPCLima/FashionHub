from django.shortcuts import get_list_or_404, get_object_or_404, render
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


def product(request, id):
    product = get_object_or_404(Product, pk=id)
    context = {'product': product}
    return render(request, 'store/pages/product.html', context=context)


def category(request, category_id):
    products = get_list_or_404(
        Product.objects.filter(
            category__id=category_id
        ).order_by('-id')
    )
    context = {'products': products}
    return render(request, 'store/pages/product_list.html', context=context)


def cart(request):
    context = {}
    return render(request, 'store/pages/cart.html', context=context)


def checkout(request):
    context = {}
    return render(request, 'store/pages/checkout.html', context=context)
