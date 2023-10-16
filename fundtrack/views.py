"""
routes blueprint definition script
"""
from flask import Blueprint, render_template, session
from flask_login import login_required, current_user

views = Blueprint("views", __name__)


@views.route("/")
def home():
    return render_template("home.html")


@views.route("/dashboard")
@login_required
def dashboard():
    session["title"] = "Dashboard"
    return render_template("dashboard.html")


@views.route("/assets")
@login_required
def assets():
    session["title"] = "Assets"
    return render_template("assets.html")


@views.route("/equity_liability")
@login_required
def equity_liability():
    session["title"] = "Equity & Liability"
    return render_template("equity_liability.html")


@views.route("/reports")
@login_required
def reports():
    session["title"] = "Reports"
    return render_template("reports.html")
