from rest_framework.generics import DestroyAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView
from post.models import PostModel
from post.api.serializers import PostSerializer

class PostListAPIView(ListAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer

class PostDetailAPIView(RetrieveAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug' # 'pk' is diğer parametresi, bu parametre ile id'ye göre detay sayfası getirilir.

class PostDeleteAPIView(DestroyAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'

class PostUpdateAPIView(UpdateAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'