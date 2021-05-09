"""CP1404/CP5632 Practical
Silver Service Taxi Test"""

from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    """Test code for SilverServiceTaxi Class."""
    new_taxi = SilverServiceTaxi("Fancy Taxi", 100, 2)
    new_taxi.drive(18)
    print(new_taxi)
    print(f"Silver Service Taxi Fare is: ${new_taxi.get_fare():.2f}")


main()
