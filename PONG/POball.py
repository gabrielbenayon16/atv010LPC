import random
class Ball:
    def __init__(self, x, y, dx, dy, speed):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.speed = speed
        self.size = 1

    def move(self):
        self.x += self.dx * self.speed
        self.y += self.dy * self.speed
        if self.y <= 0 or self.y >= 20 - self.size:
            self.dy = -self.dy
            print("Ball collides with wall!")

    def handleCollision(self, paddle):
        if (
            self.x <= paddle.x + paddle.width and
            self.x + self.size >= paddle.x and
            self.y <= paddle.y + paddle.height and
            self.y + self.size >= paddle.y
        ):
            if self.dx < 0:
                self.x = paddle.x + paddle.width
            elif self.dx > 0:
                self.x = paddle.x - self.size
            self.dx = -self.dx
            return True
        return False

    def reset(self):
        self.x = 25
        self.y = 10
        self.dx = random.choice([-1, 1])
        self.dy = random.choice([-1, 1])
