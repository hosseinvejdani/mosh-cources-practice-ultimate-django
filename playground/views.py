from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product


def say_hello(request):
    # # method 1
    # try:
    #     product = Product.objects.filter(pk=0)
    # except ObjectDoesNotExist:
    #     pass

    # # method 2
    # product = Product.objects.filter(pk=1).first()

    # method 3
    exist = Product.objects.filter(pk=1).exists()

    return render(request, 'hello.html', {'name': 'Mosh'})

