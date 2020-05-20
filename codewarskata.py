def score_hand(cards):
    point_list = []
    aces = 0
    #count the aces, deal with them later
    for card in cards:
        if card == 'A':
            aces += 1

    #put the cards in a new list with their point values, 'cept Aces
    for card in cards:
        try:
            new_card = int(card)
            point_list.append(new_card)
        except ValueError:
            if card == 'J' or card == 'K' or card == 'Q':
                point_list.append(10)
            else:
                pass

    #sum the total of points, excl. aces
    score = 0
    for num in point_list:
        score += num

    #scoring logic
    if aces == 0:
        return score
    elif score <= 10 and aces == 1:
        score += 11
    elif score > 10 and aces == 1:
        score += 1
    elif score <= 9 and aces == 2:
        score += 12
    elif score > 9 and aces == 2:
        score += 2
    elif score <= 8 and aces == 3:
        score += 13
    elif score > 8 and aces == 3:
        score += 3
    elif score <= 7 and aces == 4:
        score += 14
    elif score > 7 and aces == 4:
        score += 4

    return score

score_hand(['2', '3'])
score_hand(['7', '7', '8'])
score_hand(['4', '7', '8'])
score_hand(['K', 'J', 'Q'])
score_hand(['A', '3'])
score_hand(['A', 'A'])
score_hand(['A', '2', 'A', '9', '9'])