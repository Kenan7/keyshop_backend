from django.shortcuts import render
from rest_framework.generics import CreateAPIView

from contact_form.serializers import CreateContactFormSerializer


class CreteContactFormView(CreateAPIView):
    serializer_class = CreateContactFormSerializer
