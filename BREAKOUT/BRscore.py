class Score:
    def __init__(self):
        self.value = 0

    def increment(self, color):
        points = 0
        # If the block is yellow, add 1 point
        if color == "Yellow":
            points = 1
        # If the block is green, add 3 points
        elif color == "Green":
            points = 3
        # If the block is red, add 7 points
        elif color == "Red":
            points = 7
        else:
            print(f"Unknown color: {color}")

        self.value += points
        print(f"Block {color} destroyed! {points} points added. Total score: {self.value}")

    def draw(self):
        print(f"Current score: {self.value}")
