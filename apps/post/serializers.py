
from typing import Dict
from rest_framework import serializers

from apps.user.models import User
from apps.post.models import Post


class CreatePostSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = ["id", "title", "body", "owner", "created_at"]

    def to_representation(self, instance: Post) -> Dict:
        serialized_data = super(CreatePostSerializer, self).to_representation(instance)
        serialized_data["owner"] = instance.owner.name
        return serialized_data


class ListPostsSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = ["id", "title", "body", "owner", "created_at"]
    
    def to_representation(self, instance: Post) -> Dict:
        serialized_data = super(ListPostsSerializer, self).to_representation(instance)
        serialized_data["owner"] = instance.owner.name
        return serialized_data


class PostPkSerializer(serializers.Serializer):
    post_id = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())

    
class RetrievePostsSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ["id", "title", "body", "created_at", "likes"]

    def get_likes(self, post: Post) -> int:
        return post.count_likes

    def to_representation(self, instance: Post) -> Dict:
        serialized_data = super(RetrievePostsSerializer, self).to_representation(instance)
        serialized_data["owner"] = self.context["request"].user.name
        return serialized_data


class UpdatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "title", "body", "created_at"]



class DeletePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "title", "body", "created_at"]


class UserPostSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "posts"]