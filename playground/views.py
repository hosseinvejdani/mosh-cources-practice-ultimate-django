from django.db.models import Value, F, Func
from django.shortcuts import render
from django.db.models.functions import Concat 
from store.models import Customer, Order, OrderItem, Product


def say_hello(request):

    # annotate new field called full_name in Customer model by 
    # calling database Func, 'CONCAT' in you query
    # method 1
    queryset = Customer.objects.annotate(
        full_name = Func(F('first_name'),Value(' '),F('last_name'),function='CONCAT')
    )

    # method 2 
    queryset = Customer.objects.annotate(
        full_name = Concat('first_name',Value(' '),'last_name')
    )

    # you can find more extra django built-in database functions
    # for handling diffrent datatypes in you queries:
    # https://docs.djangoproject.com/en/3.2/ref/models/database-functions/


    return render(request, 'hello.html', {'name': 'Hossein', 'result': list(queryset)})

