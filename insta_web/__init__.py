from app import app
from helpers.render import render
from models import User
import assets

from .blueprints.users.views import users_blueprint
from .blueprints.sessions.views import sessions_blueprint
from .blueprints.images.views import images_blueprint
from .blueprints.follows.views import follows_blueprint

app.register_blueprint(users_blueprint, url_prefix="/users")
app.register_blueprint(sessions_blueprint, url_prefix="/")
app.register_blueprint(images_blueprint, url_prefix="/images")
app.register_blueprint(follows_blueprint, url_prefix="/follows")

@app.route("/")
def home():
	return render("index.html")