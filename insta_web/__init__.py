from app import app
from helpers.render import render

@app.route("/")
def home():
	return render("index.html")