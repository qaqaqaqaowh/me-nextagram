from flask import Flask
import os
from database import db
import peeweedbevolve
from models import *

app = Flask(__name__)

@app.cli.command()
def migrate():
	db.evolve(interactive=True if os.environ["FLASK_ENV"] == "development" else False, ignore_tables=["base_model"])