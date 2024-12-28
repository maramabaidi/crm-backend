from flask import Flask
from app.models import db
from app.config import Config
from app.routes import routes

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    app.register_blueprint(routes)
    return app
