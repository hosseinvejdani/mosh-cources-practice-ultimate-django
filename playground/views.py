from django.shortcuts import render
from django.db.models.aggregates import Count, Min, Max, Avg, Sum
from store.models import Order, OrderItem, Product


def say_hello(request):

    # How many units of product 1 have we sold?
    result = OrderItem.objects\
        .filter(product_id=1)\
        .aggregate(units_sold=Sum('quantity'))

    # How many orders has customer 1 placed?
    result = Order.objects.filter(customer_id=1).aggregate(order_count=Count('id'))

    # What is the min, max and average price of the products in collection 3?
    result = Product.objects.filter(collection_id=3)\
        .aggregate(
            min=Min('unit_price'),
            max=Max('unit_price'),
            avg=Avg('unit_price')
        )

    return render(request, 'hello.html', {'name': 'Hossein', 'result': result})

