from .base_model import BaseModel, pw
from models import User

class Image(BaseModel):
	url = pw.CharField()
	user = pw.ForeignKeyField(User, backref="images")