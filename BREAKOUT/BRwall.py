class Wall:
    def __init__(self, thickness, color):
        self.thickness = thickness
        self.color = color

    def draw(self):
        print(f"Wall with thickness {self.thickness} and color {self.color}")

    def getBounds(self):
        # Simula bordas fictícias
        return [(0, 0, 800, self.thickness)]  # Exemplo
