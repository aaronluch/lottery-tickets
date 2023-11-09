# roulette game function
import time
import random

def play_roulette(bank): # play roulette, return bank
    print(f'\n>>CURRENT BALANCE: ${bank:.2f}\n')
    print(' ' * 8 + '*' * 8 + '\n        Roulette\n' + ' ' * 8 + '*' * 8)
    print('\n Rules:\n - Slots are numbered 0-36\n - Even slots are red, odd slots are black\n - 0 slot is green\n - The riskier you bet, the higher the winnings!')
    print('\n\n')
    color_guess = -1
    while color_guess != 'b' and color_guess != 'r':
        print(' ' * 8 + 'Black or red (b/r)?')
        color_guess = input(' ' * 12 + '>>> ')
        if color_guess != 'b' and color_guess != 'r':
            print('Try again.')
    if color_guess == 'b':
        color_guess = 'Black'
    if color_guess == 'r':
        color_guess = 'Red'
    color_bet = bank + 1
    while color_bet > bank:
        try:
            print(' ' * 8 + 'Amount to bet on color:')
            color_bet = int(input(' ' * 12 + '>>> $'))
            if color_bet > bank:
                print('Insufficient funds.')
        except:
            print('Enter a number.')
            color_bet = bank + 1
    bank -= color_bet
    print(' ' * 8 + 'Bet on a number (y/n)?')
    bet_on_number = -1
    while bet_on_number != 'y' and bet_on_number != 'n':
        bet_on_number = input(' ' * 12 + '>>> ')
        if bet_on_number != 'y' and bet_on_number != 'n':
            print('Try again.')
    if bet_on_number == 'y':
        print(' ' * 8 + 'Pick your number:')
        num = -1
        while num < 0 or num > 36:
            num = int(input(' ' * 12 + '>>> '))
            if num < 0 or num > 36:
                print('Pick a number between 0 and 36')
        number_bet = bank + 1
        while number_bet > bank:
            try:
                print(' ' * 8 + 'Amount to bet on number:')
                number_bet = int(input(' ' * 12 + '>>> $'))
                if number_bet > bank:
                    print('Insufficient funds.')
            except:
                print('Enter a number.')
                number_bet = bank + 1
        bank -= number_bet
    num = -1
    number_bet = 0
    print("\nSpinning the wheel", end='')
    time.sleep(0.5)
    print(".", end='')
    time.sleep(0.5)
    print(".", end='')
    time.sleep(0.5)
    print(".\n", end='')
    time.sleep(0.5)
    print('\n')
    print("\nTossing the ball", end='')
    time.sleep(0.5)
    print(".", end='')
    time.sleep(0.5)
    print(".", end='')
    time.sleep(0.5)
    print(".\n", end='')
    time.sleep(1)
    print('\n')
    winning_num = random.randint(0, 36)
    if winning_num == 0:
        winning_color = 'Green'
    if winning_num % 2 == 0:
        winning_color = 'Red'
    if winning_num % 2 == 1:
        winning_color = 'Black'
    print('\n' + ' ' * 8 + f'The ball has landed on {winning_num} ({winning_color})!\n')
    earnings = 0
    if winning_num == num:
        earnings = bet_on_number * 36
    if winning_color == color_guess:
        earnings += color_bet * 1.9
    if winning_num == num and winning_color == color_guess:
        bank += earnings
        print(' ' * 8 + 'Jackpot!')
        print(' ' * 8 + f'Balance +${earnings - number_bet - color_bet:.2f}')
        time.sleep(3)
        return bank
    if winning_num == num and winning_color != color_guess:
        bank += earnings
        print(' ' * 8 + 'Big hit!')
        print(' ' * 8 + f'Balance +${earnings - color_bet:.2f}')
        time.sleep(3)
        return bank
    if winning_num != num and winning_color == color_guess:
        bank += earnings
        print(' ' * 8 + 'You Win!')
        print(' ' * 8 + f'Balance +${earnings - number_bet:.2f}')
        time.sleep(3)
        return bank
    else:
        print(' ' * 8 + 'You Lose.')
        print(' ' * 8 + f'Balance -${number_bet + color_bet:.2f}')
        time.sleep(3)
        return bank
