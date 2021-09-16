from django.shortcuts import render
from store.models import OrderItem, Product


def say_hello(request):

    # Whenever you call only() it replaces the set of fields to load immediately.
    # we can access to 'title' and 'id' immediately in hello.html
    # but if we want to render product.unit_price in .html file, out web all
    # will freeze, since it defered by .only() method and rendering it cause 1000 extra 
    # queries in our case, becouse we have 1000 product in our database 
    # The only() method is more or less the opposite of defer(). 
    # the diiference of only() and values() methos is that by calling values()
    # method you get data as a dictionary but in the case of only()
    # method you get object instance.
    queryset = Product.objects.defer('description')


    return render(request, 'hello.html', {'name': 'Hossein', 'products':list(queryset)})

