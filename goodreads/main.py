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


def show_user_data(username="hosein", password="654321"):
    user = User.authenticate(username, password)
    
    if user is None:
        print("User not fond")
        return
    print(f"username: {user.username}")
    
    print("BOOKshelves")
    for shelf in user.shelves:
        print(f"\t{shelf.name} ({shelf.book_shelves.count()})")

    print("Books")
    for book_shelf_instance in user.book_shelves:
        print(f"{book_shelf_instance.id}\t{book_shelf_instance.book.name}")

    
    # book = Book.get_by_id(3)
    # read_shelf = user.shelves.where(Shelf.name == Shelf.READ)
    
    # name_book_shelf = BookShelf.create(
    #     user=user, book=book, shelf=read_shelf,
    #     start_date='2020-09-12', rate='5', comment="VERY GOOD"
    #     )


if __name__ == '__main__':
    # create_tables()
    # load_data()
    # show_data()
    show_user_data(username="hosein")
    # bs = BookShelf.get_by_id(2)
    # bs.change_to_read()
