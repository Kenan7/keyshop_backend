from django.urls import path
from rest_framework import routers

from order import views

urlpatterns = [
    path("order/create/", views.OrderCreateView.as_view()),
    path("testt/", views.ProductListCreateView.as_view()),
]
