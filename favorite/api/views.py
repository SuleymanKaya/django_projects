from rest_framework.generics import ListCreateAPIView
from favorite.api.paginations import FavoritePagination
from favorite.api.serializers import FavoriteListCreateAPISerializer
from favorite.models import FavoriteModel

class FavoriteListCreateAPIView(ListCreateAPIView):
    serializer_class = FavoriteListCreateAPISerializer
    pagination_class = FavoritePagination

    # Sadece kullanıcıya ait değerleri getiren metod
    def get_queryset(self):
        queryset = FavoriteModel.objects.filter(user = self.request.user)
        return queryset

    # Sadece ilgili kullanıcı adına kayıt alan metod
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        return serializer