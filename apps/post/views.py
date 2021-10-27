from uuid import UUID

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import get_object_or_404

from apps.post.serializers import (
    CreatePostSerializer,
    ListPostsSerializer,
    PostPkSerializer,
    RetrievePostsSerializer,
    UpdatePostSerializer,
)
from apps.post.models import Post

from core.facade.post import delete_post, update_post


@api_view(["POST", "GET", "PUT", "DELETE"])
@permission_classes([IsAuthenticated])
def post_view(request: Request, pk: UUID = None) -> Response:

    if request.method == "POST":
        # create post
        serializer = CreatePostSerializer(
            data=request.data, context={"request": request}
            )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, HTTP_201_CREATED)

    if request.method == "GET" and pk:
        # retrieve post
        pk_serializer = PostPkSerializer(data={"post_id": pk})
        pk_serializer.is_valid(raise_exception=True)
        
        post = get_object_or_404(
            Post.objects.filter(id=pk_serializer.validated_data["post_id"].pk)
            )
        serializer = RetrievePostsSerializer(
            post, context={"request": request}
            )
        return Response(serializer.data, HTTP_200_OK)

    if request.method == "GET" and not pk:
        # list posts
        serializer = ListPostsSerializer(
            Post.objects.all(), many=True
            )
        return Response(serializer.data, HTTP_200_OK)
    
    if request.method == "PUT" and pk:
        # update post
        pk_serializer = PostPkSerializer(data={"post_id": pk})
        pk_serializer.is_valid(raise_exception=True)
        post = update_post(
            request=request, post_id=pk_serializer.validated_data["post_id"].pk
            )
        return Response(UpdatePostSerializer(post).data, HTTP_200_OK)

    if request.method == "DELETE":
        # delete post
        pk_serializer = PostPkSerializer(data={"post_id": pk})
        pk_serializer.is_valid(raise_exception=True)
        delete_post(post_id=pk_serializer.validated_data["post_id"].pk)
        return Response(None, HTTP_204_NO_CONTENT)
