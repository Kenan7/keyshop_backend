from rest_framework.serializers import ModelSerializer, Serializer

from product.models import Product


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


# class singleProduct(Serializer):
#     class Meta:
#         model = Product
#         fields = "__all__"
