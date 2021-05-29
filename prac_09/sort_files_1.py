"""
CP1404/CP5632 Practical
Sort files 1
"""
import os
import shutil
DIRECTORY = "FilesToSort"


def main():
    """Program to create a new directory for each extension."""
    os.chdir(DIRECTORY)
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue

        new_directory = filename.split(".")

        try:
            os.mkdir(new_directory[1])
        except FileExistsError:
            pass

        if new_directory[1] in filename:
            shutil.move(filename, new_directory[1])


main()
