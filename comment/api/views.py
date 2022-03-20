from urllib import request
from rest_framework.generics import (CreateAPIView, ListAPIView, DestroyAPIView, UpdateAPIView, 
                                    RetrieveAPIView)
from rest_framework.mixins import (UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin,
                                    ListModelMixin)
from comment.api.serializers import CommentCreateSerializer, CommentListSerializer, CommentDeleteUpdateSerializer
from comment.models import CommentModel
from comment.api.permissions import IsOwner
from comment.api.paginations import CommentPagination

class CommentCreateAPIView(CreateAPIView, ListModelMixin):
    queryset = CommentModel.objects.all()
    serializer_class = CommentCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        return serializer
        
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

# Nested serializers'ın içinde Mixin'ler kullanılamaz.
class CommentListAPIView(ListAPIView):
    serializer_class = CommentListSerializer
    pagination_class = CommentPagination

    def get_queryset(self):
        queryset = CommentModel.objects.filter(parent=None)
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(post=query)
        return queryset

class CommentDeleteAPIView(DestroyAPIView, UpdateModelMixin, RetrieveModelMixin):
    queryset = CommentModel.objects.all()
    serializer_class = CommentDeleteUpdateSerializer
    lookup_field = 'pk'
    permission_classes = [IsOwner]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

class CommentUpdateAPIView(UpdateAPIView, RetrieveAPIView, DestroyModelMixin):
    queryset = CommentModel.objects.all()
    serializer_class = CommentDeleteUpdateSerializer
    lookup_field = 'pk'
    permission_classes = [IsOwner]

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

