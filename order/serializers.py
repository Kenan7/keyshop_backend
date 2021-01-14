from product.models import Product
from product.serializers import ProductSerializer
from rest_framework.serializers import ModelSerializer, Serializer

from order.models import Order, ProductList


class ProductListSerializer(ModelSerializer):
    class Meta:
        model = ProductList
        fields = [
            "quantity",
            "product",
        ]


class OrderSerializer(ModelSerializer):
    product_list = ProductListSerializer(many=True)

    def create(self, validated_data):
        items = validated_data.pop("product_list")
        order = Order.objects.create(**validated_data)
        for item in items:
            ProductList.objects.create(order=order, **item)

        return order

    class Meta:
        model = Order
        fields = [
            "user",
            "address",
            "product_list",
        ]
