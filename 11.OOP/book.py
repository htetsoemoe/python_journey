# chapter11_oop.py

# 1. Creating a Book Class
class Book:
    def __init__(self, title, author, isbn, publication_year):
        """
        Constructor Method to create a new Book Object.
        Attributes: title, author, isbn, publication_year, is_available (default True)
        """
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_year = publication_year
        self.is_available = True # A new book is considered available

    def display_info(self):
        """Method to display the book's information."""
        status = "available" if self.is_available else "not available yet"
        print(f"\n--- Book Information ---")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.isbn}")
        print(f"Publication Year: {self.publication_year}")
        print(f"Status: {status}")

    def borrow(self):
        """Method to borrow the book."""
        if self.is_available:
            self.is_available = False
            print(f"'{self.title}' has been borrowed.")
        else:
            print(f"'{self.title}' is currently not available.")

    def return_book(self):
        """Method to return the book."""
        if not self.is_available:
            self.is_available = True
            print(f"'{self.title}' has been returned.")
        else:
            print(f"'{self.title}' was already available.")

# 2. Creating Objects from the Book Class
book1 = Book("Python Basics", "Bob", "978-1234567890", 2022)
book2 = Book("Data Science Handbook", "Alice", "978-0987654321", 2021)

# 3. Printing the Objects' Attributes
print(f"Book1 Title: {book1.title}")
print(f"Book2 Author: {book2.author}")

# 4. Calling and using the Objects' Methods
print("\n--- Book1 Actions ---")
book1.display_info()
book1.borrow()
book1.display_info()
book1.borrow() # Try to borrow again (should not be possible)

print("\n--- Book2 Actions ---")
book2.display_info()
book2.borrow()
book2.display_info()
book2.return_book()
book2.display_info()
book2.return_book() # Try to return again (should not be possible)

# 5. Directly changing an Attribute's value
book1.publication_year = 2023
print(f"\nBook1's new publication year: {book1.publication_year}")
book1.display_info()
