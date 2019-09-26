from .base_model import BaseModel, pw
from werkzeug.security import generate_password_hash
from flask_login import UserMixin
from playhouse.hybrid import hybrid_property

class User(BaseModel, UserMixin):
	email = pw.CharField(unique=True)
	password = pw.CharField()
	username = pw.CharField(unique=True)
	is_private = pw.BooleanField(default=False)
	bio = pw.CharField(default="")
	profile_image = pw.CharField(null=True)

	@hybrid_property
	def image(self):
		return self.profile_image if self.profile_image else '/static/blank.png'

	@hybrid_property
	def feeds(self):
		from models import Image
		return Image.select().where(Image.id << [i.id for i in (self.images + Image.select().where(Image.user << self.following))]).order_by(Image.created_at.desc()).prefetch(User)

	@hybrid_property
	def following(self):
		from models import Follow
		return User.select().join(Follow, on=(User.id == Follow.idol_id)).where((Follow.follower_id == self.id) & (Follow.approved == True))

	@hybrid_property
	def followers(self):
		from models import Follow
		return User.select().join(Follow, on=(User.id == Follow.follower_id)).where((Follow.idol_id == self.id) & (Follow.approved == True))
	
	@hybrid_property
	def following_requests(self):
		from models import Follow
		return User.select().join(Follow, on=(User.id == Follow.follower_id)).where((Follow.follower_id == self.id) & (Follow.approved == False))

	@hybrid_property
	def follower_requests(self):
		from models import Follow
		return User.select().join(Follow, on=(User.id == Follow.follower_id)).where((Follow.idol_id == self.id) & (Follow.approved == False))

	def validate(self, prev_self):
		if not self.username:
			self.errors.append("Username is required")

		dup_username = User.get_or_none(User.username == self.username)
		if dup_username and not(dup_username == self):
			self.errors.append("Username is not unique")

		dup_email = User.get_or_none(User.email == self.email)
		if dup_email and not(dup_email == self):
			self.errors.append("Email is not unique")

		if len(self.password) < 8:
			self.errors.append("Password length needs to be at least 8")
		elif not self.id or (prev_self and (not prev_self.password == self.password)):
			self.password = generate_password_hash(self.password)

		import re
		if not re.match(r".+@.+\..+", self.email):
			self.errors.append("Invalid email")