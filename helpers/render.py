from flask import render_template

def render(html, *args, **kwargs):
	def inner():
		return render_template(html, *args, **kwargs)
	return render_template("_layout.html", render=inner, *args, **kwargs)