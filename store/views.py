from django.shortcuts import render


def home(request):
    context = {}
    return render(request, 'store/pages/home.html', context=context)


def productList(request):
    context = {}
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
