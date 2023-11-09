# Final Project - Lottery Simulator
# Aaron Luciano (adlucian) and Dante Zucconi (dzucconi)
# CS021 / 11/25/2022 - 12/09/2022
# Simulate playing the lottery

import time
from bank import read_bank_amount
from menu_functions import get_menu_option
from menu_functions import get_lotto
from menu_functions import get_snack
from menu_functions import get_casino
from menu_functions import program_exit
from ticket_games import play_super_winner
from ticket_games import play_mini_scratch
from ticket_games import play_lotto_4
from ticket_games import play_big_bucket
from poker import play_poker
from roulette import play_roulette
from blackjack import play_blackjack
from constants import entry_amount
from constants import cola_price, hot_dog_price, chips_price, coffee_price
from constants import TITLE

def main(): #open bank.txt and read amount, display title and open main menu
    bank = read_bank_amount()
    print(TITLE)
    time.sleep(1.5)
    bank = entry_amount # need to read bank amonut from a file if file exists. if file doesnt exist, use entry amount
    menu = get_menu_option(bank)
    cont = True
    while cont == True:
        prev_snacked = False
        prev_lottoed = False
        prev_casino = False
        if menu != '1' and menu != '2' and menu != '3' and menu != '4':
            print('...Not sure what you mean by that, bud.')
            menu = get_menu_option(bank)
        if menu == '1': # prompts for lotto input and calls appropriate function
            if not prev_lottoed:
                lotto = get_lotto(bank)
            if lotto != '1' and lotto != '2' and lotto != '3' and lotto != '4' and lotto != '5':
                print("Oh! Sorry, we don't have that one in stock.\n")
                prev_lottoed = True
                lotto = get_lotto(bank)
            if lotto == '1':
                bank = play_super_winner(bank)
                print('\n')
                prev_lottoed = True
                lotto = get_lotto(bank)
            if lotto == '2':
                bank = play_mini_scratch(bank)
                print('\n')
                prev_lottoed = True
                lotto = get_lotto(bank)
            if lotto == '3':
                bank = play_lotto_4(bank)
                print('\n')
                prev_lottoed = True
                lotto = get_lotto(bank)
            if lotto == '4':
                bank = play_big_bucket(bank)
                print('\n')
                prev_lottoed = True
                lotto = get_lotto(bank)
            if lotto == '5':
                menu = get_menu_option(bank)
        if menu == '2': # prompts for snack input and charges bank balance
            if not prev_snacked:
                snack = get_snack(bank)
            if snack != '1' and snack != '2' and snack != '3' and snack != '4' and snack != '5':
                print("Hmm...Never heard of it. We've got what's on the menu.\n")
                time.sleep(2)
                prev_snacked = True
                snack = get_snack(bank)
            if snack == '1':
                bank -= cola_price
                print(f'\nBalance -${cola_price}')
                print('Mmm...Refreshing.\n')
                time.sleep(2)
                prev_snacked = True
                snack = get_snack(bank)
            if snack == '2':
                bank -= hot_dog_price
                print(f'\nBalance -${hot_dog_price}')
                print('That hot dog was delicious.\n')
                time.sleep(2)
                prev_snacked = True
                snack = get_snack(bank)
            if snack == '3':
                bank -= chips_price
                print(f'\nBalance -${chips_price}')
                print('A little greasy...but tasty nonetheless.\n')
                time.sleep(2)
                prev_snacked = True
                snack = get_snack(bank)
            if snack == '4':
                bank -= coffee_price
                print(f'\nBalance -${coffee_price}')
                print("Blehck. It's burnt.\n")
                time.sleep(2)
                prev_snacked = True
                snack = get_snack(bank)
            if snack == '5':
                menu = get_menu_option(bank)
        if menu == '3': # prompts for casino input and calls appropriate function
            if not prev_casino:
                casino = get_casino(bank)
            if casino != '1' and casino != '2' and casino != '3' and casino != '4':
                print("Excuse me? We got what we got.\n")
                prev_casino = True
                casino = get_casino(bank)
            if casino == '1':
                bank = play_blackjack(bank)
                print('\n')
                prev_casino = True
                casino = get_casino(bank)
            if casino == '2':
                bank = play_poker(bank)
                print('\n')
                prev_casino = True
                casino = get_casino(bank)
            if casino == '3':
                bank = play_roulette(bank)
                print('\n')
                prev_casino = True
                casino = get_casino(bank)
            if casino == '4':
                menu = get_menu_option(bank)
        if menu == '4':
            cont = program_exit(bank)
            if cont == True:
                menu = get_menu_option(bank)

# call main
main()