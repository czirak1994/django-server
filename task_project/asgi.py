from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from django.urls import path
from . import consumers  # replace with your actual consumers module

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter([
        path("api/tasks/", consumers.TaskConsumer.as_asgi()),
    ]),
})