from uuid import UUID

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT
from rest_framework.decorators import api_view, permission_classes

from apps.like.serializer import CreateLikeSerializer, LikePkSerializer



@api_view(["POST"])
@permission_classes([IsAuthenticated])
def like_view(request: Request, pk: UUID = None) -> Response:

    if request.method == "POST":
        # create like related to a post
        serializer = CreateLikeSerializer(
            data=request.data, context={"request": request}
            )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, HTTP_201_CREATED)

    elif request.method == "DELETE":
        from core.facade.like import delete_like
        # delete like
        pk_serializer = LikePkSerializer(data={"like_id": pk})
        pk_serializer.is_valid(raise_exception=True)
        delete_like(post_id=pk_serializer.validated_data["post_id"].pk)
        return Response(None, HTTP_204_NO_CONTENT)
