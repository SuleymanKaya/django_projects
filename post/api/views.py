from rest_framework.generics import (DestroyAPIView, 
                                    ListAPIView, 
                                    RetrieveAPIView, 
                                    RetrieveUpdateAPIView, 
                                    CreateAPIView)
from rest_framework.permissions import (IsAuthenticated)
from rest_framework.filters import SearchFilter, OrderingFilter
from post.api.permissions import IsOwner
from post.models import PostModel
from post.api.serializers import PostSerializer, PostUpdateCreateSerializer

class PostListAPIView(ListAPIView):
    serializer_class = PostSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'content']

    def get_queryset(self):
        queryset = PostModel.objects.filter(draft=False)
        return queryset

class PostDetailAPIView(RetrieveAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug' # 'pk' is diğer parametresi, bu parametre ile id'ye göre detay sayfası getirilir.

class PostDeleteAPIView(DestroyAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'
    permission_classes = [IsOwner]

class PostUpdateAPIView(RetrieveUpdateAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostUpdateCreateSerializer
    lookup_field = 'slug'
    permission_classes = [IsOwner]

    def perform_update(self, serializer):
        serializer.save(modified_by=self.request.user)

class PostCreateAPIView(CreateAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostUpdateCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)