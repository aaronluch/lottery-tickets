# all menu functions
import time
from constants import TITLE_1, TITLE_2, TITLE_3, TITLE_4, TITLE_5, TITLE_6, TITLE_7, TITLE_8, TITLE_9, TITLE
from constants import COUNTER_TITLE, CLERK, LOTTO_TIX, SNACK, CASINO

def get_menu_option(bank): # displays main menu and returns main menu input
    print(f'\n>>CURRENT BALANCE: ${bank:.2f}')
    time.sleep(0.9)
    print(COUNTER_TITLE)
    print(CLERK)
    print(' ' * 8 + '-' * 15)
    print(' ' * 8 + '1. Buy a lottery ticket')
    print(' ' * 8 + '2. Buy a snack')
    print(' ' * 8 + '3. Visit the back room...')
    print(' ' * 8 + '4. Cut your losses (Quit)')
    selection = input('\n     >>> ')
    return selection


def get_lotto(bank): # displays lotto menu and returns lotto menu input
    print(f'\n>>CURRENT BALANCE: ${bank:.2f}')
    print(LOTTO_TIX)
    print('\n')
    print(' ' * 8 + '1. Super Winner Deluxe')
    print(' ' * 8 + '2. Mini Scratch')
    print(' ' * 8 + '3. Lotto 4 Low')
    print(' ' * 8 + '4. Big Bucket Super Winner')
    print(' ' * 8 + '5. Back')
    selection = input('\n     >>> ')
    return selection


def get_snack(bank): # displays snack menu and returns snack menu input
    print(f'\n>>CURRENT BALANCE: ${bank:.2f}')
    print(SNACK)
    print('\n' + '     Menu:')
    print(' ' * 8 + '1. Cola')
    print(' ' * 8 + '2. Hot Dog')
    print(' ' * 8 + '3. Chips')
    print(' ' * 8 + '4. Coffee')
    print(' ' * 8 + '5. Back')
    selection = input('\n     >>> ')
    return selection


def get_casino(bank): # displays game menu and returns game menu input
    print(f'\n>>CURRENT BALANCE: ${float(bank):.2f}')
    print(CASINO)
    print(' ' * 8 + '1. Blackjack')
    print(' ' * 8 + "2. Poker")
    print(' ' * 8 + '3. Roulette')
    print(' ' * 8 + '4. Back')
    selection = input('\n     >>> ')
    return selection
    
def program_exit(bank): # asks if user wants to quit. if yes, write groceries.txt
    cont = input("\nWoah there! Are you sure you're done playing? (y/n)\n>>> ")
    if cont == 'y':
        try:
            with open('bank.txt','w') as f:
                file_bank = bank
                f.write(repr(file_bank))
        except:
            with open('bank.txt','a') as f:
                f.write(repr(bank))
        f.close()
        print('\nThanks for stopping by The Lotto Stand!')
        return False
    if cont == 'n':
        return True