MINIMUM_LENGTH = 5


def main():
    """Get password and display using stars."""
    print(f"Your password must be a minimum length of {MINIMUM_LENGTH} characters")
    password = get_password()
    display_stars(password)


def get_password():
    """Get valid password."""
    password = input("Please enter your password: ")
    while len(password) < MINIMUM_LENGTH:
        print("Invalid password")
        password = input("Please enter your password: ")
    return password


def display_stars(word):
    """Display word length using stars."""
    for i in range(len(word)):
        print("*", end="")


main()
