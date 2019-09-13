from django.db import models
from users.models import User


class Post(models.Model):
    text = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

