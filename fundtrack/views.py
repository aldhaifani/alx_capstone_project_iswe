"""
routes blueprint definition script
"""
import json
from flask import (
    Blueprint,
    render_template,
    session,
    request,
    redirect,
    url_for,
    jsonify,
)
from flask_login import login_required, current_user
from .models import Asset, Equity, Liability
from . import db

views = Blueprint("views", __name__)


@views.route("/")
@views.route("/home")
@views.route("/home/")
def home():
    """Home route

    Returns:
        renter_template
    """
    return render_template("home.html")


@views.route("/dashboard")
@views.route("/dashboard/")
@login_required
def dashboard():
    """Dashboard route

    Returns:
        renter_template
    """
    session["title"] = "Dashboard"
    return render_template("dashboard.html", user=current_user)


@views.route("/assets")
@views.route("/assets/")
@login_required
def assets():
    """Assets route

    Returns:
        _type_: _description_
    """
    session["title"] = "Assets"
    return render_template("assets.html", user=current_user)


@views.route("/assets/add", methods=["GET", "POST"])
@views.route("/assets/add/", methods=["GET", "POST"])
@login_required
def form_add_assets():
    """Assets add form route

    Returns:
        renter_template or redirect
    """
    session["title"] = "Add assets"

    if request.method == "POST":
        name = request.form.get("name")
        value = int(request.form.get("value"))
        asset_type = (
            True
            if request.form.get("asset_type") == "current"
            else False
        )

        new_asset = Asset(
            name=name, value=value, current=asset_type, user_id=current_user.id
        )
        db.session.add(new_asset)
        db.session.commit()

        return redirect(url_for("views.assets"))

    return render_template("form_assets.html", user=current_user)


@views.route("/assets/edit/<string:id>", methods=["GET", "POST"])
@views.route("/assets/edit/<string:id>/", methods=["GET", "POST"])
@login_required
def form_edit_assets(id):
    """Assets edit form route

    Returns:
        renter_template or redirect
    """
    session["title"] = "Edit assets"

    asset = Asset.query.get(id)

    if request.method == "POST":
        asset.name = request.form.get("name")
        asset.value = int(request.form.get("value"))
        asset.current = (
            True
            if request.form.get("asset_type") == "current"
            else False
        )

        db.session.commit()

        if asset.id == 1:
            session["cash"] = asset.value

        return redirect(url_for("views.assets"))

    return render_template("form_edit_assets.html", asset=asset)


@views.route("/delete-asset", methods=["POST"])
@views.route("/delete-asset/", methods=["POST"])
@login_required
def delete_asset():
    """Delete asset

    Returns:
        json string
    """
    asset = json.loads(request.data)
    asset_id = asset["assetId"]

    asset = Asset.query.get(asset_id)
    if asset:
        if asset.user_id == current_user.id:
            db.session.delete(asset)
            db.session.commit()
    return jsonify({})


@views.route("/equity_liability")
@views.route("/equity_liability/")
@login_required
def equity_liability():
    """equity_liability add form route

    Returns:
        renter_template
    """
    session["title"] = "Equity & Liability"
    return render_template("equity_liability.html", user=current_user)


@views.route("/equity_liability/add_equity", methods=["GET", "POST"])
@views.route("/equity_liability/add_equity/", methods=["GET", "POST"])
@login_required
def form_equity():
    """Equity add form route

    Returns:
        renter_template or redirect
    """
    session["title"] = "Add Equity"

    if request.method == "POST":
        name = request.form.get("name")
        value = int(request.form.get("value"))

        new_equity = Equity(name=name, value=value, user_id=current_user.id)
        db.session.add(new_equity)
        db.session.commit()

        return redirect(url_for("views.equity_liability"))

    return render_template("form_equity.html", user=current_user)


@views.route(
    "/equity_liability/edit_equity/<string:id>",
    methods=["GET", "POST"]
)
@views.route(
    "/equity_liability/edit_equity/<string:id>/",
    methods=["GET", "POST"]
)
@login_required
def form_edit_equity(id):
    """Equity edit form route

    Returns:
        renter_template or redirect
    """
    session["title"] = "Edit equity"

    equity = Equity.query.get(id)

    if request.method == "POST":
        equity.name = request.form.get("name")
        equity.value = int(request.form.get("value"))

        db.session.commit()

        return redirect(url_for("views.equity_liability"))

    return render_template("form_edit_equity.html", equity=equity)


@views.route("/delete-equity", methods=["POST"])
@views.route("/delete-equity/", methods=["POST"])
@login_required
def delete_equity():
    """Delete Equity

    Returns:
    json string
    """
    equity = json.loads(request.data)
    equity_id = equity["equityId"]

    equity = Equity.query.get(equity_id)
    if equity:
        if equity.user_id == current_user.id:
            db.session.delete(equity)
            db.session.commit()
    return jsonify({})


@views.route("/equity_liability/add_liability", methods=["GET", "POST"])
@views.route("/equity_liability/add_liability/", methods=["GET", "POST"])
@login_required
def form_liability():
    """Liability add form route

    Returns:
        renter_template or redirect
    """
    session["title"] = "Add Liability"

    if request.method == "POST":
        name = request.form.get("name")
        value = int(request.form.get("value"))
        liability_type = (
            True if request.form.get("liability_type") == "current" else False
        )

        new_liability = Liability(
            name=name,
            value=value,
            current=liability_type,
            user_id=current_user.id
        )
        db.session.add(new_liability)
        db.session.commit()
        return redirect(url_for("views.equity_liability"))

    return render_template("form_liability.html", user=current_user)


@views.route(
    "/equity_liability/edit_liability/<string:id>",
    methods=["GET", "POST"]
)
@views.route(
    "/equity_liability/edit_liability/<string:id>/",
    methods=["GET", "POST"]
)
@login_required
def form_edit_liability(id):
    """Liability edit form route

    Returns:
        renter_template or redirect
    """
    session["title"] = "Edit liability"

    liability = Liability.query.get(id)

    if request.method == "POST":
        liability.name = request.form.get("name")
        liability.value = int(request.form.get("value"))
        liability.current = (
            True if request.form.get("asset_type") == "current" else False
        )

        db.session.commit()

        return redirect(url_for("views.equity_liability"))

    return render_template("form_edit_liability.html", liability=liability)


@views.route("/delete-liability", methods=["POST"])
@views.route("/delete-liability/", methods=["POST"])
@login_required
def delete_liability():
    """Delete laibility

    Returns:
        json string
    """
    liability = json.loads(request.data)
    liability_id = liability["liabilityId"]

    liability = Liability.query.get(liability_id)
    if liability:
        if liability.user_id == current_user.id:
            db.session.delete(liability)
            db.session.commit()
    return jsonify({})


@views.route("/reports")
@views.route("/reports/")
@login_required
def reports():
    """reports add form route

    Returns:
        renter_template
    """
    session["title"] = "Reports"
    return render_template("reports.html", user=current_user)
