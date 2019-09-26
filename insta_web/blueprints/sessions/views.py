from flask import Blueprint, flash, request, redirect, url_for
from helpers.render import render
from werkzeug.security import check_password_hash
from flask_login import login_user, logout_user, login_required
from models import User

sessions_blueprint = Blueprint("sessions", __name__, template_folder="templates")

@sessions_blueprint.route("/login")
def new():
	return render("sessions/new.html")

@sessions_blueprint.route("/login", methods=["POST"])
def create():
	username = request.form.get("username")
	password = request.form.get("password")
	user = User.get_or_none(User.username == username)
	if user and check_password_hash(user.password, password):
		flash("Welcome!", "success")
		login_user(user)
		return redirect(url_for("home"))
	else:
		flash("Bad login", "danger")
		return render("sessions/new.html", username=username)

@sessions_blueprint.route("/logout", methods=["POST"])
@login_required
def destroy():
	flash("Logged out!", "info")
	logout_user()
	return redirect(url_for("home"))







