"""
authentication blueprint definition script
"""
from flask import Blueprint, render_template, flash, request, redirect, url_for, session
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        passwd = request.form.get("login_passwd")

        user = User.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password, passwd):
                login_user(user, remember=True)
                session["username"] = current_user.name
                return redirect(url_for("views.dashboard"))
            else:
                flash("Please check your email and password.", category="error")
                return render_template("login.html", user_exist=False)
        return render_template("login.html", user_exist=False)
    return render_template("login.html")


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

        if db.session.query(User).filter_by(name=name).count() < 1:
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
            else:
                return render_template("signup.html", user_already_exist="True")
        return render_template("signup.html", username_exists="True")

    return render_template("signup.html")
