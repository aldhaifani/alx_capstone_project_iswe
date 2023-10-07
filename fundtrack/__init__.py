"""
webapp init file
"""
from flask import Flask


def create_app():
    # create the app package
    app = Flask(__name__)

    # cookies and session data encryption key
    app.config["SECRET_KEY"] = "hello world"

    # registering blueprints
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    return app
