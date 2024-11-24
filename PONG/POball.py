class Ball:
    def __init__(self, x, y, size, speedX, speedY):
        self.x = x
        self.y = y
        self.size = size
        self.speedX = speedX
        self.speedY = speedY
        self.initialSpeedX = speedX
        self.initialSpeedY = speedY

    def move(self):
        self.x += self.speedX
        self.y += self.speedY

    def reset(self):
        self.x = 50
        self.y = 25
        self.speedX = self.initialSpeedX
        self.speedY = self.initialSpeedY

    def handleCollision(self, paddle):
        if paddle.x <= self.x <= paddle.x + paddle.width:
            if paddle.y <= self.y <= paddle.y + paddle.height:
                self.speedX = -self.speedX

    def get_position(self):
        return self.x, self.y
