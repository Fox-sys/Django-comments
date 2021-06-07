import json
from django.contrib.contenttypes.models import ContentType
from channels.db import database_sync_to_async
from .models import Comment
from channels.generic.websocket import AsyncWebsocketConsumer
from django.conf import settings
from django.apps import apps

try:
    POSTS_MODEL = settings.DEFAULT_POSTS_MODEL
    Post = apps.get_model(POSTS_MODEL)
except:
    raise Exception('Variable DEFAULT_POSTS_MODEL isn\'t defiend in setting.py file')


class CommentsConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.post_id = self.scope['url_route']['kwargs']['post_id']
        self.post_group_name = f'post_{self.post_id}'
        await self.channel_layer.group_add(self.post_group_name, self.channel_name)
        print(1)
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.post_group_name, self.channel_layer) 

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        comment = text_data_json['text']
        new_comment = await self.create_new_comment(comment)
        data = {
            'author': new_comment.author.username,
            'published_on': new_comment.published_on.strftime('%Y-%m-%d %H:%M'),
            'text': new_comment.text
        }
        await self.channel_layer.group_send(
            self.post_group_name,
            {
                'type': 'new_comment',
                'message': data
            }
        )

    @database_sync_to_async
    def create_new_comment(self, text):
        ct = ContentType.objects.get_for_model(Post)
        comment =  Comment.objects.create(author=self.scope['user'], text=text, content_type=ct, object_id=self.post_id)
        Post.objects.get(id=self.post_id).comments.add(comment)
        return comment


    async def new_comment(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({'message': message}))