"""CP1404/CP5632 Practical
UnreliableCar Test"""

from prac_08.unreliable_car import UnreliableCar


def main():
    """Test code for UnreliableCar Class."""
    new_car = UnreliableCar("Unreliable Car", 100, 80)
    new_car.drive(40)
    print(new_car)


main()
