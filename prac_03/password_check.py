MINIMUM_LENGTH = 5


def main():
    print(f"Your password must be a minimum length of {MINIMUM_LENGTH} characters")
    password = get_password()
    display_stars(password)


def get_password():
    password = input("Please enter your password: ")
    while not is_valid(password):
        print("Invalid password")
        password = input("Please enter your password: ")
    return password


def is_valid(password):
    if len(password) < MINIMUM_LENGTH:
        return False
    return True


def display_stars(word):
    for i in range(len(word)):
        print("*", end="")


main()
