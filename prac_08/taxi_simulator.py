"""
CP1404/CP5632 Practical
Taxi Simulator
"""
from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    """Taxi Program."""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    bill_to_date = 0.00

    print("Let's drive!")
    print("q)uit, c)hoose taxi, d)rive")
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            print("Taxis available:")
            for i, taxi in enumerate(taxis):
                print(i, taxi)
                print("Invalid taxi choice")
            print("Bill to date: ")
        elif choice == "d":
            print("Drive how far? ")
            print("Your Limo trip cost you $102.90")
            print("Bill to date: $682.60")
        else:
            print("Invalid option")
        print("Let's drive!")
        print("q)uit, c)hoose taxi, d)rive")
        choice = input(">>> ").lower()
    print("Total trip cost: ")
    print("Taxis are now:")
    for i, taxi in enumerate(taxis):
        print(i, taxi)


main()
