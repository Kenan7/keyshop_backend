from product.models import Product
from product.serializers import ProductSerializer
from rest_framework.serializers import ModelSerializer, Serializer

from order.models import Order, ProductList


class ProductListSerializer(ModelSerializer):
    class Meta:
        model = ProductList
        fields = "__all__"


class OrderSerializer(ModelSerializer):
    product_list = ProductListSerializer(many=True)

    def create(self, validated_data):
        items = validated_data.pop("product_list")
        for x in items:
            ProductList.objects.create(product=x.product, quantity=x.quantity)

    class Meta:
        model = Order
        fields = "__all__"
