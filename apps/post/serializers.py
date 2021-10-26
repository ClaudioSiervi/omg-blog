from rest_framework import serializers

from apps.user.models import User
from apps.post.models import Post


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="user.id")

    class Meta:
        model = Post
        fields = ["id", "title", "body", "owner"]


class UserPostSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "posts"]