from PONG.POball import Ball
from POpaddle import Paddle
from POscore import Score
import time

class Game:
    def __init__(self):
        self.ball = Ball(50, 25, 5, 5, 5)
        self.player1 = Paddle(5, 20, 5, 10, 2)
        self.player2 = Paddle(90, 20, 5, 10, 2)
        self.score1 = Score()
        self.score2 = Score()
        self.running = True

    def handleEvents(self):
        self.player1.moveUp()
        self.player2.moveDown()

    def updateGame(self):
        self.ball.move()

        self.ball.handleCollision(self.player1)
        self.ball.handleCollision(self.player2)

        ball_x, ball_y = self.ball.get_position()
        if ball_x < 0:  # player 2 score
            self.score2.increment(1)
            print("Jogador 2 marcou ponto!")
            self.ball.reset()
        elif ball_x > 100:  # player 2 score
            self.score1.increment(1)
            print("Jogador 1 marcou ponto!")
            self.ball.reset()

        # wall collision
        if ball_y < 0 or ball_y > 50:
            self.ball.speedY = -self.ball.speedY

    def draw(self):
        ball_x, ball_y = self.ball.get_position()
        p1_x, p1_y = self.player1.get_position()
        p2_x, p2_y = self.player2.get_position()
        print(f"""       x   y 
Bola: ({ball_x}, {ball_y})
P1:   ({p1_x}, {p1_y})
P2:   ({p2_x}, {p2_y})
Pontuação: P1 - {self.score1.getValue()} | P2 - {self.score2.getValue()}
{"-"*40}""")

    def gameLoop(self):
        print("Game starting...")
        while self.running:
            self.handleEvents()
            self.updateGame()
            self.draw()
            time.sleep(2)
