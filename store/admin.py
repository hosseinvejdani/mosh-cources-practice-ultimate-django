from django.contrib import admin
from django.db.models.aggregates import Count
from django.utils.html import format_html, urlencode
from django.urls import reverse
from . import models 

# Register your models here.

@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title','products_count']
    list_per_page = 10

    @admin.display(ordering='products_count')
    def products_count(self,collection):
        url = (reverse('admin:store_product_changelist') 
        + '?' 
        + urlencode({
            'collection__id': collection.id,
        }))  
        return format_html('<a href={}> {} </a>',url,collection.products_count)
    
    def get_queryset(self, request) :
        return super().get_queryset(request)\
            .annotate(products_count=Count('product'))


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','unit_price','collection','inventory','inventory_status']
    list_editable = ['unit_price','inventory']
    list_filter = ['collection','last_update ']
    list_per_page = 10

    @admin.display(ordering='inventory')
    def inventory_status(self,product):
        if product.inventory < 10 :
            return 'Low'
        else:
            return 'Ok'



@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','membership','orders_count']
    list_editable = ['membership']
    ordering = ['first_name','last_name']
    list_per_page = 10
    search_fields = [
        'first_name__istartswith',
        'last_name__istartswith',
        ]

    @admin.display(ordering='orders_count')
    def orders_count(self,customer):
        url = (reverse('admin:store_order_changelist')
            + '?'
            + urlencode({
                'customer__id':customer.id
            })
        )
        return format_html('<a href={} > {} </a>',url,customer.orders_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(orders_count=Count('order'))


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['pk','placed_at','payment_status','customer','customer_id']
    list_select_related = ['customer']
    list_editable = ['payment_status']
    ordering = ['placed_at']
    list_per_page = 10

    @admin.display(ordering='customer_id')
    def customer_id(self,order):
        return order.customer.id