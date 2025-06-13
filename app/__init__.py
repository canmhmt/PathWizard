from flask import Flask
from app.routes import routes
import time

def create_service():
    app = Flask("__init__")
    routes(app)
    return app
