from django.urls import path
from . import views

urlpatterns = [
    # Главная страница
    path('', views.index),
    # Страница сгрупповыми постами
    path('posts/', views.group_posts),
    # Отдельная страница с полным текстом поста
    path('posts/<slug:pk>/', views.posts_detail),
] 