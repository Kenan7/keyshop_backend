from django.contrib import admin

from product.models import Category, Compability, Product


class ProductAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = (
            super(ProductAdmin, self).get_queryset(request).filter(active=True)
        )
        self.request = request
        return qs


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Compability)
