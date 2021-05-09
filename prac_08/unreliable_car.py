"""
CP1404/CP5632 Practical
Unreliable Car Class
"""
from prac_08.car import Car
import random


class UnreliableCar(Car):
    """UnreliableCar Class."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive like parent Car but generate a random number between 0 and 100, and only drive
        the car if that number is less than the car's reliability."""
        random_number = random.randint(1, 100)
        if random_number >= self.reliability:
            distance = 0
        return super().drive(distance)
