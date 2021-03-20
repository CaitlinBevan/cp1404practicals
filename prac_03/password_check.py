MINIMUM_LENGTH = 5


def main():
    print(f"Your password must be a minimum length of {MINIMUM_LENGTH} characters")
    password = input("Please enter your password: ")
    while not is_password_valid(password):
        print("Invalid password")
        password = input("Please enter your password: ")
    for i in range(len(password)):
        print("*", end="")


def is_password_valid(password):
    if len(password) < MINIMUM_LENGTH:
        return False
    return True


main()
