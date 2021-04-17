"""CP1404/CP5632 Practical - Guitar Test Program."""

from prac_06.guitar import Guitar


def main():
    guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2013, 16035.40)

    print(f"{guitar.name} get_age() - Expected 99. Got {guitar.get_age()}")
    print(f"{another_guitar.name} get_age() - Expected 8. Got {another_guitar.get_age()}")

    print(f"{guitar.name} s_vintage() - Expected True. Got {guitar.is_vintage()}")
    print(f"{another_guitar.name} s_vintage() - Expected False. Got {another_guitar.is_vintage()}")


main()
