from rest_framework import serializers

from apps.like.models import Like
from apps.post.models import Post
from apps.user.models import User


class CreateLikeSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    owner = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        default=serializers.CurrentUserDefault())
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())

    class Meta:
        model = Like
        fields = ["id", "post", "owner", "created_at"]


class LikePkSerializer(serializers.Serializer):
    like_id = serializers.PrimaryKeyRelatedField(queryset=Like.objects.all())
