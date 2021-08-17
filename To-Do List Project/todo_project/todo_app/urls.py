from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('create/', views.create, name="create"),
    path('delete/<Todos_id>', views.delete, name="delete"),
    path('yes_finished/<Todos_id>', views.yes_finished, name="yes_finished"),
    path('no_finished/<Todos_id>', views.no_finished, name="no_finished"),
    path('update/<Todos_id>', views.update, name="update"),
]