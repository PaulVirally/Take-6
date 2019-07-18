import random
import matplotlib.pyplot as plt
from BigPlayer import BigPlayer
from ClosePlayer import ClosePlayer
from HeuristicBigPlayer import HeuristicBigPlayer
from HeuristicSmallPlayer import HeuristicSmallPlayer
from RandomPlayer import RandomPlayer
from SmallPlayer import SmallPlayer

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

wins = [0, 0, 0, 0, 0, 0]
total_scores = [0, 0, 0, 0, 0, 0]

num_games = 1000000

for i in range(num_games):
    cards = random.sample(deck, 10*6 + 4)
    players = [RandomPlayer(cards[:10], 0),
               SmallPlayer(cards[10:20], 1),
               BigPlayer(cards[20:30], 2),
               HeuristicSmallPlayer(cards[30:40], 3),
               HeuristicBigPlayer(cards[40:50], 4),
               ClosePlayer(cards[50:60], 5)]
    scores = [0, 0, 0, 0, 0, 0]
    table = [[cards[50]], [cards[51]], [cards[52]], [cards[53]]]

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
    total_scores = [total_scores[x] + scores[x] for x in range(len(total_scores))]

plt.title('Strategy Distribution')

plt.subplot(2, 1, 1)
plt.ylabel('Win Percentage')
win_percs = [100*x/sum(wins) for x in wins]
plt.bar(range(6), win_percs, color='blue')
plt.xticks([])
for idx, win_perc in enumerate(win_percs):
    plt.text(idx, win_perc - 4, str(win_perc) + '%', color='white', horizontalalignment='center')

plt.subplot(2, 1, 2)
plt.ylabel('Average Score')
avg_scores = [x/num_games for x in total_scores]
plt.bar(['Random', 'Small', 'Big', 'HeuristicSmall', 'HeuristicBig', 'Close'], avg_scores, color='green')
for idx, avg_score in enumerate(avg_scores):
    plt.text(idx, avg_score - 3, str(avg_score), color='white', horizontalalignment='center')

plt.show()