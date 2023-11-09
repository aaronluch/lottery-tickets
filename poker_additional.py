# additional functions for poker
# printing and formatting
import time
from poker_checks import check_two_pair
from poker_checks import check_poker_wins
from poker_checks import get_high_card
from constants import DECK_NAMES, DECK, POKER_WINS, WIN_STRENGTHS, DECK_VALUES

def print_flop(cards): # prints list of card names with a suspenseful delay
    print('Flop:')
    time.sleep(1)
    for i in cards:
        print(f'- {DECK_NAMES[i][0]}')
        time.sleep(1)


def win_chance_2(hand): # calculates and returns the strength of a hand with two cards
    if check_two_pair(hand):
        return 1
    else:
        return 0


def win_chance_5(hand): # calculates and returns the strength of a hand with five cards
    wins = check_poker_wins(hand)
    try:
        chance = WIN_STRENGTHS[wins[0]]
    except:
        chance = 0
    return chance

    
def get_player_bet(bank): # prompts for and returns raise
    player_bet = bank + 1
    while player_bet > bank:
        print('\nEnter your raise:')
        try:
           player_bet = int(input('>>> $'))
           if player_bet > bank:
               print("You don't have enough for that, pal.")
        except:
            print('Enter something valid...above zero? A number?')
    return player_bet


def get_dealer_move_r1(hand): # returns best dealer move and bet based on their hand, player move, and current bet for the first round of betting
    strength = win_chance_2(hand)
    high_card = get_high_card(hand)
    high_value = int(DECK_NAMES[high_card][3])
    if strength == 0:
        return 'c', 0
    if strength == 1:
        return 'r', 10
    if strength == 1 and high_value >= 11:
        return 'r', 20


def get_dealer_move_r2(hand, player_bet): # returns best dealer move and bet based on their hand, player move, and current bet for the first round of betting
    strength = win_chance_5(hand)
    if strength < 1 and player_bet <= 100:
        return 'c', 0
    if strength < 1 and player_bet > 100:
        return 'f', 0
    if strength >= 1 and strength <= 2:
        return 'r', 20
    if strength > 3:
        return 'r', 50


def display_player_win(pot, player_high_card, player_win): # displays player win
    if not not player_win:
        print(f'\nYou win with a {player_win[0]}!')
        print(' ' * 8 + f'Balance +${pot}')
        return
    if not player_win:
        print(f'\nYou win with a high card! The {DECK_NAMES[player_high_card][0]}!')
        print(' ' * 8 + f'Balance +${pot}')
        return


def display_dealer_win(pot, dealer_high_card, dealer_win): # displays dealer win
    if not not dealer_win:
        print(f'\nThe dealer wins with a {dealer_win[0]}.')
        print(' ' * 8 + f'Balance -${pot / 2}')
        return
    if not dealer_win:
        print(f'\nThe dealer wins with a high card, the {DECK_NAMES[dealer_high_card][0]}.')
        print(' ' * 8 + f'Balance -${int(pot / 2)}')
        return
