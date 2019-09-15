from django.db import models
from users.models import User, Interest
from core.utils import table_name


class Post(models.Model):
    class Meta:
        db_table = table_name('posts')

    text = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    tags = models.ManyToManyField(Interest)

    def __str__(self):
        return self.text

