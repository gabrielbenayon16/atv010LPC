from POball import Ball
from POpaddle import Paddle
import random
import time

class Game:
    def __init__(self):
        self.ball = Ball(25, 10, 1, 1, 1)
        self.paddle1 = Paddle(6, 10, 2, 5, 1)
        self.paddle2 = Paddle(46, 10, 2, 5, 1)
        self.score1 = 0
        self.score2 = 0

    def startGame(self):
        print("Game Starting...")
        self.ball.reset()
        self.paddle1.reset()
        self.paddle2.reset()

        while True:
            self.handleEvents()
            self.updateGame()
            self.checkCollisions()
            self.draw()

            time.sleep(2)

            self.paddle1.y += random.choice([-1, 1]) * self.paddle1.speed
            self.paddle2.y += random.choice([-1, 1]) * self.paddle2.speed

            self.ball.move()

            if self.score1 >= 2:
                print("P1 wins!")
                break
            elif self.score2 >= 2:
                print("P2 wins!")
                break

    def handleEvents(self):
        self.paddle1.y += random.choice([-1, 1]) * self.paddle1.speed
        self.paddle2.y += random.choice([-1, 1]) * self.paddle2.speed
        self.paddle1.y = max(0, min(self.paddle1.y, 20 - self.paddle1.height))
        self.paddle2.y = max(0, min(self.paddle2.y, 20 - self.paddle2.height))

    def updateGame(self):
        self.ball.move()

    def draw(self):
        print(
            f"Ball: ({self.ball.x}, {self.ball.y}) | P1: ({self.paddle1.x}, {self.paddle1.y}) | P2: ({self.paddle2.x}, "
            f"{self.paddle2.y})")
        print(f"Score: P1: {self.score1} | P2: {self.score2}")

    def checkCollisions(self):
        if self.ball.handleCollision(self.paddle1):
            print("Ball hits paddle1!")

        if self.ball.handleCollision(self.paddle2):
            print("Ball hits paddle2!")

        if self.ball.x <= 0:
            self.score2 += 1
            print("P2 score!")
            self.ball.reset()

        if self.ball.x >= 50:
            self.score1 += 1
            print("P1 score!")
            self.ball.reset()
