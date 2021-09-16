from django.shortcuts import render
from store.models import OrderItem, Product


def say_hello(request):

    # -> select_related(*fields)
    # Returns a QuerySet that will “follow” foreign-key relationships,
    # selecting additional related-object data when it executes its query.
    # This is a performance booster which results in a single more
    # complex query but means later use of foreign-key relationships
    #  won’t require database queries.
    queryset = Product.objects.select_related('collection').all()
    # if you dont use select_related here and render 
    # product.collection.title in html file, you will send 1000 extra 
    # query for 1000 products



    return render(request, 'hello.html', {'name': 'Hossein', 'products':list(queryset)})

