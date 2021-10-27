from rest_framework import generics

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT
from rest_framework.decorators import api_view, permission_classes


from core.facade.auth import authenticate


from apps.user.serializers import CreateUserSerializer, AuthSerializer



@api_view(["POST"])
@permission_classes([AllowAny])
def authentication_view(request: Request) -> Response:
    serializer = AuthSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    token, refresh = authenticate(**serializer.validated_data)
    return Response(
        {"access": token, "refresh": refresh},
        status=HTTP_200_OK,
    )


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def user_view(request: Request) -> Response:

    if request.method == "POST":
        # create user
        serializer = CreateUserSerializer(
            data=request.data,
            )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, HTTP_201_CREATED)