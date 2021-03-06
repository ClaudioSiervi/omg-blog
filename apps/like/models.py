from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from core.mixin.model import AbstractModelMixin
from apps.user.models import User
from apps.post.models import Post


class Like(AbstractModelMixin, models.Model):
    post = models.ForeignKey(Post, related_name="likes", on_delete=models.CASCADE)
    owner = models.ForeignKey(User, related_name="likes", on_delete=models.CASCADE)

    class Meta:
        db_table = "like"
        ordering = ["created_at"]

