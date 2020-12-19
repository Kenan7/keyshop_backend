from django.urls import path
from rest_framework import routers

from product import views

urlpatterns = [
    path("category", views.CategoryListView.as_view()),
    path("product", views.ProductsListView.as_view()),
    path("product/<int:id>/", views.ProductsDetailView.as_view()),
]
