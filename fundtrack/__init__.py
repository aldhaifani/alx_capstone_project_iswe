"""
webapp init file
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager


# the data base for users auth
db = SQLAlchemy()
DB_name = "database.db"


def create_app():
    # create the app package
    app = Flask(__name__)

    # setting the database
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///{}".format(DB_name)

    # initializing the db
    db.init_app(app)

    # cookies and session data encryption key
    app.config["SECRET_KEY"] = "hello world"

    # registering blueprints
    from .views import views
    from .auth import auth

    # assert that a db exists
    from .models import User, Asset, Liability, Equity

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
    if not path.exists("fundtrack/" + DB_name):
        with app.app_context():
            db.create_all()
        print("Database created")
