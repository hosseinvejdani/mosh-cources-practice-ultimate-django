from django.db.models import Value, F, Func, Count,ExpressionWrapper
from django.db.models.fields import DecimalField
from django.shortcuts import render
from django.db.models.functions import Concat 
from store.models import Customer, Order, OrderItem, Product


def say_hello(request):

    # by expressionswrapper you can build complex expressions:
    # for example you can annotate new field to product called
    # discounted_price like this:
    discounted_price = ExpressionWrapper(F('unit_price') * 0.8,output_field=DecimalField())
    queryset = Product.objects.annotate(
        discounted_price = discounted_price
    )

    return render(request, 'hello.html', {'name': 'Hossein', 'result': list(queryset)})

