from .base_model import BaseModel, pw
from werkzeug.security import generate_password_hash

class User(BaseModel):
	email = pw.CharField(unique=True)
	password = pw.CharField()
	username = pw.CharField(unique=True)

	def validate(self, prev_self):
		if len(self.password) < 8:
			self.errors.append("Password length needs to be at least 8")
		elif not self.id or (prev_self and (not prev_self.password == self.password)):
			self.password = generate_password_hash(self.password)

		import re
		if not re.match(r".+@.+\..+", self.email):
			self.errors.append("Invalid email")