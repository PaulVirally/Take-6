from Player import Player

class HeuristicBigPlayer(Player):

    def __init__(self, hand, name):
        super().__init__(hand, name)
        self.hand.sort()
    
    def play(self, table):
        table = table[:]

        if len(self.hand) == 1:
            return self.hand[0]

        card = self.hand[-1] # The card we want to play

        # Sort the table
        table.sort(key=lambda x: x[-1])
        row, row_idx = None, 0 # The row we play the card on
        for idx, r in enumerate(table):
            if r[-1] < card:
                row = r
                row_idx = idx
                break
        
        if row is None or len(row) < 5:
            return self.hand.pop()

        candidate_card = None
        candidate_dist = float('inf')
        fives = []
        for r in table[row_idx+1:]:
            if len(r) == 5:
                fives.append(r)
            else:
                c = [x for x in self.hand[:-1] if x > r[-1]] # Find the largest card for the row
                if c:
                    c = c[0]
                else:
                    continue
                dist = c - r[-1]
                if dist < candidate_dist:
                    candidate_dist = dist
                    candidate_card = c
        
        if candidate_card is None:
            if not fives:
                self.hand.pop()
                return card

            cards = []
            for c in self.hand[:-1]:
                for r in fives[::-1]:
                    if c > r[-1]:
                        dist = c - r[-1]
                        cards.append((c, dist))
                        break
            
            cards.sort(key=lambda x: x[1])
            if cards:
                return self.hand.pop(self.hand.index(cards[0][0]))
            return self.hand.pop()
        
        return self.hand.pop(self.hand.index(candidate_card))