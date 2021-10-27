from apps.like.serializer import CreateLikeSerializer
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT
from rest_framework.decorators import api_view, permission_classes


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def like_view(request: Request) -> Response:

    if request.method == "POST":
        # create like related to a post
        serializer = CreateLikeSerializer(
            data=request.data, context={"request": request}
            )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, HTTP_201_CREATED)