from .base_model import BaseModel, pw
from .user import User

class Follow(BaseModel):
	follower = pw.ForeignKeyField(User)
	idol = pw.ForeignKeyField(User)
	approved = pw.BooleanField()