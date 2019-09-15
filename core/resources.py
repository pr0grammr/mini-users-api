from rest_framework import generics, mixins


class RetrieveResource(mixins.RetrieveModelMixin, generics.GenericAPIView):

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class ListResource(mixins.ListModelMixin, generics.GenericAPIView):

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class CreateResource(mixins.CreateModelMixin, generics.GenericAPIView):

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UpdateResource(mixins.UpdateModelMixin, generics.GenericAPIView):

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class DestroyResource(mixins.DestroyModelMixin, generics.GenericAPIView):

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

