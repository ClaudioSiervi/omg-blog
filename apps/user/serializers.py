from rest_framework import serializers

from apps.user.models import User


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["name", "email", "password"]


class AuthSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
