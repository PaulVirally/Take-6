import random
from Player import Player

class RandomPlayer(Player):

    def __init__(self, hand, name):
        super().__init__(hand, name)
        random.shuffle(self.hand)
    
    def play(self, table):
        return self.hand.pop()