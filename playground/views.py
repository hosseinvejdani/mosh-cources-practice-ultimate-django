from django.db.models import query
from django.shortcuts import render
from store.models import Collection, OrderItem, Product
from django.db.models import Q


def say_hello(request):
    # # find all the products : inventory < 10 AND unit_price < 20 --> Method 1
    # queryset = Product.objects.filter(inventory__lt=10,unit_price__lt=20)
    # list(queryset)

    # find all the products : inventory < 10 AND unit_price < 20 --> Method 2
    # queryset = Product.objects.filter(inventory__lt=10).filter(unit_price__lt=20)
    # list(queryset)

    # # # find all the products : inventory < 10 AND unit_price < 20 --> Method 3
    # queryset = Product.objects.filter(Q(inventory__lt=10) & Q(unit_price__lt=20))
    # list(queryset)

    # # # find all the products : inventory < 10 OR unit_price < 20 
    # queryset = Product.objects.filter(Q(inventory__lt=10) & Q(unit_price__lt=20))
    # list(queryset)

    # # find all the products : inventory < 10 OR inventory > 50 AND unit_price > 30 
    queryset = Product.objects.filter(Q(inventory__lt=10) | Q(inventory__gt=50) & Q(unit_price__gt=30))
    list(queryset)

    return render(request, 'hello.html', {'name': 'Hossein'})

