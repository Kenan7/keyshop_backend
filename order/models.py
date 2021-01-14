from django.conf import settings
from django.db import models
from product.models import Product

User = settings.AUTH_USER_MODEL


class Order(models.Model):
    address = models.CharField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.user.email} - {self.address or ''}"


class ProductList(models.Model):
    quantity = models.IntegerField(default=1)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(
        Order,
        related_name="product_list",
        on_delete=models.SET_NULL,
        null=True,
    )

    def __str__(self):
        return f"{self.product.item_name or ''} - ({self.quantity or ''})"
