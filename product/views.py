from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from product.models import Category, Product
from product.serializers import CategorySerializer, ProductSerializer


class ProductsListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # filter_backends = (OrderingFilter,)


class CategoryListView(ListAPIView):
    queryset = Category.objects.get_all()
    serializer_class = CategorySerializer
