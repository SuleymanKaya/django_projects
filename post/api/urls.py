from django.urls import path
from post.api.views import PostDetailAPIView, PostListAPIView, PostDeleteAPIView, PostUpdateAPIView

urlpatterns = [
    path('list', PostListAPIView.as_view(), name='list'),
    path('detail/<slug>', PostDetailAPIView.as_view(), name='detail'),
    path('delete/<slug>', PostDeleteAPIView.as_view(), name='delete'),
    path('update/<slug>', PostUpdateAPIView.as_view(), name='update'),
]