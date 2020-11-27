from rest_framework import serializers

from contact_form.models import ContactForm


class CreateContactFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactForm
        fields = "__all__"
