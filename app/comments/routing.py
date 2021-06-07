from django.urls import path
from .consumers import CommentsConsumer
from django.conf import Settings, settings

try:
    POSTS_URL = settings.DEFAULT_POSTS_URL
except: 
    raise Exception('Variable DEFAULT_POSTS_URL isn\'t defiend in setting.py file')

websocket_urlpatterns = [
    path('comments/<int:post_id>/', CommentsConsumer.as_asgi(), name='create_comment')
]