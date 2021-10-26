from rest_framework import generics

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from core.facade.auth import authenticate


from apps.user.serializers import UserSerializer, AuthSerializer
from apps.user.models import User


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


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
