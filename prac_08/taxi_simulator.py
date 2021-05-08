"""
CP1404/CP5632 Practical
Taxi Simulator
"""
from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Taxi Program."""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    bill_to_date = 0.00

    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            print("Taxis available:")
            display_available_taxis(taxis)
            taxi_choice = int(input("Choose taxi: "))
            try:
                current_taxi = taxis[taxi_choice]
            except IndexError:
                print("Invalid taxi choice")
            print(f"Bill to date: ${bill_to_date:.2f}")
        elif choice == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                current_taxi.start_fare()
                distance_to_drive = int(input("Drive how far? "))
                current_taxi.drive(distance_to_drive)
                current_fare = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${current_fare:.2f}")
                bill_to_date += current_fare
            print(f"Bill to date: ${bill_to_date:.2f}")
        else:
            print("Invalid option")
            print(f"Bill to date: ${bill_to_date:.2f}")
        print(MENU)
        choice = input(">>> ").lower()
    print(f"Total trip cost: {bill_to_date:.2f}")
    print("Taxis are now:")
    display_available_taxis(taxis)


def display_available_taxis(taxis):
    """Display available taxis."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


main()
