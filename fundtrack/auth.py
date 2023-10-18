"""
authentication blueprint definition script
"""
from flask import Blueprint, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from .models import User
from . import db

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        passwd = request.form.get("passwd")

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, passwd):
            login_user(user, remember=True)
            session["username"] = current_user.name.split(" ")[0]
            return redirect(url_for("views.dashboard"))
        return render_template("login.html", user_exist="False")
    return render_template("login.html", user_exist="True")


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("views.home"))


@auth.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        passwd = request.form.get("passwd")

        # form validations are already done in javascript
        # creating and adding a new user to the db

        if db.session.query(User).filter_by(email=email).count() < 1:
            new_user = User(
                email=email,
                name=name,
                password=generate_password_hash(passwd, method="scrypt"),
            )
            db.session.add(new_user)
            db.session.commit()

            # redirect the user to the login page
            return redirect(url_for("auth.login"))
        return render_template("signup.html", user_already_exist="True")

    return render_template("signup.html", user_already_exist="False")
