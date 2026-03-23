import library

Books = [
    ("To Kill a Mockingbird", "Harper Lee"),
    ("The Great Gatsby", "F. Scott Fitzgerald"),
    ("The Lord of the Rings", "J.R.R. Tolkien"),
    ("The checklist manifesto", "Atul Gawande"),
    ("Harry Potter", "J.K. Rowling"),
    ("So Good They Can't Ignore You", "Cal Newport"),
    ("Deep work", "Cal Newport"),
    ("The 4 hour work week", "Tim Ferriss"),
    ("Ego is the enemy", "Ryan Holiday"),
    ("Hell yeah or no", "Derek Sivers"),
]

# Grok suggestion for reducing duplicates
def populate_library(lib, book_data):
    for title, author in book_data:
        lib.add_book(library.Book(title, author))

# Grok code for the test_add_book function: Shorter and more concise
def test_add_book():
    lib = library.Library()                  # Create a new library instance
    populate_library(lib, Books)
    expected = [(t, a) for t, a in Books]
    assert lib.list_books() == expected

# This is a test function that tests the add_book function in the library Object
def test_add_book():
    """ Adds a book to the library with the given title and author """
    lib = library.Library()
    books = [library.Book(title, author) for title, author in Books]

    for book in books:
        lib.add_book(book)

    assert lib.list_books() == [(book.title, book.author) for book in books]

# This is a test function that tests the delete_book function in the library Object
def test_delete_book():
    """ Deletes a book from the library with the given title """
    lib = library.Library()

    added_books = [library.Book(title, author) for title, author in Books]

    for book in added_books:
        lib.add_book(book)
    # Deleting the book at index 4 (Harry Potter) from the library
    lib.delete_book(added_books[4].title)
    # lib.delete_book("Harry Potter")

    remaining_books = lib.list_books()
    # Asserting that the remaining books in the library are correct after deletion
    assert len(remaining_books) == len(Books) - 1
    # assert ("Harry Potter", "J.K. Rowling") not in remaining_books
    assert lib.list_books() == [(book.title, book.author) for book in added_books if book != added_books[4]]

# Grok code for the test_delete_book function in the library Object
# def test_delete_book():
#     lib = library.Library()
#     input_books = [library.Book(t, a) for t, a in Books]
#     for b in input_books:
#         lib.add_book(b)

#     lib.delete_book("Harry Potter")           # known title

#     remaining = lib.list_books()
#     assert len(remaining) == len(Books) - 1
#     assert ("Harry Potter", "J.K. Rowling") not in remaining

# Even stronger (two separate tests)
# def test_delete_book_removes_existing_title():
#     lib = library.Library()
#     added_books = [library.Book(t, a) for t, a in Books]
#     for b in added_books:
#         lib.add_book(b)

#     lib.delete_book("The Great Gatsby")

#     remaining_titles = {title for title, _ in lib.list_books()}
#     assert "The Great Gatsby" not in remaining_titles
#     assert len(remaining_titles) == len(Books) - 1


# def test_delete_book_does_nothing_for_non_existing_title():
#     lib = library.Library()
#     added_books = [library.Book(t, a) for t, a in Books]
#     for b in added_books:
#         lib.add_book(b)

#     before = len(lib.list_books())
    
#     lib.delete_book("Non Existent Book 123")

#     assert len(lib.list_books()) == before

# This is a test function that tests the list_book function in the library Object
def test_list_book():
    """ Returns a list of books currently added to the library """
    lib = library.Library()
    # Creating book objects from the Books list
    books = [library.Book(title, author) for title, author in Books]
    # Adding the book objects to the library
    for book in books:
        lib.add_book(book)
    # Asserting that the list_books function returns the correct list of books
    assert lib.list_books() == [(book.title, book.author) for book in books]

# This is a test function that tests the search_book_title function in the library Object
def test_search_book_title():
    """ Returns a list of books with the given title """
    lib = library.Library()

    added_books = [library.Book(title, author) for title, author in Books]

    for book in added_books:
        lib.add_book(book)

    search_result = lib.search_book_title("The Lord of the Rings")
    expected = [
        (book.title, book.author) 
        for book in added_books 
        if book.title == "The Lord of the Rings"]
    
    assert search_result == expected

# This is a test function that tests the search_book_author function in the library Object
def test_search_book_author():
    """ Returns a list of books by the given author """
    lib = library.Library()

    added_books = [library.Book(title, author) for title, author in Books]

    for book in added_books:
        lib.add_book(book)
  
    search_result = lib.search_book_author("J.K. Rowling")
    expected = [(book.title, book.author) for book in added_books if book.author == "J.K. Rowling"]

    assert search_result == expected

# This is a test function that tests the generation_stat function in the library Object
def test_generate_statistics():
    """ Returns the number of books and a set of unique authors in the library """
    lib = library.Library()
    added_books = [library.Book(title, author) for title, author in Books]

    for book in added_books:
        lib.add_book(book)

    stats = lib.generate_statistics()

    expected_authors = set(book.author for book in added_books)
    # expected_authors = {
    #     "Harper Lee", "F. Scott Fitzgerald", "J.R.R. Tolkien",
    #     "Atul Gawande", "J.K. Rowling", "Cal Newport",
    #     "Tim Ferriss", "Ryan Holiday", "Derek Sivers"
    # }

    assert stats == {
        "total_books": len(added_books),
        "unique_authors": expected_authors
    }

