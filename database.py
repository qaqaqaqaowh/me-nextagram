from playhouse.db_url import connect
import os

db = connect(os.environ["DATABASE_URL"])