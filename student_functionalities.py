import library_functions
from login import login
import borrow_functions


def student():
    while not login():
        pass

    while True:
        ch = int(input("Press 1 to check the book details\nPress 2 to Borrow/Return books\nPress 3 to Exit\n"))
        if ch == 1:
            # this function is defined in the library_functions
            library_functions.display()  # this functions shows all the books stored in the csv file
        elif ch == 2:
            borrow_functions.borrow_details()  # this functions enables the functionalities of the library
        elif ch == 3:
            print("Exiting the student menu.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
