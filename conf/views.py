from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        ## This data variable will contain refresh and access tokens
        data = super().validate(attrs)
        ## You can add more User model's attributes like username,email etc. in the data dictionary like this.
        # data["name"] = f"{self.user.first_name} {self.user.last_name}"
        return data


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
