from flask import Blueprint, render_template, request, redirect, url_for, jsonify, flash
from models import User
from helpers.flash import flash_messages
from helpers.render import render
from flask_login import login_required, current_user
from helpers.upload import upload

users_blueprint = Blueprint('users', __name__, template_folder="templates")

@users_blueprint.route("/new")
def new():
	return render("users/new.html")

@users_blueprint.route("/", methods=["POST"])
def create():
	username = request.form.get("username")
	email = request.form.get("email")
	password = request.form.get("password")
	password_conf = request.form.get("password_conf")
	user = User(username=username, email=email, password=password)
	if user.save():
		flash("Signed up! Please proceed to login.", "success")
		return redirect(url_for("sessions.new"))
	else:
		flash_messages(user.errors, "danger")
		return render("users/new.html", username=username, email=email)

@users_blueprint.route('/<username>')
def show(username):
	user = User.get_or_none(User.username == username)
	if user:
		return render("users/show.html", user=user)
	else:
		return redirect(url_for("home"))

@users_blueprint.route("/<id>/edit")
@login_required
def edit(id):
	user = User.get_or_none(User.id == id)
	if user and current_user == user:
		return render("users/edit.html", user=user)
	else:
		return redirect(url_for("home"))

@users_blueprint.route("/<id>", methods=["POST"])
@login_required
def update(id):
	user = User.get_or_none(User.id == id)
	if user and current_user == user:
		user.username = request.form.get('username')
		user.bio = request.form.get('bio')
		state = request.form.get('private')
		user.is_private = state if state else False
		file = request.files.get('profile')
		if file.filename:
			user.profile_image = upload(file)
		if user.save():
			return redirect(url_for('users.show', username=user.username))
		else:
			flash_messages(user.errors, 'danger')
			return render("users/edit.html", user=user)
	else:
		return redirect(url_for('home'))

@users_blueprint.route("/search")
def search():
	search = request.args["name"]
	users = User.select().where(User.username ** f"%{search}%")
	return jsonify([
		{
			"username": u.username,
			"image": u.image
		} for u in users
	])





