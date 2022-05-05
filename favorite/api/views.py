from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from favorite.api.paginations import FavoritePagination
from favorite.api.permissions import IsOwner
from favorite.api.serializers import FavoriteListCreateAPISerializer, FavoriteAPISerializer
from favorite.models import FavoriteModel

class FavoriteListCreateAPIView(ListCreateAPIView):
    serializer_class = FavoriteListCreateAPISerializer
    pagination_class = FavoritePagination
    permission_classes = [IsAuthenticated]

    # Sadece kullanıcıya ait değerleri getiren metod
    def get_queryset(self):
        queryset = FavoriteModel.objects.filter(user = self.request.user)
        return queryset

    # Sadece ilgili kullanıcı adına kayıt alan metod
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        return serializer

# RetrieveUpdateAPIView
# RetrieveDestroyAPIView
class FavoriteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = FavoriteModel.objects.all()
    serializer_class = FavoriteAPISerializer
    pagination_class = FavoritePagination
    lookup_field = 'pk'
    permission_classes = [IsOwner]