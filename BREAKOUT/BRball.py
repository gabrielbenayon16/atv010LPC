class Ball:
    def __init__(self, x, y, speedX, speedY):
        self.size = None
        self.x = x
        self.y = y
        self.speedX = speedX
        self.speedY = speedY

    def move(self):
        self.x += self.speedX
        self.y += self.speedY

    def get_position(self):
        return self.x, self.y
