from django.shortcuts import render
from store.models import Product


def say_hello(request):


    # # sort products by title in ASC order and render first 5 of them
    # products = Product.objects.order_by('title')[:5]

    # # sort products by title in DSC order and render first 5 of them
    # products = Product.objects.order_by('-title')[:5]

    # # sort products by title in DSC order then reverse its direction and render first 5 of them
    # products = Product.objects.order_by('-title').reverse()[:5]
    
    # # sort products by unit_price in ASC oreder and then sort them by 
    # # title in DSC order and render first 10 of them
    # products = Product.objects.order_by('unit_price','-title')[:10]

    # # find cheapest product in collection 3
    # products = Product.objects.filter(collection__id=3).order_by('unit_price')[0]

    # # find 5 cheapest products in collection 3
    # products = Product.objects.filter(collection__id=3).order_by('unit_price')[:5]

    # # find cheapest product in collection 3
    # products = Product.objects.filter(collection__id=3).earliest('unit_price')

    # find most expensive product in collection 3
    products = Product.objects.filter(collection__id=3).latest('unit_price')


    return render(request, 'hello.html', {'name': 'Hossein'})

