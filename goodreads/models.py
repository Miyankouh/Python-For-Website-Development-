from datetime import datetime
from peewee import MySQLDatabase, Model, CharField, ForeignKeyField,\
    DateField, SmallIntegerField, TextField, DateTimeField

from playhouse.db_url import connect


# databases = MySQLDatabase('my_app', user='your user name', password='your password', host='127.0.01', port=3306)
database = connect('mysql://username:password@127.0.0.1:3306/database name')


class BaseModel(Model):

    class Meta:
        database = database

    def __str__(self):
        return str(self.id)


class User(BaseModel):
    username = CharField(max_length=35)
    password = CharField(max_length=35)


class Book(BaseModel):
    isbn = CharField(max_length=35)
    name = CharField(max_length=225)


class Author(BaseModel):
    name = CharField(max_length=35)


class Shelf(BaseModel):
    name = CharField(max_length=35)
    user = ForeignKeyField(User, backref='shelves')


class BookShelf(BaseModel):
    user = ForeignKeyField(User, backref='book_shelves')
    book = ForeignKeyField(Book, backref='book_shelves')
    shelf = ForeignKeyField(Shelf, backref='book_shelves')
    start_date = DateField(null=True)
    end_date = DateField(null=True)
    rete = SmallIntegerField()
    commetnt = TextField()

    created_time = DateTimeField(default=datetime())


class BookAuthor(BaseModel):
    book = ForeignKeyField(Book, backref='authors')
    author = ForeignKeyField(Author, backref='books')


class BookTranslator(BaseModel):
    book = ForeignKeyField(Book, backref='translators')
    translator = ForeignKeyField(Author, backref='translated_books')


class UserAuthor(BaseModel):
    user = ForeignKeyField(User, backref='followed_authors')
    authors = ForeignKeyField(Author, backref='following_users')


class UserRelation(BaseModel):
    following = ForeignKeyField(User, backref='following')
    follower = ForeignKeyField(User, backref='follower')
