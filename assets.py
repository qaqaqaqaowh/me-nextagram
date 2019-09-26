from flask_assets import Environment, Bundle
from app import app

assets = Environment(app)

assets.register('css_all', Bundle(
	'css/layout.css',
	'css/form.css',
	'css/profile.css',
	'css/home.css',
	filters='cssmin',
	output='gen/home-%(version)s.css'
))

assets.register('js_all', Bundle(
	'js/layout.js',
	filters='jsmin',
	output='gen/home-%(version)s.js'
))