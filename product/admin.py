from django.contrib import admin

from product.models import Category, Compability, Product

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Compability)
