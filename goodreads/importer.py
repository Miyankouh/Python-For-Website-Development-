import json

from models import User, Book, Author, Shelf, BookAuthor, BookShelf


class BaseImporter:
    """Abstract base importer class which get filename and model class in
    each child class and load json data from `filename.json` to the database
    and given table defined by `model`"""

    filename = None
    model = None

    @classmethod
    def load(cls):
        """This method is abstract also so avoid to run instantly, without
        defining filename and model in class attributes"""

        with open(f'fixtures/{cls.filename}.json', encoding="utf8") as f:
            data = json.loads(f.read())

        instances = list()
        for instance in data:
            instances.append(cls.model.create(**instance))

        return instances


class UserImporter(BaseImporter):
    filename = 'users'
    model = User


class BookImporter(BaseImporter):
    filename = 'books'
    model = Book


class AuthorImporter(BaseImporter):
    filename = 'authors'
    model = Author


class ShelfImporter(BaseImporter):
    filename = None
    model = Shelf
    default_shelves = ['read', 'currently reading', 'want to read']

    @classmethod
    def load(cls):
        instances = list()
        for user in User.select():
            for shelf in cls.default_shelves:
                instances.append(cls.model.create(user=user, name=shelf))

        return instances


class BookAuthorImporter(BaseImporter):
    filename = 'books-authors'
    model = BookAuthor


class BookShelfImporter(BaseImporter):
    filename = 'books-shelves'
    model = BookShelf
