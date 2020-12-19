from django.db import models
from django.db.models import Manager


class ProductManager(Manager):
    def get_active(self):
        return super(ProductManager, self).get_queryset().filter(active=True)


class Product(models.Model):
    item_name = models.CharField(max_length=30)
    stock_quantity = models.IntegerField(default=1)
    quantity = models.IntegerField(default=1)
    description = models.CharField(max_length=1000)
    price = models.FloatField()
    discount_price = models.FloatField(null=True, blank=True)
    image = models.ImageField(upload_to="products/")

    category = models.ForeignKey(
        "Category", on_delete=models.SET_NULL, null=True
    )
    compability = models.ManyToManyField("Compability")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    active = models.BooleanField()

    objects = ProductManager()

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return f"{self.item_name} - {self.category} - ({self.price})"

    class Meta:
        verbose_name_plural = "Products"


class Compability(models.Model):
    name = models.CharField(max_length=16)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Compabilities"


class CategoryManager(Manager):
    def get_all(self):
        return (
            super(CategoryManager, self)
            .get_queryset()
            .prefetch_related("product_set")
        )


class Category(models.Model):
    name = models.CharField(max_length=16)

    objects = CategoryManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"
