"""
CP1404/CP5632 Practical
Emails
"""


def main():
    emails_dict = {}
    email = input("Email: ")
    while email != "":
        name = get_name(email)
        suggested_name = input(f"Is your name {name}? (Y/n) ").upper()
        if suggested_name != "Y" and suggested_name != "":
            name = input("Name: ")
        emails_dict[email] = name
        email = input("Email: ")

    for email, name in emails_dict.items():
        print(f"{name} ({email})")


def get_name(email):
    split_email = email.split("@")[0]
    further_split = split_email.split(".")
    name = " ".join(further_split).title()
    return name


main()

