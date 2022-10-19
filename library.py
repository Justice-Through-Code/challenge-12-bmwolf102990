from book import Book


class Library():
    def __init__(self):
        """Initialize the empty book list"""
        pass

    def add_title(self):
        """Add a Book object with the given title and author to the book list"""
        pass

    def count_books(self):
        """Return the number of books currently in the booklist"""
        pass

    def remove_title(self):
        """Remove a book from the book list"""
        pass

    def is_empty(self):
        """Return True if the book list is empty, False if not"""
        return self.books == []
