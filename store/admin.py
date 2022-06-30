""" Registered models to be shown in admin app"""
from django.contrib import admin
from .models import Order, Product, Bag

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    """ Special view settings for Products in admin """
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)

class OrdersAdmin(admin.ModelAdmin):
    """ Special view settings for Orders in admin """
    list_display = (
        'order_id',
        'user_id',
        'transaction_date',
        'grand_total',
    )

admin.site.register(Order, OrdersAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Bag)
