import json
from django.http import JsonResponse
from django.shortcuts import (get_list_or_404,
                              get_object_or_404,
                              redirect,
                              render)
from utils.transaction import generate_transation_id
from .models import Product, Order, OrderItem, Customer
from .forms import ShippingAddressForm
from django.db.models import Q
from django.contrib import messages


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

        if request.POST:
            form = ShippingAddressForm(request.POST)

            if form.is_valid() and items.count() > 0:
                shipping = form.save(commit=False)

                # Register transation_id in order
                order.transation_id = generate_transation_id()
                order.complete = True
                order.save()

                # Add fields that are not in form
                shipping.customer = customer
                shipping.order = order
                shipping.save()
                return redirect('store:home')

    else:
        items = []
        order = {'get_cart_total': 0,
                 'get_cart_items': 0}

    context = {
        'form': ShippingAddressForm(),
        'order': order,
        'items': items
        }
    return render(request, 'store/pages/checkout.html', context=context)


def update_item(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    customer = get_object_or_404(Customer, user=request.user)
    product = Product.objects.get(id=productId)
    order, _ = Order.objects.get_or_create(
            customer=customer,
            complete=False)

    orderItem, _ = OrderItem.objects.get_or_create(
        order=order,
        product=product
    )

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()
    print(orderItem)

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Update Item', safe=False)


def search(request):

    search_term = request.GET.get('q', '').strip()

    print('search_term')
    print(search_term)

    products = Product.objects.filter(
        Q(name__icontains=search_term)
    ).order_by('-id')

    if not products.exists():
        messages.info(request, 'No results...😢')

    context = {
        'products': products,
        }

    return render(request,
                  'store/pages/product_list.html',
                  context=context)
