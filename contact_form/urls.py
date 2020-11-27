from django.urls import path

from contact_form import views

urlpatterns = [path("create/", views.CreteContactFormView.as_view())]
