from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post
from .serializers import PostSerializer
from rest_framework import status
from rest_framework import permissions


class SinglePostView(APIView):
    permission_classes = (permissions.AllowAny, )

    def get(self, request, pk, format=None):
        try:
            post = Post.objects.get(pk=pk)
            serializer = PostSerializer(post)

            return Response(serializer.data, status=status.HTTP_200_OK)
        except Post.DoesNotExist:
            return Response({'message': 'Post does not exist'}, status=status.HTTP_404_NOT_FOUND)

