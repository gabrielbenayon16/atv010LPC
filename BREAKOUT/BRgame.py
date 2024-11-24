import time
from BRball import Ball
from BREAKOUT.BRpaddle import Paddle
from BRblock import Block

class Game:
    def __init__(self):
        self.ball = Ball(10, -2, 5, 10)
        self.paddle = Paddle(10, 9, 100)
        self.blocks = [
            Block(x * 60, 200, 50, 20) for x in range(5)
        ]  # Cria 5 blocos na linha 200
        self.running = True
        self.score = 0  # Pontuação do jogo

    def check_collisions(self):
        ball_x, ball_y = self.ball.get_position()

        # Verifica colisão com os blocos
        for block in self.blocks:
            if not block.destroyed and block.collides_with(ball_x, ball_y, self.ball.size):
                print("A bola colidiu com um bloco!")
                block.destroyed = True  # Marca o bloco como destruído
                self.ball.speedY = -self.ball.speedY  # Reverte direção Y
                self.score += 10  # Incrementa a pontuação
                break  # Só uma colisão por vez

        # Verifica colisão com a raquete
        paddle_x, paddle_y = self.paddle.get_position()
        if (paddle_x <= ball_x <= paddle_x + self.paddle.width and
                paddle_y <= ball_y <= paddle_y + 10):  # Tolerância de 10px
            print("A bola colidiu com a raquete!")
            self.ball.speedY = -self.ball.speedY  # Reverte direção Y

    def update(self):
        self.ball.move()

    def draw_status(self):
        """
        Exibe o status do jogo no terminal.
        """
        ball_x, ball_y = self.ball.get_position()
        paddle_x, paddle_y = self.paddle.get_position()
        blocks_remaining = sum(1 for block in self.blocks if not block.destroyed)

        print(f"Posição da bola: ({ball_x}, {ball_y})")
        print(f"Raquete em: ({paddle_x}, {paddle_y})")
        print(f"Blocos restantes: {blocks_remaining}")
        print(f"Pontuação: {self.score}")
        print("------")

    def run(self):
        print("Iniciando o jogo...")
        while self.running:
            self.update()
            self.check_collisions()
            self.draw_status()

            # Stop the game if the ball goes off the screen
            _, ball_y = self.ball.get_position()
            if ball_y > 500:  # Simula o fim do jogo
                print("Fim do jogo! A bola saiu dos limites.")
                self.running = False

            time.sleep(2)  # Simula o intervalo de tempo
