"""
webapp init file
"""
from os import path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


# the data base for users auth
db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    """main app creation

    Returns:
        flask app
    """
    # create the app package
    app = Flask(__name__)

    # setting the database
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"

    # initializing the db
    db.init_app(app)

    # cookies and session data encryption key
    app.config["SECRET_KEY"] = "hello world"

    # registering blueprints
    from .views import views
    from .auth import auth

    # assert that a db exists
    from .models import User

    create_database(app)

    # Login manager
    login_manager = LoginManager()
    login_manager.login_view = "views.home"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    # app blue print registration
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    return app


def create_database(app):
    """Creates the db if it doesn't exist already

    Args:
        app: flask app
    """
    if not path.exists("fundtrack/" + DB_NAME):
        with app.app_context():
            db.create_all()
