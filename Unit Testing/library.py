class Book:
    """ A class representing a book with a title and an author """
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    """ A class representing a library that can store books and perform various operations on them """
    def __init__(self):
        self.books = []           # private by convention, not enforced.

    def add_book(self, book: Book) -> None:     # type hinting for better code readability and error checking
        """ Adds a book to the library """
        # book = Book(title, author)  
        self.books.append(book)

    def delete_book(self, title: str) -> None:
        """ Deletes a book from the library with the given title """
        self.books = [b for b in self.books if b.title != title]

    def list_books(self) -> list[tuple[str, str]]:
        """ Returns a list of books currently added to the library """
        return [(b.title, b.author) for b in self.books]

    def search_book_title(self, title: str) -> list[tuple[str, str]]:
        """ Returns a list of books with the given title """
        return [(b.title, b.author) for b in self.books if b.title == title]

    def search_book_author(self, author: str) -> list[tuple[str, str]]:
        """ Returns a list of books by the given author """
        return [(b.title, b.author) for b in self.books if b.author == author]

    def generate_statistics(self) -> dict[str, int | set[str]]:
        """ Returns the number of books and a set of unique authors in the library """
        total_books = len(self.books)
        unique_authors = set(b.author for b in self.books)
        return {
            "total_books": total_books,
            "unique_authors": unique_authors
        }
    