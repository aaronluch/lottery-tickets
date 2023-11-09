# poker's main function, pulling from a few other files
import time
from casino import get_shuffle
from casino import print_cards
from poker_additional import get_player_bet
from poker_additional import print_flop
from poker_additional import get_dealer_move_r2
from poker_additional import display_player_win
from poker_additional import display_dealer_win
from poker_additional import get_dealer_move_r1
from poker_checks import check_poker_wins
from poker_checks import get_high_card
from constants import DECK_NAMES, DECK, POKER_WINS, WIN_STRENGTHS, DECK_VALUES

def play_poker(bank): # plays poker, returns bank
    print(f'\n>>CURRENT BALANCE: ${bank:.2f}\n')
    print(' ' * 8 + '*' * 5 + "\n        Poker\n" + ' ' * 8 + '*' * 5)
    print('\n')
    print('Rules:')
    print('- Two rounds of betting')
    print('- Three cards in the flop')
    shuffle = get_shuffle(DECK)
    dealer = []
    player = []
    dealer.append(shuffle[0])
    dealer.append(shuffle[1])
    player.append(shuffle[2])
    player.append(shuffle[3])
    print("\nShuffling", end='')
    time.sleep(0.5)
    print(".", end='')
    time.sleep(0.5)
    print(".", end='')
    time.sleep(0.5)
    print(".\n", end='')
    time.sleep(1)
    print('\n')
    print_cards(player, 0)
    print('\n')
    player_move = -1
    while player_move != 'c' and player_move != 'r':
        print(f'\n>>CURRENT BALANCE: ${bank:.2f}\n')
        print('Check or raise? (c/r)?')
        player_move = input('>>> ')
        if player_move != 'c' and player_move != 'r':
            print('\nTry again.\n')
    if player_move == 'c':
        print('\nYou check.\n')
        player_bet = 0
    if player_move == 'r':
        player_bet = get_player_bet(bank)
        bank -= player_bet
    dealer_move, dealer_bet = get_dealer_move_r1(dealer)
    dealer_bet_1 = 0
    if dealer_move == 'c' and player_move == 'r':
        print('\nDealer has matched.\n')
        pot = int(player_bet * 2)
        print(f'Current pot: ${pot}')
    if dealer_move == 'c' and player_move == 'c':
        print('\nDealer has checked.\n')
        pot = int(player_bet + dealer_bet)
        print(f'Current pot: ${pot}')
    if dealer_move == 'r':
        dealer_bet_1 = dealer_bet
        print(f'\nDealer has raised by ${dealer_bet}.\n')
        player_move = -1
        while player_move != 'm' and player_move != 'f':
            print(f'\n>>CURRENT BALANCE: ${bank:.2f}\n')
            print('Match or fold? (m/f)?')
            player_move = input('>>> ')
            if player_move != 'm' and player_move != 'f':
                print('\nTry again.\n')
        if player_move == 'f':
            print('\nYou fold. Try again sometime, will ya?\n')
            print(' ' * 8 + f'Balance -${player_bet}')
            return bank
        if player_move == 'm' and bank < dealer_bet:
            print("\nYou don't have enough money for that!! Get outta here!")
            bank += player_bet
            return bank
        if player_move == 'm' and bank >= dealer_bet:
            bank -= dealer_bet
            pot = int(player_bet * 2 + dealer_bet * 2)
            print(f'\nCurrent pot: ${pot}')
    print('\n')
    flop = []
    flop.append(shuffle[4])
    flop.append(shuffle[5])
    flop.append(shuffle[6])
    for i in flop:
        dealer.append(i)
    print_flop(flop)
    print('\n')
    player_move = -1
    while player_move != 'c' and player_move != 'r':
        print(f'\n>>CURRENT BALANCE: ${bank:.2f}\n')
        print('Check or raise? (c/r)?')
        player_move = input('>>> ')
        if player_move != 'c' and player_move != 'r':
            print('\nTry again.\n')
    if player_move == 'c':
        print('\nYou check.\n')
        player_bet = 0
    if player_move == 'r':
        player_bet = get_player_bet(bank)
        bank -= player_bet
    dealer_move, dealer_bet = get_dealer_move_r2(dealer, player_bet)
    if dealer_move == 'f':
        print('\nDealer has folded. You win!\n')
        print(f'Current pot: ${pot}\n')
        print(' ' * 8 + f'Balance +${pot}')
        bank += pot
        return bank
    if dealer_move == 'c' and player_move == 'r':
        print('\nDealer has matched.\n')
        pot += int(player_bet * 2)
        print(f'Current pot: ${pot}')
    if dealer_move == 'c' and player_move == 'c':
        print('\nDealer has checked.\n')
        pot += int(player_bet + dealer_bet)
        print(f'Current pot: ${pot}')
    if dealer_move == 'r':
        print(f'\nDealer has raised by ${dealer_bet}.\n')
        player_move = -1
        while player_move != 'm' and player_move != 'f':
            print(f'\n>>CURRENT BALANCE: ${bank:.2f}\n')
            print('Match or fold? (m/f)?')
            player_move = input('>>> ')
            if player_move != 'm' and player_move != 'f':
                print('\nTry again.\n')
        if player_move == 'f':
            print('\nYou fold. Try again sometime, will ya?\n')
            print(' ' * 8 + f'Balance -${pot - dealer_bet_1}')
            time.sleep(2)
            return bank
        if player_move == 'm' and bank < dealer_bet:
            print("\nYou don't have enough money for that!! Get outta here!")
            bank += player_bet
            time.sleep(2)
            return bank
        if player_move == 'm' and bank >= dealer_bet:
            bank -= dealer_bet
            pot = int(player_bet * 2 + dealer_bet * 2)
            print(f'Current pot: ${pot}')
    dealer.pop(4)
    dealer.pop(3)
    dealer.pop(2)
    print('\nRevealing cards...\n')
    time.sleep(1)
    print_cards(dealer, 1)
    print('\n')
    time.sleep(1)
    print_cards(flop, 2)
    print('\n')
    time.sleep(1)
    print_cards(player, 0)
    print('\n')
    time.sleep(1)
    for i in flop:
        player.append(i)
        dealer.append(i)
    dealer_win = check_poker_wins(dealer)
    player_win = check_poker_wins(player)
    player_high_card = get_high_card(player)
    dealer_high_card = get_high_card(dealer)
    if not dealer_win and not player_win:
        if int(DECK_NAMES[player_high_card][3]) > int(DECK_NAMES[dealer_high_card][3]):
            display_player_win(pot, player_high_card, player_win)
            time.sleep(3)
            return bank
        if int(DECK_NAMES[player_high_card][3]) < int(DECK_NAMES[dealer_high_card][3]):
            display_dealer_win(pot, dealer_high_card, dealer_win)
            time.sleep(3)
            return bank
        if int(DECK_NAMES[player_high_card][3]) == int(DECK_NAMES[dealer_high_card][3]):
            print('\nA tie of high cards! What are the odds!\nIf this was a real casino, you would probably win. Too bad.\n')
            print(' ' * 8 + f'Balance -${pot / 2}')
            time.sleep(3)
            return bank
    if player_win and dealer_win:
        if player_win[0] == dealer_win[0]:
            if int(DECK_NAMES[player_high_card][3]) > int(DECK_NAMES[dealer_high_card][3]):
                print(f'Well, you both have a {player_win[0]}. But you have the high card, the {DECK_NAMES[player_high_card][0]}')
                print(' ' * 8 + f'Balance +${pot / 2}')
                time.sleep(3)
                return bank
            if int(DECK_NAMES[player_high_card][3]) <= int(DECK_NAMES[dealer_high_card][3]):
                print(f'Wow! You both have a {player_win[0]}! Yeah, sorry...this one is going to the house. You lose')
                print(' ' * 8 + f'Balance -${pot / 2}')
                time.sleep(3)
                return bank
    if player_win:
        display_player_win(pot, player_high_card, player_win)
        bank += pot
        time.sleep(3)
        return bank
    if dealer_win:
        display_dealer_win(pot, dealer_high_card, dealer_win)
        time.sleep(3)
        return bank

