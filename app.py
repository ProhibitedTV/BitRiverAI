import os
import requests
import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from config import config
from models import db, User  # Import db from models to avoid circular imports

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

login_manager = LoginManager()

def create_app():
    app = Flask(__name__)

    # Load configuration
    env = os.getenv('FLASK_ENV', 'development')
    app.config.from_object(config[env])

    # Initialize extensions with app context
    db.init_app(app)
    Migrate(app, db)  # Directly use app here to prevent redefinition
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    with app.app_context():
        # Automatically create tables if they don't exist (for development purposes)
        db_path = os.path.join(app.instance_path, 'site.db')
        if not os.path.exists(db_path):
            db.create_all()

        @login_manager.user_loader
        def load_user(user_id):
            return db.session.get(User, int(user_id))

    # Register blueprints
    from routes.auth import auth_bp
    from routes.chat import chat_bp
    from routes.main import main_bp
    from routes.imagegen import imagegen_bp  # Import the new blueprint

    app.register_blueprint(auth_bp)
    app.register_blueprint(chat_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(imagegen_bp)  # Register the new blueprint

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
