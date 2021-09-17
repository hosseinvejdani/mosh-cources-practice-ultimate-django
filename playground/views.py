from django.db.models import Value, F, Func, Count
from django.shortcuts import render
from django.db.models.functions import Concat 
from store.models import Customer, Order, OrderItem, Product


def say_hello(request):

    # add new field to customer that shows total order that each 
    # customer has been placed
    queryset = Customer.objects.annotate(
        order_count = Count('order')
    )

    # add new field to product that shows total numbers that this product exist in orders
    queryset = Product.objects.annotate(
        orderitem_count = Count('orderitem')
    )

    return render(request, 'hello.html', {'name': 'Hossein', 'result': list(queryset)})

