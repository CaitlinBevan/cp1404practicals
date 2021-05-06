"""
CP1404/CP5632 Practical
SilverServiceTaxi class
"""
from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi with a fancy fare."""
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi instance, based on parent class Taxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return a string like a Taxi but with the flagfall."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Return the price for the SilverServiceTaxi trip."""
        return self.flagfall + super().get_fare()
