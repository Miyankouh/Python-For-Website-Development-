from datetime import datetime
from peewee import SqliteDatabase, Model, CharField, TextField,\
    DateTimeField, BooleanField, ForeignKeyField


database = SqliteDatabase("Posts.db")


class BaseModel(Model):
    created_time = DateTimeField(default=datetime.now())

    class Meta:
        database = database


class Category(BaseModel):
    name = CharField()


class Article(BaseModel):
    url = CharField()

    title = CharField(null=True)
    body = TextField(null=True)
    is_completed = BooleanField(default=False)

    category = ForeignKeyField(Category, backref='articles')
