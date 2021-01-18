
"""
ASGI config for AderibigbeVictorTest project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter,URLRouter
from channels.http import AsgiHandler
import os
import orders.routing

# from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AderibigbeVictorTest.settings')

application = ProtocolTypeRouter({
    'http':AsgiHandler(),
    "websocket": AuthMiddlewareStack(
            URLRouter(
                orders.routing.websocket_urlpatterns)
    ),

})
