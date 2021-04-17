"""CP1404/CP5632 Practical - Guitar Class."""


class Guitar:
    """Represent a Guitar object."""
    YEAR = 2021
    VINTAGE = 50

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string formatting."""
        return "{self.name} ({self.year}) : ${self.cost}".format(self=self)

    def get_age(self):
        """Return age of Guitar."""
        return Guitar.YEAR - self.year

    def is_vintage(self):
        """Return if age greater than or equal to Guitar.VINTAGE."""
        return self.get_age() >= Guitar.VINTAGE
