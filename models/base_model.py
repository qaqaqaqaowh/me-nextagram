import peewee as pw
from database import db
from datetime import datetime

class BaseModel(pw.Model):
	created_at = pw.DateTimeField(default=datetime.now)
	updated_at = pw.DateTimeField(default=datetime.now)

	def save(self, *args, **kwargs):
		self.errors = []
		self.validate(self.__class__.get_or_none(self.__class__.id == self.id))

		if not len(self.errors):
			self.updated_at = datetime.now()
			return super(BaseModel, self).save(*args, **kwargs)

	def validate(self, prev_self):
		pass

	class Meta:
		database = db
		legacy_table_names = False