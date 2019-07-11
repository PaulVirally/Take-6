class Player:

    def __init__(self, hand, name):
        self.hand = hand
        self.name = name

    def play(self, table):
        raise NotImplementedError