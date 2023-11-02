
def login():
    user.enter_userid()
    password = input("Enter your password:")
    with open('credential.csv', 'r') as file:
        # reader = csv.reader(file)
        for row in file:
            row_data = row.split(',')
            if row_data[0] == user.get_userid() and row_data[1] == password:
                print("\nLogin successful!")
                return True
    print("\nInvalid id or password. Please try again.")
    return False


# here we will store the user id and use it in another functions
class User:
    def __init__(self):
        self.userid = None

    def enter_userid(self):  # we are taking input from the user
        self.userid = input("Enter your User id:")

    def get_userid(self):  # we are returning the user id as output
        return self.userid


user = User()  # we are creating an instance for the variable
