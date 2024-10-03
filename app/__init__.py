from flask import Flask
from .routes import main

app = Flask(__name__)

def create_app():

    with app.app_context():
        app.register_blueprint(main)
    return app