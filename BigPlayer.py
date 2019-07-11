from Player import Player

class BigPlayer(Player):

    def __init__(self, hand, name):
        super().__init__(hand, name)
        self.hand.sort()
    
    def play(self, table):
        return self.hand.pop()