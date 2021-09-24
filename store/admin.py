from django.contrib import admin
from . import models 

# Register your models here.

@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_per_page = 10


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','unit_price','collection','inventory','inventory_status']
    list_editable = ['unit_price','inventory','collection']
    list_per_page = 10

    @admin.display(ordering='inventory')
    def inventory_status(self,product):
        if product.inventory < 10 :
            return 'Low'
        else:
            return 'Ok'



@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','membership']
    list_editable = ['membership']
    ordering = ['first_name','last_name']
    list_per_page = 10


admin.site.register(models.Order)
