from playhouse.postgres_ext import *
import os

db = PostgresqlExtDatabase(os.environ["DATABASE_URL"].split("/")[-1], user='postgres')