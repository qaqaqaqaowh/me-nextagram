from flask import Blueprint, request, redirect, url_for
from flask_login import login_required, current_user
from helpers.upload import upload
from models import Image

images_blueprint = Blueprint('images', __name__)

@images_blueprint.route("/", methods=["POST"])
@login_required
def create():
	file = request.files.get("image")
	if file.filename:
		url = upload(file)
		image = Image(url=url, user_id=current_user.id)
		image.save()
	return redirect(url_for('users.show', username=current_user.username))