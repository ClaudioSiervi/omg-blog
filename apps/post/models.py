from django.db import models

from core.mixin.model import AbstractModelMixin
from apps.user.models import User


class Post(AbstractModelMixin, models.Model):
    title = models.CharField(max_length=100, blank=True, default="")
    body = models.TextField(blank=True, default="")
    owner = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)


    @property
    def count_likes(self) -> int:
        return self.likes.filter(post=self.pk).count()

    class Meta:
        db_table = "post"
        ordering = ["created_at"]
