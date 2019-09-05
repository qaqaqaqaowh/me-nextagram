from flask import render_template

def render(html):
	def inner():
		return render_template(html)
	return render_template("_layout.html", render=inner)