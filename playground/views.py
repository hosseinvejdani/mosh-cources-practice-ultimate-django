from django.db.models import Value, F
from django.shortcuts import render
from django.db.models.aggregates import Count, Min, Max, Avg, Sum
from store.models import Customer, Order, OrderItem, Product


def say_hello(request):

    #  Annotate method : Annotates each object in the
    #  QuerySet with the provided list of query expressions.
    #  An expression may be a simple value, a reference to a
    #  field on the model (or any related models), or an aggregate
    #  expression (averages, sums, etc.) that has been computed
    #  over the objects that are related to the objects in the QuerySet.

    # prcatice 1 :
    # add new field to customer called is_new with defalut True value
    # in this case you should use Value() method
    queryset = Customer.objects.annotate(is_new=Value(True))
    # you can use it multiple time :
    queryset = Customer.objects.annotate(is_new=Value(True),is_old=Value(False))

    # practice 2 :
    # add new attribute to orderitem with annotate method
    # which calculate and shows total price as new field -> 'total_price'
    queryset = OrderItem.objects.annotate(total_price = F('unit_price')*F('quantity'))
    # as you can see, you can perform computional task here in  annotate method using F methods

    return render(request, 'hello.html', {'name': 'Hossein', 'result': list(queryset)})

