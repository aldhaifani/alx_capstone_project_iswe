"""Database models script
"""
from . import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    """User model

    Args:
        db (database model): the database model
        UserMixin: flask login helper
    """

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(256))
    name = db.Column(db.String(150))
    assets = db.relationship("Asset")
    liabilities = db.relationship("Liability")
    equities = db.relationship("Equity")


class Asset(db.Model):
    """Asset model that represents the assets,

    Args:
        db (database model): the database model
    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), unique=True)
    value = db.Column(db.Integer)
    current = True
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))


class Liability(db.Model):
    """Liability model that represents the liabilities,

    Args:
        db (database model): the database model
    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), unique=True)
    value = db.Column(db.Integer)
    current = True
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))


class Equity(db.Model):
    """Equity model that represents the equities,

    Args:
        db (database model): the database model
    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), unique=True)
    value = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
