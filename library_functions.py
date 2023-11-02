import datetime
from login import User

user = User()


def borrow_book(book_title):
    import csv
    # check if the book is listed in the csv or not
    with open('books.csv', 'r') as borrow:
        # reader = csv.reader(borrow)
        for s in borrow:
            s_data = s.split(',')
            if s_data[1] == book_title:
                print("The book is found in the database")
                # userid = input("Enter your user id to borrow book")
                user.get_userid()
                # adding date and time in the csv file
                date_format = '%d-%m-%y'
                current_date = datetime.datetime.now().strftime(date_format)
                # now adding the book name, the user id and date of borrow and return in the csv file
                with open('details.csv', 'a', newline='') as csvfile:  # write all the details in the new csv file
                    csvwriter = csv.writer(csvfile)
                    csvwriter.writerow([user.get_userid(), book_title, current_date])
                    # csvfile.write(','.join(book_title) + '\n')
                print("The book has been successfully borrowed by user you")
                break
        else:
            print("The book is not found in the database")


# Display Book Details
def display():
    # Read books from CSV file
    with open('books.csv', 'r') as file:
        for line in file:
            fields = line.split(',')
            for field in fields:
                print(field, end=" ")


# def return_book():
#     return_date = input("Enter the second date (YYYY-MM-DD):")
#     date_of_return = datetime.strptime(return_date, "%Y-%m-%d")
#     fine = fine_calc()
#     if fine == 0:
#         print("You returned the book successfully")
#     elif fine > 0:
#         print(f"Please pay the fine of Rs {fine}")
#         with open('details.csv', 'r') as file:
#             lines = file.readlines()
#
#         # Modify the specified column with new data
#         for i in range(len(lines)):
#             row = lines[i].strip().split(',')
#             row[3] = str(fine)
#             lines[i] = ','.join(row) + '\n'
#
#     # with open('details.csv', 'a') as fileS:
#     # for line in fileS:
#     # line_s = line.split(',')
#     # fileS.write(date_of_return)

def return_book(book_to_return):
    pass
#     with open("details.csv", 'r') as verify:
#         for useR in verify:
#             user_data = useR.split(',')
#             book_in_csv = useR.split(',')
#             if user_data[0] == user.get_userid():
#                 if book_in_csv[1] == book_to_return:
#                     return_date = input("Enter the return date (YYYY-MM-DD):")
#                     date_of_return = datetime.datetime.strptime(return_date, "%Y-%m-%d")
#                     fine = fine_calc(date_of_return)
#                     if fine == 0:
#                         print("You returned the book successfully")
#                     elif fine > 0:
#                         print(f"Please pay the fine of Rs {fine}")
#
#                     with open('details.csv', 'r') as file:
#                         lines = file.readlines()
#
#                     # Modify the specified column with new data
#                     for i in range(len(lines)):
#                         row = lines[i].strip().split(',')
#                         row[3] = str(fine)
#                         lines[i] = ','.join(row) + '\n'
#
#                     # Overwrite the file with the updated data
#                     with open('details.csv', 'w') as file:
#                         file.writelines(lines)
#
#                     # To display the updated file
#                     with open('details.csv', 'r') as file:
#                         print(file.read())
#                 else:
#                     print("There is no book which is issued to the user")
#             else:
#                 print("User not found")


def fine_calc(date_of_return):
    date_difference = date_of_return - borrow_book.current_date
    if date_difference == 7:
        return 0
    else:
        return (date_difference - 7) * 2


def add_book():
    while True:
        with open('books.csv', "a") as csv_file:
            book_no = input("enter the book number")
            bn = input("enter the book name")
            author = input("enter the author name")
            genre = input("enter the book genre")
            nob = input("enter the number of books available")
            csv_file.write(f"{book_no},{bn},{author},{genre},{nob}\n")
            ch = input("Do you want to exit Y/N?: ")
        if ch == 'Y' or ch == 'y':
            break
        else:
            print("Wrong Choice")


def display_stu():
    with open('details.csv', 'r') as file:
        for line in file:
            fields = line.split(',')
            for field in fields:
                print(field, end=" ")
