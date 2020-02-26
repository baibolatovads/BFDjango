from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


# Create your models here.

class MyUserManager(UserManager):
    def create_editor(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_editor', True)
        return self._create_user(username, email, password, **extra_fields)

class MyUser(AbstractUser):
    is_editor = models.BooleanField(default=False)
    objects = MyUserManager()