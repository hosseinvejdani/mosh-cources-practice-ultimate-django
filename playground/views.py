from django.db.models import query
from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Collection, OrderItem, Product


def say_hello(request):
    # # find all the products that are $4
    # queryset = Product.objects.filter(unit_price=4)

    # # find all the products that are grather than $4
    # queryset = Product.objects.filter(unit_price__gt=4)

    # # find all the products that are grather than or equal to $4
    # queryset = Product.objects.filter(unit_price__gte=4)

    # # find all the products that are less than 
    # queryset = Product.objects.filter(unit_price__lt=4)

    # # find all the products that are less than or equal to $4
    # queryset = Product.objects.filter(unit_price__lte=4)

    # # find all the products that are in range $4 ~ $20
    # queryset = Product.objects.filter(unit_price__range=(4,20))

    # # find all the products which is in collection 3
    # queryset = Product.objects.filter(collection__id=3)

    # # find all the products which is in collection_id >=5
    # queryset = Product.objects.filter(collection__id__gte=5)

    # # find all the products which is its collection_id in range(2,6)
    # queryset = Product.objects.filter(collection__id__range=(2,6))

    # # find all the products which thire title contains sensitive case 'coffe'
    # queryset = Product.objects.filter(title__contains='coffee')

    # # find all the products which thire title contains insensitive case 'coffe'
    # queryset = Product.objects.filter(title__icontains='coffee')

    # # find all the products which thire title start with sensitive case 'coffe'
    # queryset = Product.objects.filter(title__startswith='coffee')

    # # find all the products which thire title starts with insensitive case 'coffe'
    # queryset = Product.objects.filter(title__istartswith='coffee')

    # # find all the products which thire title ends with sensitive case 'coffe'
    # queryset = Product.objects.filter(title__endswith='coffee')

    # # find all the products which thire title ends with insensitive case 'coffe'
    # queryset = Product.objects.filter(title__iendswith='coffee')

    # # find all products that updataed at year 2021
    # queryset = Product.objects.filter(last_update__year=2021)

    # # find all products which their decriptions is null
    # queryset = Product.objects.filter(description__isnull=False)

    # find all order items for products in collection 3
    queryset = OrderItem.objects.filter(product__collection__id=5)
    list(queryset)

    return render(request, 'hello.html', {'name': 'Hossein'})

