from flask import Blueprint, redirect, url_for, jsonify
from flask_login import login_required, current_user
from models import Follow, User

follows_blueprint = Blueprint('follows', __name__, template_folder='templates')

@follows_blueprint.route("/request/<user_id>", methods=["POST"])
@login_required
def create(user_id):
	user = User[user_id]
	follow = Follow(follower_id=current_user.id, idol_id=user_id, approved=False if user.is_private else True)
	if follow.save():
		return redirect(url_for('users.show', username=user.username))
	else:
		return redirect(url_for('home'))

@follows_blueprint.route("/accept/<user_id>", methods=["POST"])
@login_required
def accept(user_id):
	follow = Follow.get(idol_id=current_user.id, follower_id=user_id)
	follow.approved = True
	follow.save()
	return jsonify({"success": True}), 200

@follows_blueprint.route("/decline/<user_id>", methods=["POST"])
@login_required
def decline(user_id):
	follow = Follow.get(idol_id=current_user.id, follower_id=user_id)
	follow.delete_instance()
	return jsonify({"success": True}), 200

@follows_blueprint.route("/delete/<user_id>", methods=["POST"])
@login_required
def destroy(user_id):
	user = User[user_id]
	follow = Follow.get(follower_id=current_user.id, idol_id=user_id)
	if follow.delete_instance():
		return redirect(url_for('users.show', username=user.username))
	else:
		return redirect(url_for('home'))






