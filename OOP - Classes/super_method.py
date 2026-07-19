class Book:
    def __init__(self, name: str, author: str, publish_year: int):
        self.name = name
        self.author = author
        self.publish_year = publish_year

    def display(self):
        print("Book Name:", self.name)
        print("Book Author:", self.author)
        print("Publish Year:", self.publish_year)


class Library(Book):
    def __init__(self, name: str, author: str, publish_year: int, book_count: int, best_book: str):
        super().__init__(name, author, publish_year)
        self.book_count = book_count
        self.best_book = best_book

    def display_library_info(self):
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
