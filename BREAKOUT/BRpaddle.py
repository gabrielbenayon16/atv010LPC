class Paddle:
    def __init__(self, x, y, width):
        self.x = x
        self.y = y
        self.width = width

    def get_position(self):
        return self.x, self.y
