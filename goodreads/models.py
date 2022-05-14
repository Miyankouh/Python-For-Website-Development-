from datetime import datetime
from peewee import MySQLDatabase, Model, CharField, ForeignKeyField, DateField, DateTimeField, SmallIntegerField, \
    TextField
from playhouse.db_url import connect


# database = MySQLDatabase('my_app', user='root', password='1234', host='127.0.0.1', port=3306)
database = connect('mysql://root:1234@127.0.0.1:3306/goodreads')


class BaseModel(Model):
    class Meta:
        database = database

    def __str__(self):
        return str(self.id)


class User(BaseModel):
    username = CharField(max_length=32)
    password = CharField(max_length=32)

    @classmethod
    def authenticate(cls, username, password):
        return cls.select().where(
            cls.username==username, cls.password==password
            ).first()


class Book(BaseModel):
    isbn = CharField(max_length=32)
    name = CharField(max_length=255)


class Author(BaseModel):
    name = CharField(max_length=32)


class Shelf(BaseModel):
    READ = 'read'
    CURRENTLY_READ = 'currently reading'
    WANT_TO_READ = 'want to read'

    name = CharField(max_length=32)
    user = ForeignKeyField(User, backref='shelves')


class BookShelf(BaseModel):
    user = ForeignKeyField(User, backref='book_shelves')
    book = ForeignKeyField(Book, backref='book_shelves')
    shelf = ForeignKeyField(Shelf, backref='book_shelves')
    start_date = DateField(null=True)
    end_date = DateField(null=True)
    rate = SmallIntegerField()
    comment = TextField()

    created_time = DateTimeField(default=datetime.now())

    def change_to_read(self):
        read_shelf = self.user.shelves.where(Shelf.name == Shelf.READ).first()
        self.shelf = read_shelf
        self.save()


class BookAuthor(BaseModel):
    book = ForeignKeyField(Book, backref='authors')
    author = ForeignKeyField(Author, backref='books')


class BookTranslator(BaseModel):
    book = ForeignKeyField(Book, backref='translators')
    translator = ForeignKeyField(Author, backref='translated_books')


class UserAuthorRelation(BaseModel):
    user = ForeignKeyField(User, backref='followed_authors')
    author = ForeignKeyField(Author, backref='following_users')


class UserRelation(BaseModel):
    following = ForeignKeyField(User, backref='following')
    follower = ForeignKeyField(User, backref='follower')
