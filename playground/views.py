from django.shortcuts import render
from django.db.models import F
from store.models import Product


def say_hello(request):


    # # find all the products : inventory = unit_price (this is not sence here but shows F application)
    # queryset = Product.objects.filter(inventory=F('unit_price'))
    # list(queryset)

    # find all the products : inventory = collection_id (this is not sence here but shows F application)
    # queryset = Product.objects.filter(inventory=F('collection__id'))   # or we can use:
    queryset = Product.objects.filter(inventory=F('collection_id'))
    list(queryset)

    return render(request, 'hello.html', {'name': 'Hossein'})

