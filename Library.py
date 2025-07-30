#---------------------------------- Task 3 ---------------------------------- #
""" DESCRIPTION:
Create a class called 'Book' to represent a book in a library system. The class should have the following attributes and methods:

Attributes:
- 'title': a string representing the title of the book.
- 'author': a string representing the author of the book.
- 'isbn': a string representing the ISBN of the book.
- 'year': an integer representing the publication year of the book.

Methods:
- '__str__()': a method that returns a formatted string with the book's title, author, ISBN, and publication year.

Create a class called 'Library' that manages a collection of books. The class should have the following methods:

Methods:

- **Add Books**:Create new book entries with details including
- **Edit Books**: Modify any book information after creation

- **Remove Books**: Delete books from the collection with confirmation

- **View Books**: Display book details in a formatted way

Create instances of the 'Book' class and demonstrate the usage of the 'Library' class by adding, removing, and listing books.
"""


## Define the Book class
class Book:
    def __init__(self, title, author, isbn, year):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year = year

    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nISBN: {self.isbn}\nYear: {self.year}"

 
### Define the Library class
class Library:
    def __init__(self):
        self.collections =[]
    

    def add_book(self, book):
        if not any(b.isbn == book.isbn for b in self.collections):
            self.collections.append(book)
     
     

    def remove_book(self, isbn):
        for book in self.collections:
            if book.isbn == isbn:
                self.collections.remove(book)
                break
                
           

    def find_book(self, isbn):
        for book in self.collections:
            if book.isbn == isbn:
                return book
        return None

    
    def edit_book(self, isbn, new_title, new_author, new_year):
        book = self.find_book(isbn)
        
        if book:
            book.title = new_title
            book.author = new_author
            book.year = new_year
            return True
           
        return False
            
         

    def list_books(self):
               
        for book in self.collections:
            print(f"{book}\n--------------------")




### TEST
book1 = Book("1984", "George Orwell", "123456789", 1949)
book2 = Book("To Kill a Mockingbird", "Harper Lee", "987654321", 1960)
book3 = Book("My book mistery", "Asi Asi", "123123123", 2020)

  

library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print("List of books in the library:")
library.list_books()

# Remove a book
library.remove_book("123456789")
print("\nList of books after removal:")
library.list_books()

# # Find a book
book = library.find_book("123123123")
if book:
    print(f"\nFound book: {book}")
else:
    print("\nBook not found.")


# # **Edit Books**: Modify any book information after creation
success = library.edit_book(isbn="123123123", new_title="New Title", new_author="New Author", new_year=2022)

if success:
    print("\nThe book was edited successfully.:")
    book = library.find_book("123123123")
    print(book)
else:
    print("\nEdit failed - ISBN not found.")

