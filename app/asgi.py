from asgiref.wsgi import WsgiToAsgi
from . import app

asgi_app = WsgiToAsgi(app)

