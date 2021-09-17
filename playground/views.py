from django.shortcuts import render
from django.db.models.aggregates import Count, Min, Max, Avg
from store.models import Order, OrderItem, Product


def say_hello(request):

    # Count of objects with defalt name
    result = Product.objects.aggregate(Count('id'))   # return result with name id__count as a dictonary
    
    # Count of objects with custom name
    result = Product.objects.aggregate(count=Count('id')) # return result with name count as a dictonary

    # you can get Min, Max and Avg values for objects at the same way

    # you can also use multiple args in aggregate method:
    result = Product.objects.aggregate(count=Count('id'),max_price=Max('unit_price')) 

    # you can also make a custom queryset with  before aggregating, like this:
    result = Product.objects.filter(collection_id=3).aggregate(count=Count('id'),max_price=Max('unit_price')) 

    return render(request, 'hello.html', {'name': 'Hossein', 'result': result})

