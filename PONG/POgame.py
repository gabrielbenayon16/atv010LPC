# game.py
import random
import time
from POball import Ball
from POpaddle import Paddle

class Game:
    def __init__(self):
        self.ball = Ball(25, 10, 1, 1, 1)  # Tamanho e velocidade da bola ajustados
        self.paddle1 = Paddle(5, 10, 6, 1, 1)  # Raquete 1 (lado esquerdo, posição x=5)
        self.paddle2 = Paddle(45, 10, 6, 1, 1)  # Raquete 2 (lado direito, posição x=45)
        self.score1 = 0  # Pontuação jogador 1
        self.score2 = 0  # Pontuação jogador 2

    def startGame(self):
        print("Jogo iniciado.")
        self.ball.reset()
        self.paddle1.reset()
        self.paddle2.reset()

        # O jogo roda indefinidamente até que um jogador ganhe
        while True:
            self.handleEvents()  # Atualiza a posição das raquetes
            self.updateGame()  # Atualiza a posição da bola
            self.checkCollisions()  # Verifica as colisões
            self.draw()  # Mostra a situação no terminal

            # Aguarda 2 segundos para a próxima atualização
            time.sleep(2)

            # Simula movimentos aleatórios para as raquetes no eixo y
            self.paddle1.y += random.choice([-1, 1]) * self.paddle1.speed
            self.paddle2.y += random.choice([-1, 1]) * self.paddle2.speed

            # Faz a bola se mover
            self.ball.move()

            # Verifica se algum jogador atingiu 2 pontos
            if self.score1 >= 2:
                print("Jogador 1 ganhou o jogo!")
                break
            elif self.score2 >= 2:
                print("Jogador 2 ganhou o jogo!")
                break

    def handleEvents(self):
        # Simula o movimento das raquetes (movendo aleatoriamente no eixo y)
        self.paddle1.y += random.choice([-1, 1]) * self.paddle1.speed
        self.paddle2.y += random.choice([-1, 1]) * self.paddle2.speed

        # Limita a raquete dentro da tela
        self.paddle1.y = max(0, min(self.paddle1.y, 20 - self.paddle1.height))
        self.paddle2.y = max(0, min(self.paddle2.y, 20 - self.paddle2.height))

    def updateGame(self):
        # Atualiza o estado do jogo (posição da bola e raquete)
        self.ball.move()

    def draw(self):
        print(
            f"Bola: ({self.ball.x}, {self.ball.y}) | Raquete 1: ({self.paddle1.x}, {self.paddle1.y}) | Raquete 2: ({self.paddle2.x}, {self.paddle2.y})")
        print(f"Pontuação atual: Jogador 1: {self.score1} | Jogador 2: {self.score2}")

    def checkCollisions(self):
        # Colisão com a raquete 1
        if self.ball.handleCollision(self.paddle1):
            print("Bola bateu na Raquete 1!")

        # Colisão com a raquete 2
        if self.ball.handleCollision(self.paddle2):
            print("Bola bateu na Raquete 2!")

        # Colisão com as paredes
        if self.ball.x <= 0:
            self.score2 += 1
            print("A bola passou pela Raquete 1! Pontuação Jogador 2 +1!")
            self.ball.reset()

        if self.ball.x >= 50:
            self.score1 += 1
            print("A bola passou pela Raquete 2! Pontuação Jogador 1 +1!")
            self.ball.reset()
