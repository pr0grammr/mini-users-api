from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager as BaseUserManager
from core.utils import table_name


class UserManager(BaseUserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        user = super().create_user(username=username, email=email, password=password, **extra_fields)
        return user


class Interest(models.Model):
    class Meta:
        db_table = table_name('user_interests')

    name = models.CharField(max_length=255, null=False)
    value = models.CharField(max_length=255, null=False)


class User(AbstractUser):
    class Meta:
        db_table = table_name('users')

    email = models.EmailField(unique=True)
    interests = models.ManyToManyField(Interest)

    objects = UserManager()

    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

