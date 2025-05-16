from flask import Flask
from .core.extensions import db, migrate
from .routes.auth_routes import auth_bp
from .core.config import load_config

def create_app():
    app = Flask(__name__)
    load_config(app)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(auth_bp, url_prefix="/auth")

    return app
