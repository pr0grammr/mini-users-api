from .models import Post
from .serializers import PostSerializer
from rest_framework import permissions
from core import resources


class CreatePostView(resources.CreateResource):
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ListUpdateDestroyPostView(resources.UpdateResource, resources.RetrieveResource, resources.DestroyResource):
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = PostSerializer
    queryset = Post.objects.all()
