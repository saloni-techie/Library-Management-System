from library_functions import borrow_book
from library_functions import return_book


def borrow_details():
    while True:
        print("1. Borrow a book")
        print("2. Return a book")
        print("3. Exit")
        choice = int(input("Enter your choice (1-4): "))
        if choice == 1:
            book_to_borrow = input("Enter the name of the book you want to borrow: ")
            borrow_book(book_to_borrow)
        elif choice == 2:
            book_to_return = input("Enter the name of the book you want to return: ")
            return_book(book_to_return)
        elif choice == 3:
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
