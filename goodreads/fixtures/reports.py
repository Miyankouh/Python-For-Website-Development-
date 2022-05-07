from models import User, Shelf, Book


def show_users():
    users = User.select()
    for user in users:
        # shelves_count = Shelf.select().where(Shelf.user == user).count()
        shelves_count = user.shelves.count()

        shelves = ', '.join([shelf.name for shelf in user.shelves])
        print(user.username, '\t', shelves, '\t', user.book_shelves.count())


def show_books():
    books = Book.select()
    for book in books:
        authors = ', '.join([book_author.author.name for book_author in book.authors])
        print(f"{book.name}({book.isbn})", '\t', authors)
