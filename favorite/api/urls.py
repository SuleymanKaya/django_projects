from django.urls import path
from favorite.api.views import FavoriteListCreateAPIView, FavoriteAPIView

app_name = 'favorite'

urlpatterns = [
    path('list_create', FavoriteListCreateAPIView.as_view(), name='list_create'),
    path('edit/<pk>', FavoriteAPIView.as_view(), name='edit'),
]