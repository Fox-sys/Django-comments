# This project is developeding with python 3.9.5, Django, Docker, PostgreSQL, Redis, Django-Channels
How to install an example?
1) git clone https://github.com/Fox-sys/Django-comments.git
2) cd django-comments
3) sudo docker-compose up --build
4) python3 -m venv env 
5) source env/bin/activate (for linux) env/scripts/activate (for windows)
6) cd app 
7) pip install -r req.txt
8) python manage.py migrate
9) python manage.py createsuperuser
10) python manage.py runsever ip:port (optional)

How to integrate?
1) get dir channels from django-comments/app
2) move it into your project
3) add into installed apps 
4) in settings.py:

```REDIS_HOST = environ.get('REDIS_HOST', '127.0.0.1')```
```REDIS_PORT = environ.get('REDIS_PORT', '6379')```
```ASGI_APPLICATION = "project name.asgi.application"```
```CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [(f"{REDIS_HOST}", int(REDIS_PORT))],
        },
    },
}
```
```DEFAULT_POSTS_URL = 'your url'```
```DEFAULT_POSTS_MODEL = 'your model (service.model name)'```
5) in asgi.py:
```import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from comments.routing import websocket_urlpatterns
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project name.settings')
application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})```

6) In default post model should be many to many field for comments.Comment
7) Also you should have redis server (if u don't have use docker-compose.yml from example. Starting with "sudo docker-compose up --build")


# Patch Note:
Version: 1.0.0 

- all is working except of docker -_- 