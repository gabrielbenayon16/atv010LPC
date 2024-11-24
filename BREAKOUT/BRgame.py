from BRpaddle import Paddle
from BRball import Ball
from BRblock import Block
from BRscore import Score  # Importa a nova classe Score
import time
import random

class Game:
    def __init__(self):
        self.blocks = []
        self.paddle = Paddle(45, 95, 10, 1, 5)
        self.ball = Ball(random.randint(10, 90), random.randint(10, 50), 1, 1, 1)
        self.running = True
        self.score = Score()  # Instancia o objeto Score
        self.createBlocks()

    def createBlocks(self):
        colors = ["Red", "Yellow", "Green"]  # Adicione outras cores, se necessário
        for i in range(3):  # Três linhas de blocos
            for j in range(10):  # Dez blocos por linha
                self.blocks.append(Block(j * 10, i * 3, 10, 3, colors[i]))

    def updateGame(self):
        self.paddle.autoMove(self.ball.x)
        self.ball.move()
        if self.ball.y > 100:
            print("A bola caiu. Fim de jogo!")
            self.running = False
        else:
            # Verifica colisão com a raquete e os blocos
            if self.ball.handleCollision(self.paddle, self.blocks):
                # Obtém a cor do bloco destruído
                block_color = self.blocks[-1].color if self.blocks else "Unknown"
                self.score.increment(block_color)  # Incrementa pontuação com base na cor
        if not self.blocks:
            print("Você destruiu todos os blocos! Parabéns!")
            self.running = False

    def draw(self):
        print(f"Bola: ({self.ball.x}, {self.ball.y}) | Raquete: ({self.paddle.x}, {self.paddle.y}) | Blocos restantes: {len(self.blocks)}")
        self.score.draw()  # Exibe a pontuação atual

    def gameLoop(self):
        print("Iniciando simulação do Breakout...")
        while self.running:
            self.updateGame()
            self.draw()
            time.sleep(0.5)  # Simula o tempo de jogo
        print(f"Pontuação final: {self.score.value}")  # Exibe a pontuação final
