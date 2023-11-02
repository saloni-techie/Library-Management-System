from login import login
from library_functions import add_book
from library_functions import display_stu
from library_functions import return_book


def management():
    while not login():
        pass

    while True:
        ch = input(
            "Enter 1 to add book\nEnter 2 take the returned book\nEnter 3 to display student details\nEnter q to "
            "quit")
        if ch == '1':
            add_book()
        elif ch == '2':
            return_book()
        elif ch == '3':
            display_stu()
        elif ch == 'q':
            break
        else:
            print("Wrong Choice")
