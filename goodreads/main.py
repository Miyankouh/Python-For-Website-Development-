from fixtures.reports import show_users, show_books
from importer import UserImporter, BookImporter, BookAuthorImporter, ShelfImporter, BookShelfImporter, AuthorImporter
from models import database, User, Book, Author, Shelf, BookShelf, BookAuthor, BookTranslator, UserAuthorRelation, \
    UserRelation


def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+Shift+B to toggle the breakpoint.


def load_data():
    importer_classes = [
        UserImporter, BookImporter, AuthorImporter,
        BookAuthorImporter, ShelfImporter, BookShelfImporter
    ]
    for _class in importer_classes:
        print(_class.load())


def create_tables():
    database.create_tables(
        [User, Book, Author, Shelf, BookShelf,
         BookAuthor, BookTranslator, UserAuthorRelation,
         UserRelation]
    )


def show_data():
    print("#" * 79)
    show_users()
    print("#" * 79)
    show_books()
    print("#" * 79)


if __name__ == '__main__':
    # create_tables()
    load_data()
    # show_data()
