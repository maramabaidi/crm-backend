from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config import Config

# Initialize db object and migrate object
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # Load configuration from config.py
    app.config.from_object(Config)

    # Initialize db and migrate with app
    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints (routes)
    from app.routes import routes
    app.register_blueprint(routes)

    return app
