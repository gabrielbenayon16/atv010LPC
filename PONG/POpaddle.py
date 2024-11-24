class Paddle:
    def __init__(self, x, y, width, height, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed

    def moveUp(self):
        self.y -= self.speed

    def moveDown(self):
        self.y += self.speed

    def get_position(self):
        return self.x, self.y
