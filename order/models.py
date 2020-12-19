from django.conf import settings
from django.db import models
from product.models import Product

User = settings.AUTH_USER_MODEL


class ProductList(models.Model):
    quantity = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)


class Order(models.Model):
    address = models.CharField(max_length=1000)

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product_list = models.ForeignKey(
        ProductList, on_delete=models.SET_NULL, null=True
    )
