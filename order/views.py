from product.models import Product
from rest_framework.generics import CreateAPIView

from order.models import Order, ProductList
from order.serializers import OrderSerializer, ProductListSerializer


class OrderCreateView(CreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    # def post(self, request, *args, **kwargs):
    #     products = request.data["product"]
    # for obj in products:
    #     item = Product.objects.get(obj)
    #     item.quantity


class ProductListCreateView(CreateAPIView):
    serializer_class = ProductListSerializer
    queryset = ProductList.objects.all()
