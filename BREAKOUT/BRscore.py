class Score:
    def __init__(self):
        self.value = 0

    def increment(self, points):
        self.value += points
        print(f"Score updated: {self.value}")

    def draw(self):
        print(f"Current score: {self.value}")
