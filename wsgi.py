from asgiref.wsgi import WsgiToAsgi
from main import app as fastapi_app

# Wrap the ASGI application (FastAPI) in WSGI adapter
application = WsgiToAsgi(fastapi_app)