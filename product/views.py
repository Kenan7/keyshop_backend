from django.shortcuts import render
from rest_framework import generics, mixins, permissions, views, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from product.models import Product
from product.serializers import ProductSerializer

# class ProductList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     permission_classes = [permissions.AllowAny]

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# @api_view(["GET", "POST"])
# def products_list(request):
#     if request.method == "GET":
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data)
