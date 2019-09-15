from rest_framework import serializers
from .models import Post
from users.serializers import InterestSerializer as TagSerializer


class PostSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(slug_field='value', many=True, read_only=True)
    owner = serializers.ReadOnlyField(source='owner.id')

    class Meta:
        model = Post
        fields = ['text', 'created_at', 'tags', 'owner']
