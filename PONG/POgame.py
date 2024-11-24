from PONG.POball import Ball
from POpaddle import Paddle
from POscore import Score
import time

class Game:
    def __init__(self):
        self.ball = Ball(50, 25, 5, 2, 1)
        self.player1 = Paddle(5, 20, 5, 10, 2)
        self.player2 = Paddle(90, 20, 5, 10, 2)
        self.score1 = Score()
        self.score2 = Score()
        self.running = True

    def handleEvents(self):
        # Simulando o movimento das raquetes (exemplo fictício)
        self.player1.moveUp()  # Jogador 1 sobe
        self.player2.moveDown()  # Jogador 2 desce

    def updateGame(self):
        # Move a bola
        self.ball.move()

        # Verifica colisões com as raquetes
        self.ball.handleCollision(self.player1)
        self.ball.handleCollision(self.player2)

        # Verifica se a bola saiu dos limites
        ball_x, ball_y = self.ball.get_position()
        if ball_x < 0:  # Pontuação para o Jogador 2
            self.score2.increment(1)
            print("Jogador 2 marcou ponto!")
            self.ball.reset()
        elif ball_x > 100:  # Pontuação para o Jogador 1
            self.score1.increment(1)
            print("Jogador 1 marcou ponto!")
            self.ball.reset()

        # Verifica colisão com as bordas superior e inferior
        if ball_y < 0 or ball_y > 50:
            self.ball.speedY = -self.ball.speedY

    def draw(self):
        # Exibe o estado atual do jogo no terminal
        ball_x, ball_y = self.ball.get_position()
        p1_x, p1_y = self.player1.get_position()
        p2_x, p2_y = self.player2.get_position()
        print(f"Posição da bola: ({ball_x}, {ball_y})")
        print(f"Jogador 1 (raquete): ({p1_x}, {p1_y})")
        print(f"Jogador 2 (raquete): ({p2_x}, {p2_y})")
        print(f"Pontuação: Jogador 1 - {self.score1.getValue()} | Jogador 2 - {self.score2.getValue()}")
        print("------")

    def gameLoop(self):
        print("Iniciando o jogo Pong...")
        while self.running:
            self.handleEvents()
            self.updateGame()
            self.draw()
            time.sleep(0.5)  # Simula o tempo entre as jogadas
