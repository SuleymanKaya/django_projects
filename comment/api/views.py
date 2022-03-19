from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView, UpdateAPIView
from comment.api.serializers import CommentCreateSerializer, CommentListSerializer, CommentDeleteUpdateSerializer
from comment.models import CommentModel
from comment.api.permissions import IsOwner
from comment.api.paginations import CommentPagination

class CommentCreateAPIView(CreateAPIView):
    queryset = CommentModel.objects.all()
    serializer_class = CommentCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        return serializer

class CommentListAPIView(ListAPIView):
    serializer_class = CommentListSerializer
    pagination_class = CommentPagination
    def get_queryset(self):
        queryset = CommentModel.objects.filter(parent=None)
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(post=query)
        return queryset

class CommentDeleteAPIView(DestroyAPIView):
    queryset = CommentModel.objects.all()
    serializer_class = CommentDeleteUpdateSerializer
    lookup_field = 'pk'
    permission_classes = [IsOwner]

class CommentUpdateAPIView(UpdateAPIView):
    queryset = CommentModel.objects.all()
    serializer_class = CommentDeleteUpdateSerializer
    lookup_field = 'pk'
    permission_classes = [IsOwner]