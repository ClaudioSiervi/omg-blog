from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_200_OK
from rest_framework import generics

from apps.post.serializers import PostSerializer
from apps.post.models import Post


class PostList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer



from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def post_view(request: Request) -> Response:
    posts = list(Post.objects.all())
    serializer = PostSerializer(posts)
    # serializer.is_valid(raise_exception=True)
    return Response(serializer.data, HTTP_200_OK)