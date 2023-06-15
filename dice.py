from random import randint

class Dice():
    """The class representing one dice."""

    def __init__(self, num_sides=6):
        """By default, a hexahedral dice is used."""
        self.num_sides = num_sides

    def roll(self):
        """Returns a random number from 1 to the number of edges."""
        return randint(1, self.num_sides)

