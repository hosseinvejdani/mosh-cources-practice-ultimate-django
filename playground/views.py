from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from tags.models import TaggedItem
from store.models import Collection, Customer, Product


def say_hello(request):

    queryset = TaggedItem.objects.get_tags_for(Product,1)

       

    return render(request, 'hello.html', {'name': 'Hossein', 'result': list(queryset)})

