"""
CP1404/CP5632 Practical
Cleanup Files
"""
import os


def main():
    """Demo os module functions."""
    print(f"Starting directory is: {os.getcwd()}")

    # Change to desired directory
    os.chdir('Lyrics/Christmas')

    # Print a list of all files in current directory
    print(f"Files in {os.getcwd()}:\n{os.listdir('.')}\n")

    # Make a new directory
    # The next time you run this, it will crash if the directory exists

    try:
        os.mkdir('temp')
    except FileExistsError:
        pass

    # Loop through each file in the (current) directory
    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

        new_name = get_fixed_filename(filename)
        print(f"Renaming {filename} to {new_name}")
        os.rename(filename, new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    return new_name


main()
