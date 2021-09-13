from django.shortcuts import render
from store.models import OrderItem, Product


def say_hello(request):

    # # select only title and price for products in dictionary format
    # products = Product.objects.values('id','title') # retrun dictonary

    # # select only title and price for products in tuple format
    # products = Product.objects.values_list('id','title') # retrun tuple

    # select products have been ordered and sort them by title
    product_ids = OrderItem.objects.values('product__id').distinct()
    queryset = Product.objects.filter(pk__in=product_ids).order_by('title')

    return render(request, 'hello.html', {'name': 'Hossein', 'products':list(queryset)})

