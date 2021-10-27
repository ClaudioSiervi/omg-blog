from apps.post.models import Post
from apps.user.models import User
from django.db.models import fields
from rest_framework import serializers

from apps.like.models import Like


class CreateLikeSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    owner = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        default=serializers.CurrentUserDefault())
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())
    rating = serializers.IntegerField(min_value=1, max_value=5)

    class Meta:
        model = Like
        fields = ["id", "post", "owner", "rating", "created_at"]
