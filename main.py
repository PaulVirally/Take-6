import random
import matplotlib.pyplot as plt
from RandomPlayer import RandomPlayer
from SmallPlayer import SmallPlayer
from BigPlayer import BigPlayer
from HeuristicSmallPlayer import HeuristicSmallPlayer
from HeuristicBigPlayer import HeuristicBigPlayer

card_vals = []
for i in range(1, 105):
    if i == 55:
        card_vals.append(7)
    elif i % 11 == 0:
        card_vals.append(5)
    elif i % 10 == 0:
        card_vals.append(3)
    elif i % 5 == 0:
        card_vals.append(2)
    else:
        card_vals.append(1)

deck = list(range(1, 105))

wins = [0, 0, 0, 0, 0]
avg_scores = [0, 0, 0, 0, 0]
total_scores = [0, 0, 0, 0, 0]

for i in range(1000000):
    cards = random.sample(deck, 10*5 + 4)
    players = [RandomPlayer(cards[:10], 0),
               SmallPlayer(cards[10:20], 1),
               BigPlayer(cards[20:30], 2),
               HeuristicSmallPlayer(cards[30:40], 3),
               HeuristicBigPlayer(cards[40:50], 4)]
    scores = [0, 0, 0, 0, 0]
    table = [[cards[40]], [cards[41]], [cards[42]], [cards[43]]]

    for turn in range(10):
        to_play = sorted([(x.play(table), x.name) for x in players])

        for card, name in to_play:
            sorted_table = sorted(table, key=lambda x: x[-1], reverse=True)
            row = None
            for r in sorted_table:
                if r[-1] < card:
                    row = r
                    break

            if row is None:
                min_score = float('inf')
                min_row_idx = None
                for idx, r in enumerate(table):
                    score = sum([card_vals[x-1] for x in r])
                    if score < min_score:
                        min_score = score
                        min_row_idx = idx
                scores[name] += min_score
                table[min_row_idx] = [card]
                continue

            row_idx = table.index(row)

            if len(row) == 5:
                scores[name] += sum([card_vals[x-1] for x in table[row_idx]])
                table[row_idx] = [card]
                continue
            
            table[row_idx].append(card)
    
    min_index, _ = min(enumerate(scores), key=lambda x: x[1])
    wins[min_index] += 1
    avg_scores = [(avg_scores[x]*i + scores[x])/(i+1) for x in range(len(avg_scores))]
    total_scores = [total_scores[x] + scores[x] for x in range(len(total_scores))]

plt.title('Strategy Distribution')

plt.subplot(3, 1, 1)
plt.ylabel('Win Percentage')
plt.bar(range(5), [100*x/sum(wins) for x in wins], color='blue')
plt.xticks([])

plt.subplot(3, 1, 2)
plt.ylabel('Average Score')
plt.bar(range(5), avg_scores, color='green')
plt.xticks([])

plt.subplot(3, 1, 3)
plt.ylabel('Total Score')
plt.bar(['Random', 'Small', 'Big', 'HeuristicSmall', 'HeuristicBig'], total_scores, color='red')

plt.show()