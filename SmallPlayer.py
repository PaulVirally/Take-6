from Player import Player

class SmallPlayer(Player):

    def __init__(self, hand, name):
        super().__init__(hand, name)
        self.hand.sort(reverse=True)
    
    def play(self, table):
        return self.hand.pop()