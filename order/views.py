from rest_framework.generics import CreateAPIView

from order.models import Order, ProductList
from order.serializers import OrderSerializer, ProductListSerializer


class OrderCreateView(CreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class ProductListCreateView(CreateAPIView):
    serializer_class = ProductListSerializer
    queryset = ProductList.objects.all()
