from book import Book


class Library():
    def __init__(self):
        """Initialize the empty book list"""
        pass
        self.books = []

    def add_title(self, title: str, author: str):
        """Add a Book object with the given title and author to the book list"""
        pass
        new_book = Book(title, author)
        self.books.append(new_book)

    def count_books(self):
        """Return the number of books currently in the booklist"""
        pass
        return int(len(self.books))

    def remove_title(self, title):
        """Remove a book from the book list"""
        pass
        filtered_list = []
        [filtered_list.append(book) for book in self.books if book.title != title and book not in filtered_list]
        self.books = filtered_list

    def display_books(self):
        # BONUS
        display_list = sorted(self.books, key=lambda x: x.title, reverse=False)
        
        for book in display_list:
            print(book)
    
    def is_empty(self):
        """Return True if the book list is empty, False if not"""
        return self.books == []
