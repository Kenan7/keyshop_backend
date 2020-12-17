from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from product.models import Category, Product
from product.serializers import CategorySerializer, ProductSerializer


class ProductsListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
