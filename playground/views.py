from django.shortcuts import render
from store.models import OrderItem, Product


def say_hello(request):


    # but in the case of filed with many-to-many relationships you should 
    # use prefetch_related. like this:
    queryset = Product.objects.prefetch_related('promotions').all()



    return render(request, 'hello.html', {'name': 'Hossein', 'products':list(queryset)})

