from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

# Instantiate extensions
db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()

def create_app():
    app = Flask(__name__)

    # Configurations
    app.config.from_object('config.Config')

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Initialize Marshmallow with the SQLAlchemy instance
    ma.init_app(app)

    # Register routes
    from .routes import api_bp
    app.register_blueprint(api_bp, url_prefix='/')

    return app
