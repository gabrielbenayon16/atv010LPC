class Score:
    def __init__(self):
        self.value = 0

    def increment(self, points):
        self.value += points

    def getValue(self):
        return self.value

    def reset(self):
        self.value = 0
