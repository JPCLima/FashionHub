from django.shortcuts import get_list_or_404, get_object_or_404, render
from .models import Product, Order, Customer


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
    if request.user.is_authenticated:
        customer = Customer.objects.get(user=request.user)
        order, _ = Order.objects.get_or_create(
            customer=customer,
            complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0,
                 'get_cart_items': 0}

    context = {
        'order': order,
        'items': items
        }
    return render(request, 'store/pages/cart.html', context=context)


def checkout(request):
    if request.user.is_authenticated:
        customer = get_object_or_404(Customer, user=request.user)
        order, _ = Order.objects.get_or_create(
            customer=customer,
            complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0,
                 'get_cart_items': 0}

    context = {
        'order': order,
        'items': items
        }
    return render(request, 'store/pages/checkout.html', context=context)
