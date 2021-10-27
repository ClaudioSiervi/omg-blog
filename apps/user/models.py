from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import UserManager
from django.db import models

from core.mixin.model import AbstractModelMixin


class User(AbstractModelMixin, AbstractBaseUser):
    name = models.CharField(verbose_name="User full name", max_length=255)
    email = models.EmailField(verbose_name="Email address", unique=True)
    username = models.CharField("Username", max_length=150,)
    is_staff = models.BooleanField(verbose_name="Is Staff", default=False)
    is_superuser = models.BooleanField("Super user status", default=False)
    is_active = models.BooleanField(verbose_name="Is Active", default=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = UserManager()

    class Meta:
        db_table = "user_user"

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser
