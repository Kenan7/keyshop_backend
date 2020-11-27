from django.db import models


# Create your models here.
class Product(models.Model):
    item_name = models.CharField(max_length=30)
    quantity = models.IntegerField(default=1)
    description = models.CharField(max_length=1000)
    price = models.FloatField()
    discount_price = models.FloatField(null=True, blank=True)
    image = models.ImageField(upload_to="products/")

    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True)
    compability = models.ManyToManyField("Compability")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

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


class Category(models.Model):
    name = models.CharField(max_length=16)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"
