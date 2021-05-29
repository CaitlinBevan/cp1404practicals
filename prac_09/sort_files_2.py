"""
CP1404/CP5632 Practical
Sort files 2
"""
import os
DIRECTORY = "FilesToSort"


def main():
    """Program to create a new directory for based on user input."""
    directory_dict = {}

    os.chdir(DIRECTORY)
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue

        new_directory = filename.split(".")
        if new_directory[1] not in directory_dict:
            category = input(f"What category would you like to sort {new_directory[1]} files into? ")
            directory_dict[new_directory[1]] = category

            try:
                os.mkdir(category)
            except FileExistsError:
                pass

        os.rename(filename, "{}/{}".format(directory_dict[new_directory[1]], filename))


main()
