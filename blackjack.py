# function for playing the blackjack game
import time
from casino import get_shuffle
from casino import get_names
from casino import print_cards
from casino import get_sum
from constants import DECK_NAMES, DECK, POKER_WINS, WIN_STRENGTHS, DECK_VALUES

def play_blackjack(bank): #plays blackjack and return bank
    print(f'\n>>CURRENT BALANCE: ${bank:.2f}\n')
    print(' ' * 8 + '*' * 9 + '\n        Blackjack\n' + ' ' * 8 + '*' * 9)
    print('\nRules:')
    print('- Aces are low')
    print('- Aim for 21!\n')
    time.sleep(1.5)
    bet = bank + 1
    while bet > bank:
        print('\n' + ' ' * 8 + 'Enter your bet:')
        try:
            bet = int(input(' ' * 8 + '>>> $'))
            if bet > bank:
                print("You don't have enough for that, pal.")
        except:
            print("\nC'mon...Enter something valid.")
    DECK = ['SA', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'SJ', 'SQ', 'SK',
            'CA','C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'CJ', 'CQ', 'CK',
            'HA', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10', 'HJ', 'HQ', 'HK',
            'DA', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'DJ', 'DQ', 'DK'] 
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
    print_cards(dealer, 1)
    print('\n')
    print_cards(player, 0)
    cont = True
    index = 4
    while cont:
        action = -1
        while action != 'h' and action != 's':
            action = input('\nHit or stand (h/s)?\n>>> ')
        if action == 's':
            cont = False
        else:
            player.append(shuffle[index])
            print(f'\n** You drew the {DECK_NAMES[shuffle[index]][0]} **\n')
            time.sleep(0.5)
            index += 1
            print_cards(dealer, 1)
            print('\n')
            print_cards(player, 0)
            total = get_sum(player)
            if total >= 21:
                cont = False
    total = get_sum(player)
    if total > 21:
        print('\nBust. The house always wins.\n')
        print(f'Balance -${bet}')
        time.sleep(3)
        bank -= bet
        return bank
    if total == 21:
        print('\nBlackjack!\n')
        print(f'Balance +${bet}')
        time.sleep(3)
        bank += bet
    if total < 21:
        cont = True
        while cont:
            dealer_total = get_sum(dealer)
            if dealer_total < 17:
                dealer.append(shuffle[index])
                print(f'\n** Dealer drew the {DECK_NAMES[shuffle[index]][0]} **\n')
                time.sleep(1)
                index += 1
            if dealer_total >= 17 and total > dealer_total:
                dealer.append(shuffle[index])
                print(f'\n** Dealer drew the {DECK_NAMES[shuffle[index]][0]} **\n')
                time.sleep(1)
                index += 1
            if dealer_total >= 17 and total <= dealer_total:
                cont = False
        dealer_total = get_sum(dealer)
        if dealer_total < total:
            print_cards(dealer, 1)
            print('\n')
            print_cards(player, 0)
            print('\nYou win!\n')
            print(f'Balance +${bet}')
            time.sleep(3)
            bank += bet
            return bank
        if dealer_total > 21:
            print_cards(dealer, 1)
            print('\n')
            print_cards(player, 0)
            print('\nDealer bust. You win!\n')
            print(f'Balance +${bet}')
            time.sleep(3)
            bank += bet
            return bank
        if dealer_total == 21:
            print_cards(dealer, 1)
            print('\n')
            print_cards(player, 0)
            print('\nDealer hit 21. You lose.\n')
            print(f'Balance -${bet}')
            time.sleep(3)
            bank -= bet
            return bank
        if dealer_total == total:
            print_cards(dealer, 1)
            print('\n')
            print_cards(player, 0)
            print('\nTie game. The house wins.\n')
            print(f'Balance -${bet}')
            time.sleep(3)
            bank -= bet
            return bank
        if dealer_total > total:
            print_cards(dealer, 1)
            print('\n')
            print_cards(player, 0)
            print('\nGood try. The house wins.\n')
            print(f'Balance -${bet}')
            time.sleep(3)
            bank -= bet
            return bank

