from django.urls import path
from favorite.api.views import FavoriteListCreateAPIView

app_name = 'favorite'

urlpatterns = [
    path('list_create', FavoriteListCreateAPIView.as_view(), name='list_create'),
]