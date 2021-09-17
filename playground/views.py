from django.db.models import F, Count,Max, Sum
from django.shortcuts import render
from store.models import Collection, Customer, Product


def say_hello(request):

    # Write code to get Customers with their last order ID
    queryset = Customer.objects.annotate(last_order_id=Max('order__id'))


    # Write code to get Collections and count of their products
    queryset = Collection.objects.annotate(products_count=Count('product'))


    # Write code to get Customers with more than 5 orders
    queryset = Customer.objects.annotate(order_count = Count('order')).filter(order_count__gt=5)


    # Write code to get Customers and the total amount they’ve spent
    queryset = Customer.objects.annotate(
        total_payment = Sum(
            F('order__orderitem__unit_price') * \
            F('order__orderitem__quantity')
        )
    )


    # Write code to get Top 5 best-selling products and their total sales with differed description
    queryset = Product.objects.annotate(
        total_sale = Sum(
            F('orderitem__unit_price') * \
            F('orderitem__quantity')
        ),
        collection_name = F('collection__title')
    ).order_by('-total_sale').defer('description')[:5]



    return render(request, 'hello.html', {'name': 'Hossein', 'result': list(queryset)})

