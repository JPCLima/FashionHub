from django.shortcuts import render


def store(request):
    context = {}
    return render(request, 'store/home.html', context=context)


def productList(request):
        context = {}
        return render(request, 'store/product_list.html', context=context)


def product(request, pk):
    context = {}
    return render(request, 'store/product.html', context=context)
