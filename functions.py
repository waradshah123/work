class Book:
    def __init__(self, book_id, title, author, genre):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.genre = genre
        self.status = "Available"  # All books are available by default
    
    def __repr__(self):
        return f"{self.title} by {self.author} ({self.genre}) - {self.status}"

class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.borrowed_books = []
    
    def __repr__(self):
        return f"User {self.user_id}: {self.name}, Borrowed books: {self.borrowed_books}"
class Library:
    def __init__(self):
        self.books = []
        self.users = []
    
    def add_book(self, book):
        self.books.append(book)
    
    def add_user(self, user):
        self.users.append(user)
    
    def borrow_book(self, user_id, book_id):
        user = self.get_user(user_id)
        book = self.get_book(book_id)
        if book and user:
            if book.status == "Available":
                book.status = "Checked Out"
                user.borrowed_books.append(book.title)
                print(f"{user.name} has borrowed '{book.title}'.")
            else:
                print(f"Sorry, the book '{book.title}' is already checked out.")
    
    def return_book(self, user_id, book_id):
        user = self.get_user(user_id)
        book = self.get_book(book_id)
        if book and user:
            if book.title in user.borrowed_books:
                book.status = "Available"
                user.borrowed_books.remove(book.title)
                print(f"{user.name} has returned '{book.title}'.")
            else:
                print(f"{user.name} has not borrowed '{book.title}'.")
    
    def search_books(self, criterion, search_value):
        results = [book for book in self.books if search_value.lower() in getattr(book, criterion).lower()]
        if results:
            for book in results:
                print(book)
        else:
            print("No matching books found.")
    
    def view_books(self, status=None):
        if status:
            books_to_view = [book for book in self.books if book.status == status]
        else:
            books_to_view = self.books
        for book in books_to_view:
            print(book)
    
    def get_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        print(f"Book with ID {book_id} not found.")
        return None
    
    def get_user(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                return user
        print(f"User with ID {user_id} not found.")
        return None
def main_menu(library):
    while True:
        print("\n--- Library Management System ---")
        print("1. View all books")
        print("2. View available books")
        print("3. View checked-out books")
        print("4. Search for a book")
        print("5. Borrow a book")
        print("6. Return a book")
        print("7. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            library.view_books()
        elif choice == '2':
            library.view_books("Available")
        elif choice == '3':
            library.view_books("Checked Out")
        elif choice == '4':
            criterion = input("Search by (title/author/genre): ").lower()
            search_value = input(f"Enter {criterion}: ")
            library.search_books(criterion, search_value)
        elif choice == '5':
            user_id = int(input("Enter your user ID: "))
            book_id = int(input("Enter the book ID to borrow: "))
            library.borrow_book(user_id, book_id)
        elif choice == '6':
            user_id = int(input("Enter your user ID: "))
            book_id = int(input("Enter the book ID to return: "))
            library.return_book(user_id, book_id)
        elif choice == '7':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":

    my_library = Library()
    

    my_library.add_book(Book(1, "The Catcher in the Rye", "J.D. Salinger", "Fiction"))
    my_library.add_book(Book(2, "To Kill a Mockingbird", "Harper Lee", "Fiction"))
    my_library.add_book(Book(3, "1984", "George Orwell", "Dystopian"))
    
    my_library.add_user(User(1, "Alice"))
    my_library.add_user(User(2, "Bob"))
    
    
    main_menu(my_library)
