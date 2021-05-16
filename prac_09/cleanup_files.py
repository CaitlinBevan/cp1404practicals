"""
CP1404/CP5632 Practical
Cleanup Files
"""
import os


def main():
    """Program to rename files in Lyrics directory."""
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print(f"(Current working directory is: {os.getcwd()})")

        for filename in filenames:
            starting_name = os.path.join(directory_name, filename)
            new_name = os.path.join(directory_name, get_fixed_filename(filename))
            print(f"Renaming {starting_name} to {new_name}")
            os.rename(starting_name, new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    # for i, letter in enumerate(filename):
    #     print(i, letter)
    replace_letters = filename.replace(" ", "_").replace(".TXT", ".txt")
    join_letters = "".join(" " + letter if letter.isupper() else letter for letter in replace_letters).title()
    further_replace_letters = join_letters.replace(" ", "_").replace("__", "_").replace(".Txt", ".txt").replace("(_", "(")
    if further_replace_letters[:1] == "_":
        new_name = further_replace_letters[1:]
    else:
        new_name = further_replace_letters
    return new_name


main()
