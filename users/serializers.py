from rest_framework import serializers
from .models import User, Interest


class InterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interest
        fields = ['value']


class UserSerializer(serializers.ModelSerializer):
    interests = serializers.SlugRelatedField(slug_field='value', read_only=True, many=True)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'interests']
