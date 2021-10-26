from rest_framework import serializers

from apps.user.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]


class AuthSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
