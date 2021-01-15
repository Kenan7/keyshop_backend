from django.contrib import admin

from order.models import Order, ProductList


class ProductListInline(admin.TabularInline):
    model = ProductList


class OrderAdmin(admin.ModelAdmin):
    inlines = [
        ProductListInline,
    ]


admin.site.register(Order, OrderAdmin)
admin.site.register(ProductList)
