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

    def get_total_current_assets(self):
        """calculates the total value of the current assets

        Returns:
            int: the total value of the current assets
        """
        total = 0
        for asset in self.assets:
            if asset.current:
                total += asset.value
        return total

    def get_total_non_current_assets(self):
        """calculates the total value of the non-current assets

        Returns:
            int: the total value of the non-current assets
        """
        total = 0
        for asset in self.assets:
            if not asset.current:
                total += asset.value
        return total

    def get_total_current_liability(self):
        """calculates the total value of the current liabilities

        Returns:
            int: the total value of the current liabilities
        """
        total = 0
        for liability in self.liabilities:
            if liability.current:
                total += liability.value
        return total

    def get_total_non_current_liability(self):
        """calculates the total value of the non-current liabilities

        Returns:
            int: the total value of the non-current liabilities
        """
        total = 0
        for liability in self.liabilities:
            if not liability.current:
                total += liability.value
        return total

    def get_total_equity(self):
        """calculates the total value of the equities

        Returns:
            int: the total value of the equities
        """
        total = 0
        for equity in self.equities:
            total += equity.value
        return total


class Asset(db.Model):
    """Asset model that represents the assets,

    Args:
        db (database model): the database model
    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(512))
    value = db.Column(db.Integer)
    current = db.Column(db.Boolean, default=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))


class Liability(db.Model):
    """Liability model that represents the liabilities,

    Args:
        db (database model): the database model
    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    value = db.Column(db.Integer)
    current = db.Column(db.Boolean, default=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))


class Equity(db.Model):
    """Equity model that represents the equities,

    Args:
        db (database model): the database model
    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    value = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
