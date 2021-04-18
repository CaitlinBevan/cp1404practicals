"""CP1404/CP5632 Practical - Guitars Program."""

from prac_06.guitar import Guitar


def main():
    """Guitars Program."""
    guitars = []

    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $ "))
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(new_guitar, "added")
        name = input("Name: ")

    # guitars.append(Guitar("Fender Stratocaster", 2014, 765.40))
    # guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = "(vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>19} ({guitar.year}), worth $ {guitar.cost:9,.2f} {vintage_string}")


main()
