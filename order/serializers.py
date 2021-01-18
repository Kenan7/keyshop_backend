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
    # FK - Foreign Key
    # {
    # "product_list": [ // array of products
    #     {
    #         "product": 1 // FK(Product),
    #         "quantity": 4 // how many should an item be ordered
    #     }
    # ],
    # "user": 1 // FK(User),
    # "address": // String
    # }

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
