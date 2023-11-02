
# we need to import all the functions which will be used in the main function

from student_functionalities import student
from management_functionalities import management

# here the function begins

print("! Welcome to Library Management System !")

while True:
    user = input("Login as student / Login as management: ")
    if user == "student" or user == 's':
        student()
        break
    elif user == "management" or user == 'm':
        management()
        break
    else:
        print("Enter 'student' if you are a student or enter 'management' if you are in management.")
        continue
