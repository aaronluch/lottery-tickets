# general casino functions
import random
from constants import DECK_NAMES, DECK, POKER_WINS, WIN_STRENGTHS, DECK_VALUES

def get_shuffle(DECK): # returns shuffled deck list
    DECK = ['SA', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'SJ', 'SQ', 'SK',
            'CA', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'CJ', 'CQ', 'CK',
            'HA', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10', 'HJ', 'HQ', 'HK',
            'DA', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'DJ', 'DQ', 'DK'] 
    shuffle = []
    num = len(DECK)
    for i in range(num):
        index = random.randint(0, num - 1)
        shuffle.append(DECK[index])
        DECK.remove(DECK[index])
        num -= 1
    DECK = ['SA', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'SJ', 'SQ', 'SK',
            'CA', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'CJ', 'CQ', 'CK',
            'HA', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10', 'HJ', 'HQ', 'HK',
            'DA', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'DJ', 'DQ', 'DK'] 
    return shuffle


def get_names(cards): # returns list of card names
    names = []
    for i in cards:
        names.append(DECK_NAMES[i][0])
    return names

def print_cards(cards, whose): # prints list of card names. 0 = player,  1 = computer, 2 = flop
    if whose == 0:
        print('Your cards:')
    if whose == 1:
        print("Dealer's cards:")
    if whose == 2:
        print("Flop:")
    for i in cards:
        print(f'- {DECK_NAMES[i][0]}')
    

def get_sum(cards): # returns sum of card values
    total = 0
    for i in cards:
        total += int(DECK_NAMES[i][1])
    return total