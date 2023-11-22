from django.contrib import admin

from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'caption']
admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'razmer', 'image']
admin.site.register(Product, ProductAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'display_products', 'created_at', 'status']

    def display_products(self, obj):
        return ", ".join([f"{item.product.name} x {item.quantity}" for item in obj.orderitem_set.all()])

    display_products.short_description = 'Maxsulotlar'
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)