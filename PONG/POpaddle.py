class Paddle:
    def __init__(self, x, y, width, height, speed):
        self.x = x
        self.y = y
        self.width = width  # Raquete mais estreita
        self.height = height
        self.speed = speed

    def moveUp(self):
        self.y -= self.speed

    def moveDown(self):
        self.y += self.speed

    def reset(self):
        self.y = 10  # Posição inicial fixa
        print("Raquete resetada para a posição inicial.")

    def draw(self):
        print(f"Raquete na posição ({self.x}, {self.y})")

    def getRect(self):
        return (self.x, self.y, self.width, self.height)
