# checking functions for playing poker
from constants import DECK_NAMES, DECK, POKER_WINS, WIN_STRENGTHS, DECK_VALUES

def get_high_card(hand): # checks for highest card in hand, return card code
    high_card = '00'
    for card in hand:
        if int(DECK_NAMES[card][3]) > int(DECK_NAMES[high_card][3]):
            high_card = card
    return high_card


def check_pair(hand): # checks for pairs in a hand,returns 2 cards, if none return False (does not check for 2 pair)
    pair = False
    for i in range(len(hand)):
        for j in range(len(hand)):
            if i != j:
                if DECK_NAMES[hand[i]][3] == DECK_NAMES[hand[j]][3]:
                    pair = hand[i], hand[j]
    return pair


def check_two_pair(hand): # checks for two pair, returns both pairs in a list, if none, return False
    pair = []
    for i in range(len(hand)):
        for j in range(len(hand)):
            if i == j:
                continue
            else:
                if DECK_NAMES[hand[i]][3] == DECK_NAMES[hand[j]][3]:
                    pair.append(hand[i])
                    pair.append(hand[j])
    if len(pair) == 8:
        pair.pop(4)
        pair.pop(4)
        pair.pop(4)
        pair.pop(4)
        return pair
    else:
        return False


def check_three_pair(hand): # checks for three of a kind, if none, return False
    three_pair = []
    for i in range(len(hand)):
        for j in range(len(hand)):
            for k in range(len(hand)):
                if i != j and j != k and i != k:
                    if DECK_NAMES[hand[i]][3] == DECK_NAMES[hand[j]][3] and DECK_NAMES[hand[j]][3] == DECK_NAMES[hand[k]][3]:
                        three_pair.append(hand[i])
                        three_pair.append(hand[j])
                        three_pair.append(hand[k])
    while len(three_pair) > 3:
        three_pair.pop(3)
    if len(three_pair) < 3:
        return False
    return three_pair


def check_straight(hand): # checks for straight and return hand, if none, return False
    hand_values = []
    for card in hand:
        hand_values.append(DECK_NAMES[card][3])
    hand_values.sort()
    for i in range(13):
        test_string = []
        for j in range(len(hand)):
            test_string.append(DECK_VALUES[i + j])
        test_string.sort()
        if test_string == hand_values:
            return hand
    return False


def check_flush(hand): # checks for flush and return hand, if none, return False
    suits = []
    for card in hand:
        suits.append(DECK_NAMES[card][2])
    if suits[0] == suits[1] and suits[1] == suits[2] and suits[2] == suits[3] and suits[3] == suits[4]:
        return hand
    else:
        return False


def check_full_house(hand): # checks for full house and returns hand, if none, return False
    three_pair = check_three_pair(hand)
    if not three_pair:
        return False
    pair = False
    for i in range(len(hand)):
        for j in range(len(hand)):
            if i != j and DECK_NAMES[hand[i]][3] != DECK_NAMES[three_pair[0]][3]:
                if DECK_NAMES[hand[i]][3] == DECK_NAMES[hand[j]][3]:
                    pair = hand[i], hand[j]
    if pair == False:
        return False
    return hand


def check_four_pair(hand): # checks for four of a kind and returns cards, if none, returns False
    four_pair = []
    for i in range(len(hand)):
        for j in range(len(hand)):
            for k in range(len(hand)):
                for s in range(len(hand)):
                    if i != j and i != k and i != s and j != k and j != s and k != s:
                        if DECK_NAMES[hand[i]][3] == DECK_NAMES[hand[j]][3] and \
                        DECK_NAMES[hand[j]][3] == DECK_NAMES[hand[k]][3] and DECK_NAMES[hand[k]][3] == DECK_NAMES[hand[s]][3]:
                            four_pair.append(hand[i])
                            four_pair.append(hand[j])
                            four_pair.append(hand[k])
                            four_pair.append(hand[s])                                                                                                                                         
    while len(four_pair) > 4:
        four_pair.pop(4)
    if len(four_pair) < 4:
        return False
    return four_pair


def check_straight_flush(hand): # checks for straight flush and returns hand, if none, returns False
    flush = check_flush(hand)
    straight = check_straight(hand)
    if flush and straight:
        return hand


def check_royal_flush(hand): # checks for royale flush and returns hand, if none, returns False this will never happen idk why im even adding it
    total = 0
    suits = []
    for card in hand:
        total += int(DECK_NAMES[card][3])
    if total != 60:
        return False
    for card in hand:
        suits.append(DECK_NAMES[card][2])
    if suits[0] == suits[1] and suits[1] == suits[2] and suits[2] == suits[3] and suits[3] == suits[4]:
        return hand
    else:
        return False


def check_poker_wins(hand): # calls functions to check for wins, returns string of wins with high card at index 0
    wins = []
    royal_flush = check_royal_flush(hand)
    if royal_flush:
        wins.append(POKER_WINS[0])
        return wins
    straight_flush = check_straight_flush(hand)
    if straight_flush:
        wins.append(POKER_WINS[1])
    four_pair = check_four_pair(hand)
    if four_pair:
        wins.append(POKER_WINS[2])
    full_house = check_full_house(hand)
    if full_house:
        wins.append(POKER_WINS[3])
    flush = check_flush(hand)
    if flush and not straight_flush:
        wins.append(POKER_WINS[4])
    straight = check_straight(hand)
    if straight and not straight_flush:
        wins.append(POKER_WINS[5])
    three_pair = check_three_pair(hand)
    if three_pair and not full_house and not four_pair:
        wins.append(POKER_WINS[6])
    two_pair = check_two_pair(hand)
    if two_pair:
        wins.append(POKER_WINS[7])
    pair = check_pair(hand)
    if pair and not two_pair and not three_pair and not full_house:
        wins.append(POKER_WINS[8])
    if not wins:
        wins = False
    return wins
