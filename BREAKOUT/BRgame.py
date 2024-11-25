from BRpaddle import Paddle
from BRball import Ball
from BRblock import Block
from BRscore import Score
import time
import random

class Game:
    def __init__(self):
        self.blocks = []
        self.paddle = Paddle(45, 95, 10, 1, 5)
        self.ball = Ball(random.randint(10, 90), random.randint(10, 50), 1, 1, 1)
        self.running = True
        self.score = Score()
        self.createBlocks()

    def createBlocks(self):
        colors = ["Red", "Yellow", "Green"]
        for i in range(3):
            for j in range(10):
                self.blocks.append(Block(j * 10, i * 3, 10, 3, colors[i]))

    def updateGame(self):
        self.paddle.autoMove(self.ball.x)
        self.ball.move()

        if self.ball.y > 100:
            print("The ball fell. Game over!")
            self.running = False
        else:
            if self.ball.handleCollision(self.paddle, self.blocks):
                block_color = self.blocks[-1].color if self.blocks else "Unknown"
                self.score.increment(block_color)

        if not self.blocks:
            print("You destroyed all the blocks! Congratulations!")
            self.running = False

    def draw(self):
        print(f"Ball: ({self.ball.x}, {self.ball.y}) | Paddle: ({self.paddle.x}, {self.paddle.y}) | Remaining blocks: {len(self.blocks)}")
        self.score.draw()

    def gameLoop(self):
        print("Game Starting...")
        while self.running:
            self.updateGame()
            self.draw()
            time.sleep(0.5)
        print(f"Final score: {self.score.value}")
