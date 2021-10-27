
import datetime
from apps.post.serializers import UpdatePostSerializer
from rest_framework.request import Request
from rest_framework.generics import get_object_or_404

from apps.post.models import Post


def update_post(request: Request, post_id: str) -> Post:
    post = get_object_or_404(
        Post.objects.filter(id=post_id)
        )
    serializer = UpdatePostSerializer(
        data=request.data,
        )
    serializer.is_valid(raise_exception=True)
    post.title = serializer.validated_data["title"]
    post.body = serializer.validated_data["body"]
    post.updated_at = datetime.datetime.now()
    post.save()
    return post


def delete_post(post_id: str) -> None:
    post = get_object_or_404(
        Post.objects.filter(id=post_id)
        )
    post.delete()
