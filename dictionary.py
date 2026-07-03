class Parola:
    def __init__(self, parola,traduzione):
        self.parola = parola
        self.traduzioni = [traduzione]
    def __repr__(self):
        return f"{self.parola} {self.traduzioni}"






