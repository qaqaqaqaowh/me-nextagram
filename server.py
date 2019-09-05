from app import app
import insta_web
import os

if __name__ == "__main__":
	app.run(bind="0.0.0.0", port=os.environ["PORT"])