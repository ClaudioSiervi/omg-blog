from django.contrib.auth.models import AbstractBaseUser
from django.db import models

from core.mixin.model import AbstractModelMixin


class User(AbstractModelMixin, AbstractBaseUser):
    name = models.CharField(verbose_name="User full name", max_length=255)
    email = models.EmailField(verbose_name="Email address", unique=True)

    is_staff = models.BooleanField(verbose_name="Is Staff", default=False)
    is_active = models.BooleanField(verbose_name="Is Active", default=True)

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
