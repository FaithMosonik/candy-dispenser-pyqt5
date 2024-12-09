import random

class Candy:
    # Available candy colors
    COLORS = ["red", "blue", "green", "yellow", "purple", "orange"]

    def __init__(self):
        # Randomly assign a color to the candy
        self.color = random.choice(self.COLORS)

    def __str__(self):
        return f"{self.color} candy"