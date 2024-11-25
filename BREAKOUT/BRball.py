class Ball:
    def __init__(self, x, y, size, speedX, speedY):
        self.x = x
        self.y = y
        self.size = size
        self.speedX = speedX
        self.speedY = speedY

    def move(self):
        self.x += self.speedX
        self.y += self.speedY

    def handleCollision(self, paddle, blocks):
        if self.x <= 0 or self.x >= 100:
            self.speedX *= -1
            print("Ball hit the wall!")

        if self.y <= 0:
            self.speedY *= -1
            print("Ball hit the ceiling.")

        if paddle.y == self.y + self.size and paddle.x <= self.x <= paddle.x + paddle.width:
            self.speedY *= -1
            print("Ball hit the paddle.")

        for block in blocks:
            if block.y <= self.y <= block.y + block.height and block.x <= self.x <= block.x + block.width:
                blocks.remove(block)
                self.speedY *= -1
                print(f"Ball hit a block at position ({block.x}, {block.y}) and destroyed it.")
                return True
        return False
