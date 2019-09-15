from rest_framework import serializers
from .models import Post
from users.serializers import InterestSerializer as TagSerializer


class PostSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(slug_field='value', many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'text', 'created_at', 'tags']
