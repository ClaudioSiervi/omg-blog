from uuid import uuid4

from django.db import models


class AbstractModelMixin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created_at = models.DateTimeField("Created at", auto_now_add=True)
    updated_at = models.DateTimeField("Updated at", auto_now=True)
    deleted_at = models.DateTimeField("Deleted at", auto_now=True)

    class Meta:
        abstract = True
