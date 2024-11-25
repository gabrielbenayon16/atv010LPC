class Score:
    def __init__(self):
        self.value = 0

    def increment(self, points):
        self.value += points
        print(f"Score incrementado. Novo valor: {self.value}")

    def getValue(self):
        return self.value

    def reset(self):
        self.value = 0
        print("Score resetado.")