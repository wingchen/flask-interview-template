import datetime
import logging
import uuid

from peewee import *
from playhouse.sqlite_ext import SqliteExtDatabase

logger = logging.getLogger()
database = SqliteExtDatabase('coding-exercise.db')

class BaseModel(Model):
    class Meta:
        database = database

class User(BaseModel):
    uuid = UUIDField(primary_key=True)
    username = CharField(unique=True, index=True)
    password = CharField()
    creation = DateTimeField(default=datetime.datetime.utcnow)
    last_login = DateTimeField(null=True)

    def to_json(self):
        return {
            'uuid': str(self.uuid),
            'username': self.username,
            'creation': self.creation,
            'last_login': self.last_login
        }

    @staticmethod
    def getUserWithUsername(username):
        try:
            user = User.get(User.username == username)
        except User.UserDoesNotExist:
            user = None

        return user

TABLE_LIST = [User]

def init_db():
    database.create_tables(TABLE_LIST)

    # initialized develop database
    develop = User()
    develop.uuid = uuid.uuid1()
    develop.username = 'develop'
    develop.password = 'of_course_you_cannot_just_store_password_in_plain_text'
    develop.save(force_insert=True)

def drop_db():
    for table in TABLE_LIST:
        print('dropping table: {}'.format(table))
        database.drop_table(table, fail_silently=True)
