class Score:
    def __init__(self):
        self.value = 0

    def increment(self, color):
        # Verifica a cor e incrementa a pontuação com base nela
        points = 0
        if color == "Yellow":
            points = 1
        elif color == "Green":
            points = 3
        elif color == "Red":
            points = 7
        else:
            print(f"Cor desconhecida: {color}")

        self.value += points
        print(f"Bloco {color} destruído! {points} pontos adicionados. Pontuação total: {self.value}")

    def draw(self):
        # Simula exibição da pontuação (aqui é apenas uma mensagem)
        print(f"Pontuação atual: {self.value}")
