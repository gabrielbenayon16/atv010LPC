class Block:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.destroyed = False  # Status para saber se o bloco foi destruído

    def get_position(self):
        return self.x, self.y, self.width, self.height

    def collides_with(self, ball_x, ball_y, ball_size):
        """
        Verifica se a bola colidiu com o bloco.
        """
        if (self.x <= ball_x <= self.x + self.width and
                self.y <= ball_y <= self.y + self.height):
            return True
        return False
