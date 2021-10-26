from typing import Tuple

from django.conf import settings
from rest_framework_simplejwt.tokens import RefreshToken

from apps.user.models import User


def authenticate(email: str, password: str) -> Tuple[str, str]:
    user = User.objects.filter(
        email=email, password__isnull=False
    ).first()
    return generate_token(user)


def generate_token(user: User) -> Tuple[str, str]:
    jwt_tokens = RefreshToken.for_user(user)
    access_token = str(jwt_tokens.access_token)
    refresh_token = str(jwt_tokens)

    return access_token, refresh_token
