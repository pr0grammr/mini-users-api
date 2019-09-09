from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from django.http import Http404
from rest_framework import status
from .serializers import UserSerializer


class UserListView(APIView):
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserDetailView(APIView):
    def get(self, request, pk, format=None):

        try:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({
                'message': 'User with ID {} was not found'.format(pk)
            }, status=status.HTTP_404_NOT_FOUND)

