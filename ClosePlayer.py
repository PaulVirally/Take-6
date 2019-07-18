from Player import Player

class ClosePlayer(Player):
    
    def __init__(self, hand, name):
        super().__init__(hand, name)
        self.hand.sort()

    def play(self, table):
        distances = []
        for card in self.hand:
            card_distances = [card - row[-1] for row in table]
            filter(lambda x: x > 0, card_distances)
            if not card_distances:
                card_distances = float('inf')
            distances.append(min(card_distances))
        
        smallest = min(distances)
        if smallest == float('inf'):
            return self.hand.pop()

        return self.hand.pop(distances.index(smallest))