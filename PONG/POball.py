import random
# ball.py
class Ball:
    def __init__(self, x, y, dx, dy, speed):
        self.x = x
        self.y = y
        self.dx = dx  # direção horizontal
        self.dy = dy  # direção vertical
        self.speed = speed

    def move(self):
        # Movimenta a bola
        self.x += self.dx * self.speed
        self.y += self.dy * self.speed

        # Se a bola colidir com as paredes superior e inferior, inverte a direção vertical
        if self.y <= 0 or self.y >= 20:  # Supondo que a altura da tela seja de 20
            self.dy = -self.dy

    def handleCollision(self, paddle):
        # Verifica se a bola colidiu com a raquete
        if self.x == paddle.x:
            if paddle.y <= self.y <= paddle.y + paddle.height:
                self.dx = -self.dx  # Inverte a direção horizontal
                return True
        return False

    def reset(self):
        # Reseta a posição da bola para o centro
        self.x = 25
        self.y = 10
        self.dx = random.choice([-1, 1])
        self.dy = random.choice([-1, 1])
