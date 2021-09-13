from django.shortcuts import render
from store.models import Product


def say_hello(request):

    # find first 5 products
    products = Product.objects.all()[:5]

    # find second 5 products
    products = Product.objects.all()[5:10]

    return render(request, 'hello.html', {'name': 'Hossein', 'products':products})

