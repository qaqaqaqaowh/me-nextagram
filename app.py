from flask import Flask
import os
from database import db
from flask_login import LoginManager

import peeweedbevolve
from models import *

app = Flask(__name__)

app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY") or os.urandom(32)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.get_or_none(User.id == user_id)

@app.cli.command()
def migrate():
	db.evolve(interactive=True if os.environ["FLASK_ENV"] == "development" else False, ignore_tables=["base_model"])