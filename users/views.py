from rest_framework.generics import get_object_or_404
from django.http import Http404
from posts.serializers import PostSerializer
from .models import User
from .serializers import UserSerializer
from core import resources
from rest_framework import permissions
from posts.models import Post


class UsersView(resources.ListResource):
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = UserSerializer
    queryset = User.objects.all()


class RetrieveUpdateDeleteUserView(resources.UpdateResource, resources.RetrieveResource, resources.DestroyResource):
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = UserSerializer
    queryset = User.objects.all()


class RetrieveUserPostsView(resources.ListResource):
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = PostSerializer

    def get_object(self):
        try:
            user = User.objects.get(pk=self.kwargs['pk'])
            return Post.objects.filter(user=user)
        except User.DoesNotExist:
            raise Http404

    def get_queryset(self):
        posts = self.get_object()
        return posts




