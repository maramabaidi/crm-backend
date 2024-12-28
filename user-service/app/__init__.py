from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config

# Initialize db object
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Load configuration from config.py
    app.config.from_object(Config)

    # Initialize db with app
    db.init_app(app)

    # Register blueprints (routes)
    from app.routes import routes
    app.register_blueprint(routes)

    return app
