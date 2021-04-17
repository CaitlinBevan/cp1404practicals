"""CP1404/CP5632 Practical - Guitar Class."""


class Guitar:
    """Represent a Guitar object."""
    YEAR = 2021

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{self.name} ({self.year}) : ${self.cost}".format(self=self)

    def get_age(self):
        return Guitar.YEAR - self.year

    def is_vintage(self, get_age):
        return get_age(self) >= 50
