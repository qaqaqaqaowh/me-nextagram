from app import app
import insta_web
import os

if __name__ == "__main__":
	app.run(port=os.environ["PORT"])