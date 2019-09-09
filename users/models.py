from django.db import models
from django.contrib.auth.models import AbstractUser
from core.utils import table_name


class User(AbstractUser):
    class Meta:
        db_table = table_name('users')

    username = None
    USERNAME_FIELD = 'email'
    email = models.EmailField(unique=True)

    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
