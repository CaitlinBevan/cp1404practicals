"""
CP1404/CP5632 Practical
Emails
"""


def main():
    email_dict = {}
    email = input("Email: ")
    while email != "":
        name = get_name(email)
        print(f"Is your name {name}? (Y/n) ")
        email = input("Email: ")


def get_name(email):
    split_email = email.split("@")[0]
    email_name = split_email.split(".")
    name = " ".join(email_name).title()
    return name


main()

