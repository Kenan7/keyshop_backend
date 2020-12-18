from rest_framework.serializers import ModelSerializer, Serializer

from product.models import Category, Product


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class CategorySerializer(ModelSerializer):
    products = ProductSerializer(
        many=True, read_only=True, source="product_set"
    )

    class Meta:
        model = Category
        fields = ["id", "name", "products"]


class CategoryOnlySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]
