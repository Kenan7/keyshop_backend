from rest_framework import serializers

from contact_form.models import ContactForm


class CreateContactFormSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    email = serializers.EmailField()
    phoneNumber = serializers.CharField()
    message = serializers.CharField()

    class Meta:
        model = ContactForm
        fields = ("name", "email", "phoneNumber", "message")

    def create(self, validated_data):
        return ContactForm.objects.create(**validated_data)
