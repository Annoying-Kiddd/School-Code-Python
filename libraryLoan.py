class Book:
    def __init__(self, title, author, quantity):
        self.title = title
        self.author = author
        self.quantity = quantity

    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, Available: {self.quantity}")

    def is_available(self):
        return self.quantity > 0

    def borrow(self):
        if self.is_available():
            self.quantity -= 1
            return True
        return False

    def return_book(self):
        self.quantity += 1

class Library:
    def __init__(self):
        self.books = {}  # Using a dictionary for efficient lookup

    def add_book(self, book):
        if book.title in self.books:
            self.books[book.title].quantity += book.quantity
        else:
            self.books[book.title] = book
        print(f"Added '{book.title}' to the library.")

    def display_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("\n--- Available Books ---")
            for book in self.books.values():
                book.display_info()

    def loan_book(self, title):
        if title in self.books:
            if self.books[title].borrow():
                print(f"You have successfully borrowed '{title}'.")
            else:
                print(f"Sorry, '{title}' is currently out of stock.")
        else:
            print(f"Error: '{title}' not found in the library.")

    def return_book(self, title):
        if title in self.books:
            self.books[title].return_book()
            print(f"You have successfully returned '{title}'.")
        else:
            print(f"Error: '{title}' does not belong to this library.")

def main():
    library = Library()
    
    # Add some initial books
    library.add_book(Book("The Hobbit", "J.R.R. Tolkien", 5))
    library.add_book(Book("Dune", "Frank Herbert", 3))
    
    while True:
        print("\n--- Library Menu ---")
        print("1. Display all books")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            library.display_books()
        elif choice == '2':
            title_to_loan = input("Enter the title of the book you want to borrow: ")
            library.loan_book(title_to_loan)
        elif choice == '3':
            title_to_return = input("Enter the title of the book you want to return: ")
            library.return_book(title_to_return)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()