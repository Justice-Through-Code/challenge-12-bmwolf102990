from book import Book

class Library():
    def __init__(self):
        """Initialize the empty book list"""
        self.books = []

    def add_title(self, title: str, author: str):
        """Add a Book object with the given title and author to the book list"""
        self.books.append(Book(title, author))

    def count_books(self):
        """Return the number of books currently in the booklist"""
        return int(len(self.books))

    def remove_title(self, title: str):
        """Remove a book from the book list"""
        filtered_list = []
        # LIST COMPREHENSION SYNTAX
        # It is basically saying "do this FOR each book IN the self.books list...if the book's title is NOT EQUAL TO the title that we are removing AND the book is NOT already IN the 'filtered_list' list...append that book to the 'filtered_list' list"
        [filtered_list.append(book) for book in self.books if book.title != title and book not in filtered_list]
        # then we reassign the value of our library's books list to the new filtered list
        self.books = filtered_list

    def display_books(self):
        # BONUS
        display_list = sorted(self.books, key=lambda x: x.title, reverse=False)
        
        for book in display_list:
            print(book)
    
    def is_empty(self):
        """Return True if the book list is empty, False if not"""
        return self.books == []
