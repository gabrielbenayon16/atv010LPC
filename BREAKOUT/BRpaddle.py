class Paddle:
    def __init__(self, x, y, width, height, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed

    def autoMove(self, ball_x):
        # Move automaticamente para acompanhar a bola
        if ball_x < self.x + self.width / 2:
            self.x = max(0, self.x - self.speed)
            print("A raquete moveu-se para a esquerda.")
        elif ball_x > self.x + self.width / 2:
            self.x = min(100 - self.width, self.x + self.speed)
            print("A raquete moveu-se para a direita.")
