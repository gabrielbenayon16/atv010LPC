class Score:
    def __init__(self):
        self.value = 0

    def increment(self, color):
        points = 0
        if color == "Yellow":
            points = 1
        elif color == "Green":
            points = 3
        elif color == "Red":
            points = 7
        else:
            print(f"Unknown color: {color}")

        self.value += points
        print(f"Block {color} destroyed! {points} points added. Total score: {self.value}")

    def draw(self):
        print(f"Current score: {self.value}")
