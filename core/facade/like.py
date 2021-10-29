
from rest_framework.generics import get_object_or_404

from apps.like.models import Like


def delete_like(like_id: str) -> None:
    like = get_object_or_404(
        Like.objects.filter(id=like_id)
        )
    like.delete()
