import datetime
from peewee import Model, CharField, DateTimeField
from app.database.database import db


class Client(Model):
    name = CharField()
    email = CharField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db