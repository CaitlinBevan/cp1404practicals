"""CP1404/CP5632 Practical - Programming Language."""


class ProgrammingLanguage:
    """Represent a Programming Language object."""

    def __init__(self, name, typing, reflection, year):
        """Initialise a Programming Language instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Return if dynamic."""
        if self.typing == "dynamic":
            return True

