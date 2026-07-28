"""
Demonstrates super(): Library inherits from Book and uses super() to call
the parent class's __init__() and display() instead of rewriting them.
"""


class Book:
    def __init__(self, name: str, author: str, publish_year: int):
        """Initialize a Book with its name, author, and publish year."""
        self.name = name
        self.author = author
        self.publish_year = publish_year

    def display(self):
        """Print the book's basic details."""
        print("Book Name:", self.name)
        print("Book Author:", self.author)
        print("Publish Year:", self.publish_year)


class Library(Book):
    """A Library is a Book (inheritance) that also tracks the collection's stats."""

    def __init__(self, name: str, author: str, publish_year: int, book_count: int, best_book: str):
        """Initialize the Book fields via super(), then add Library-specific fields."""
        super().__init__(name, author, publish_year)
        self.book_count = book_count
        self.best_book = best_book

    def display_library_info(self):
        """Print the parent Book's details, then the Library's own details."""
        super().display()
        print("Total Book Count:", self.book_count)
        print("Best Performing Book:", self.best_book)


# Corrected initialization with proper argument matching
library_collection = Library(
    name="The Alchemist",
    author="Paulo Coelho",
    publish_year=1988,
    book_count=2,
    best_book="The Alchemist"
)

library_collection.display_library_info()
