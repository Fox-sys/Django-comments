from django.urls import path
from .views import PostDetailView, PostListView

urlpatterns = [
    path('posts/', PostListView.as_view(), name='posts'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail')
]