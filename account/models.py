from django.db import models

from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.validators import UnicodeUsernameValidator

from .manager import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        max_length = 150,
        validators = [UnicodeUsernameValidator],
        unique = True
    )
    email = models.EmailField(
        max_length = 150,
        unique=True
    )
    date_joined = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    class Meta:
        ordering = ["-date_joined"]

