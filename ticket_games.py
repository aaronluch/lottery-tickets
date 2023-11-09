# all lottery ticket games' functions for each respective game
import time
import random

def play_super_winner(bank): # plays super winner and returns bank balance
    print('\nInsert Super Winner Deluxe!',end=''), time.sleep(.5), print('.',end=''), time.sleep(.5), print('.',end=''), time.sleep(.5), print('.\n')
    if bank >= 10:
        bank -= 10
    else:
        print("Woah there... You haven't got enough funds for that!")
        time.sleep(1)
        input("Press enter to return.\n")
        return bank
    print('Match 1 Number = 5$')
    print('Match 2 Numbers = 12$')
    print('Match 3 Numbers = Win up to 1,200$!\n')
    time.sleep(1)
    print(f'~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(f'/|------------------------|\\')
    print(f'\|   [1] [2] [3] [4] [5]  |/')
    print(f'/|   [6] [7] [8] [9] [10] |\\')
    print(f'\|     Winning Numbers    |/')
    print(f'/|       [*] [*] [*]      |\\')
    print(f'\|------------------------|/')
    print(f'~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
    time.sleep(1)
    winning_numbers = []
    random_card_numbers = []
    i = 0
    while i != 10:
        num = random.randint(1,10)
        if num not in random_card_numbers:
            random_card_numbers.append(num)
            i += 1
        else: 
            i = i
    k = 0
    while k != 3:
        win_num = random.randint(1,10)
        if win_num not in winning_numbers:
            winning_numbers.append(win_num)
            k += 1
        else:
            k = k
    t1 = 0
    while t1 != 1:  
        scratch1 = input("Select the first space to scratch: (1 - 10)\n\t>>> ")
        scratch1 = (int(scratch1))
        if scratch1 not in range (1,11):
            print("Select a valid number! (1 - 10)\n")
            t1 = 0
        else:
            t1 = 1
    t2 = 0
    while t2 != 1:  
        scratch2 = input("Select the second space to scratch: (1 - 10)\n\t>>> ")
        scratch2 = (int(scratch2))
        if scratch2 not in range (1,11):
            print("Select a valid number! (1 - 10)\n")
            t1 = 0
        elif scratch2 == scratch1:
            print("Number already selected! Input a different number.\n")
            t2 = 0
        else:
            t2 = 1
    t3 = 0
    while t3 != 1:
        scratch3 = input("Select the third space to scratch: (1 - 10)\n\t>>> ")
        scratch3 = (int(scratch3))
        if scratch3 not in range (1,11):
            print("Select a valid number! (1 - 10)\n")
            t3 = 0
        elif scratch3 == scratch1 or scratch3 == scratch2:
            print("Number already selected! Input a different number.\n")
            t3 = 0
        else:
            t3 = 1
    scratch1 = (int(scratch1) - 1)
    scratch2 = (int(scratch2) - 1)
    scratch3 = (int(scratch3) - 1)
    card_scratch1 = random_card_numbers[scratch1-1]
    card_scratch2 = random_card_numbers[scratch2-1]
    card_scratch3 = random_card_numbers[scratch3-1]
    spots = ['*','*','*','*','*','*','*','*','*','*']
    spots[scratch1] = card_scratch1
    spots[scratch2] = card_scratch2
    spots[scratch3] = card_scratch3
    time.sleep(.7)
    print(f'~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(f'/|------------------------|\\')
    print(f'\|   [{spots[0]}] [{spots[1]}] [{spots[2]}] [{spots[3]}] [{spots[4]}]  |/')
    print(f'/|   [{spots[5]}] [{spots[6]}] [{spots[7]}] [{spots[8]}] [{spots[9]}] |\\')
    print(f'\|     Winning Numbers    |/')
    print(f'/|       [{winning_numbers[0]}] [{winning_numbers[1]}] [{winning_numbers[2]}]      |\\')
    print(f'\|------------------------|/')
    print(f'~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    winning_amount = 0
    matched_numbers = 0
    if card_scratch1 in winning_numbers or card_scratch2 in winning_numbers or card_scratch3 in winning_numbers:
        winning_amount = 5
        matched_numbers = 1
    else:
        pass
    if matched_numbers == 1:
        if card_scratch1 in winning_numbers and card_scratch2 in winning_numbers:
            winning_amount = 12
            matched_numbers = 2
    else:
        pass
    if matched_numbers == 1:
        if card_scratch1 in winning_numbers and card_scratch3 in winning_numbers:
            winning_amount = 12
            matched_numbers = 2
    else:
        pass
    if matched_numbers == 1:
        if card_scratch2 in winning_numbers and card_scratch3 in winning_numbers:
            winning_amount = 12
            matched_numbers = 2
    else:
        pass
    if matched_numbers == 2:
        if card_scratch1 in winning_numbers and card_scratch2 in winning_numbers and card_scratch3 in winning_numbers:
            random_jackpot = random.randint(10,100)
            winning_amount = winning_amount * random_jackpot
            matched_numbers = 3
    time.sleep(1)
    if matched_numbers == 0:
        print("Sorry... Maybe try another?")
    if matched_numbers == 1:
        print(f'You have won ${winning_amount:.2f}')
        bank += winning_amount
    if matched_numbers == 2:
        print(f'Congratulations! You won ${winning_amount:.2f}')
        bank += winning_amount
    if matched_numbers == 3:
        print(f'Woah! You won a grand total of ${winning_amount:.2f}!')
        bank += winning_amount
    print(f'The winning numbers were: {winning_numbers}')
    print(f'You scratched: [{card_scratch1}, {card_scratch2}, {card_scratch3}]')
    time.sleep(1)
    input("\nPress Enter to continue...")
    return bank


def play_mini_scratch(bank): # plays mini scratch and returns bank balance
    if bank >= 1:
        bank -= 1
    else:
        print("Woah there... You haven't got enough funds for that!")
        time.sleep(1)
        input("Press enter to return.")
        return bank
    print('\nInsert Mini Scratch Game',end=''), time.sleep(.5), print('.',end=''), time.sleep(.5), print('.',end=''), time.sleep(.5), print('.')
    time.sleep(1)
    print("Scratch your three numbers and test your luck!")
    time.sleep(1)
    print(f'\n|-----------------|')
    print(f'|   [1] [2] [3]   |')
    print(f'| Winning Numbers |')
    print(f'|   [*] [*] [*]   |')
    print(f'|-----------------|\n')
    winning_numbers = []
    random_card_numbers = []
    i = 0
    while i != 3:
        num = random.randint(1,9)
        if num not in random_card_numbers:
            random_card_numbers.append(num)
            i += 1
        else: 
            i = i
    k = 0
    while k != 3:
        win_num = random.randint(1,9)
        if win_num not in winning_numbers:
            winning_numbers.append(win_num)
            k += 1
        else:
            k = k
    t1 = 0
    while t1 != 1:  
        scratch1 = input("Select the first space to scratch: (1 - 3)\n\t>>> ")
        scratch1 = (int(scratch1))
        if scratch1 not in range (1,4):
            print("Select a valid number! (1 - 3)\n")
            t1 = 0
        else:
            t1 = 1
    t2 = 0
    while t2 != 1:  
        scratch2 = input("Select the second space to scratch: (1 - 3)\n\t>>> ")
        scratch2 = (int(scratch2))
        if scratch2 not in range (1,4):
            print("Select a valid number! (1 - 3)\n")
            t1 = 0
        elif scratch2 == scratch1:
            print("Number already selected! Input a different number.\n")
            t2 = 0
        else:
            t2 = 1
    t3 = 0
    while t3 != 1:
        scratch3 = input("Select the third space to scratch: (1 - 3)\n\t>>> ")
        scratch3 = (int(scratch3))
        if scratch3 not in range (1,4):
            print("Select a valid number! (1 - 3)")
            t3 = 0
        elif scratch3 == scratch1 or scratch3 == scratch2:
            print("Number already selected! Input a different number.")
            t3 = 0
        else:
            t3 = 1
    scratch1 = (int(scratch1) - 1)
    scratch2 = (int(scratch2) - 1)
    scratch3 = (int(scratch3) - 1)
    card_scratch1 = random_card_numbers[scratch1-1]
    card_scratch2 = random_card_numbers[scratch2-1]
    card_scratch3 = random_card_numbers[scratch3-1]
    winning_amount = 0
    matched_numbers = 0
    spots = ['*','*','*','*','*','*','*','*','*']
    spots[scratch1] = card_scratch1
    spots[scratch2] = card_scratch2
    spots[scratch3] = card_scratch3
    time.sleep(.7)
    # evaluates winning amount
    if card_scratch1 in winning_numbers or card_scratch2 in winning_numbers or card_scratch3 in winning_numbers:
        winning_amount = 1
        matched_numbers = 1
    else:
        pass
    if matched_numbers == 1:
        if card_scratch1 in winning_numbers and card_scratch2 in winning_numbers:
            winning_amount = 3
            matched_numbers = 2
    else:
        pass
    if matched_numbers == 1:
        if card_scratch1 in winning_numbers and card_scratch3 in winning_numbers:
            winning_amount = 3
            matched_numbers = 2
    else:
        pass
    if matched_numbers == 1:
        if card_scratch2 in winning_numbers and card_scratch3 in winning_numbers:
            winning_amount = 3
            matched_numbers = 2
    else:
        pass
    if matched_numbers == 2:
        if card_scratch1 in winning_numbers and card_scratch2 in winning_numbers and card_scratch3 in winning_numbers:
            winning_amount = winning_amount * 3
            matched_numbers = 3
    time.sleep(1)
    print(f'\n|-----------------|')
    print(f'|   [{spots[0]}] [{spots[1]}] [{spots[2]}]   |')
    print(f'| Winning Numbers |')
    print(f'|   [{winning_numbers[0]}] [{winning_numbers[1]}] [{winning_numbers[2]}]   |')
    print(f'|-----------------|\n')
    if winning_amount <= 1:
        print("Sorry... you lost. (Need to match at least 2 numbers!)")
    if winning_amount > 1:
        print(f'Congratulations! You won ${winning_amount:.2f}')
        bank += winning_amount
    print(f'The winning numbers were: {winning_numbers}')
    print(f'You scratched: [{card_scratch1}, {card_scratch2}, {card_scratch3}]')
    time.sleep(1)
    input("\nPress Enter to continue...")
    return bank

def play_lotto_4(bank): # plays lotto 4 low and returns bank balance
    if bank >= 20:
        bank -= 20
    else:
        print("Woah there... You haven't got enough funds for that!")
        time.sleep(1)
        input("Press enter to return.")
        return bank
    print('\nInsert Lotto 4 Low Game',end=''), time.sleep(.5), print('.',end=''), time.sleep(.5), print('.',end=''), time.sleep(.5), print('.',end='')
    time.sleep(.5)
    print("\nScratch 3 numbers like you would in tic-tac-toe.")
    print(f'\n$*******************$')
    print(f'$|-----------------|$')
    print(f'$|   [1] [2] [3]   |$')
    print(f'$|   [4] [5] [6]   |$')
    print(f'$|   [7] [8] [9]   |$')
    print(f'$| Winning Numbers |$')
    print(f'$|   [*] [*] [*]   |$')
    print(f'$|-----------------|$')
    print(f'$*******************$\n')
    time.sleep(1)
    bank -= 20
    winning_numbers = []
    random_card_numbers = []
    i = 0
    while i != 9:
        num = random.randint(1,9)
        if num not in random_card_numbers:
            random_card_numbers.append(num)
            i += 1
        else: 
            i = i
    k = 0
    while k != 3:
        win_num = random.randint(1,9)
        if win_num not in winning_numbers:
            winning_numbers.append(win_num)
            k += 1
        else:
            k = k
    t1 = 0
    while t1 != 1:  
        scratch1 = input("Select the first space to scratch: (1 - 9)\n\t>>> ")
        scratch1 = (int(scratch1))
        if scratch1 not in range (1,10):
            print("Select a valid number! (1 - 9)\n")
            t1 = 0
        else:
            t1 = 1
    t2 = 0
    while t2 != 1:
        scratch2 = input("Select the second space to scratch: (1 - 9)\n\t>>> ")
        scratch2 = (int(scratch2))
        if scratch1 == 1:
            if scratch2 == 2 or scratch2 == 3 or scratch2 == 4 or scratch2 == 7 or scratch2 == 5:
                t2 = 1
            else:
                print("Select a proper number like you were playing on a tic-tac-toe board!\n")
                t2 = 0     
        
        elif scratch1 == 2:
            if scratch2 == 5 or scratch2 == 8:
                t2 = 1
            else:
                print("Select a proper number like you were playing on a tic-tac-toe board!\n")
                t2 = 0  

        elif scratch1 == 3:
            if scratch2 == 2 or scratch2 == 1 or scratch2 == 5 or scratch2 == 7 or scratch2 == 6 or scratch2 == 9:
                t2 = 1
            else:
                print("Select a proper number like you were playing on a tic-tac-toe board!\n")
                t2 = 0  
        
        elif scratch1 == 4:
            if scratch2 == 5 or scratch2 == 6:
                t2 = 1
            else:
                print("Select a proper number like you were playing on a tic-tac-toe board!\n")
                t2 = 0  
        
        elif scratch1 == 5:
            if scratch2 == 1 or scratch2 == 2 or scratch2 == 3 or scratch2 == 4 or scratch2 == 5 or scratch2 == 6 or scratch2 == 7 or scratch2 == 8 or scratch2 == 9:
                t2 = 1
            else:
                print("Select a proper number like you were playing on a tic-tac-toe board!\n")
                t2 = 0  
        
        elif scratch1 == 6:
            if scratch2 == 3 or scratch2 == 9 or scratch2 == 5 or scratch2 == 4:
                t2 = 1
            else:
                print("Select a proper number like you were playing on a tic-tac-toe board!\n")
                t2 = 0  
        
        elif scratch1 == 7:
            if scratch2 == 4 or scratch2 == 1 or scratch2 == 5 or scratch2 == 3 or scratch2 == 8 or scratch2 == 9:
                t2 = 1
            else:
                print("Select a proper number like you were playing on a tic-tac-toe board!\n")
                t2 = 0  
        
        elif scratch1 == 8:
            if scratch2 == 7 or scratch2 == 5 or scratch2 == 2 or scratch2 == 9:
                t2 = 1
            else:
                print("Select a proper number like you were playing on a tic-tac-toe board!\n")
                t2 = 0  
        
        elif scratch1 == 9:
            if scratch2 == 6 or scratch2 == 3 or scratch2 == 5 or scratch2 == 1 or scratch2 == 8 or scratch2 == 7:
                t2 = 1
            else:
                print("Select a proper number like you were playing on a tic-tac-toe board!\n")
                t2 = 0  
       
        elif scratch2 == scratch1:
            print("Number already selected! Input a different number.\n")
            t2 = 0

        elif scratch2 not in range (1,10):
            print("Select a valid number! (1 - 9)\n")
            t2 = 0
        
        else:
            t2 = 1
    
    scratch1 = (int(scratch1))
    scratch2 = (int(scratch2))        
    t3 = 0
    while t3 != 1:
        scratch3 = input("Select the third space to scratch: (1 - 9)\n\t>>> ")
        scratch3 = (int(scratch3))
        if scratch1 == 1:
            if scratch2 == 5 or scratch2 == 9:
                if scratch3 != scratch2:
                    if scratch3 == 5 or scratch3 == 9:
                        t3 = 1
            elif scratch2 == 4 or scratch2 == 7:
                if scratch3 != scratch2:
                    if scratch3 == 4 or scratch3 == 7:
                        t3 = 1       
            elif scratch2 == 2 or scratch2 == 3:
                if scratch3 != scratch2:
                    if scratch3 == 2 or scratch3 == 3:
                        t3 = 1                            
            else:
                print("Select a proper number like you were playing on a tic-tac-toe board!\n")
                t3 = 0  

        elif scratch1 == 3:
            if scratch2 == 2 or scratch2 == 1:
                if scratch3 != scratch2:
                    if scratch3 == 1 or scratch3 == 2:
                        t3 = 1
            elif scratch2 == 5 or scratch2 == 7:
                if scratch3 != scratch2:
                    if scratch3 == 7 or scratch3 == 5:
                        t3 = 1
            elif scratch2 == 6 or scratch2 == 9:
                if scratch3 != scratch2:
                    if scratch3 == 9 or scratch3 == 6:
                        t3 = 1            
            else:
                print("Select a proper number like you were playing on a tic-tac-toe board!\n")
                t3 = 0  
        
        elif scratch1 == 4:
            if scratch2 == 5 or scratch2 == 6:
                if scratch3 != scratch2:
                    if scratch3 == 5 or scratch3 == 6:
                        t3 = 1
            else:
                print("Select a proper number like you were playing on a tic-tac-toe board!\n")
                t3 = 0  
        
        elif scratch1 == 5:
            if scratch2 == 1 or scratch2 == 2 or scratch2 == 3 or scratch2 == 4 or scratch2 == 6 or scratch2 == 7 or scratch2 == 8 or scratch2 == 9:
                if scratch3 != scratch2:
                    if scratch3 == 1 or scratch3 == 2 or scratch3 == 3 or scratch3 == 4 or scratch3 == 6 or scratch3 == 7 or scratch3 == 8 or scratch3 == 9:
                        t3 = 1
            else:
                print("Select a proper number like you were playing on a tic-tac-toe board!\n")
                t3 = 0  
       
        elif scratch1 == 6:
            if scratch2 == 5 or scratch2 == 4:
                if scratch3 != scratch2:
                    if scratch3 == 5 or scratch3 == 4:
                        t3 = 1
            elif scratch2 == 3 or scratch2 == 9:
                if scratch3 != scratch2:
                    if scratch3 == 3 or scratch3 == 9:
                        t3 = 1
            else:
                print("Select a proper number like you were playing on a tic-tac-toe board!\n")
                t3 = 0  

        elif scratch1 == 7:
            if scratch2 == 5 or scratch2 == 3:
                if scratch3 != scratch2:
                    if scratch3 == 5 or scratch3 == 3:
                        t3 = 1
            elif scratch2 == 8 or scratch2 == 9:
                if scratch3 != scratch2:
                    if scratch3 == 8 or scratch3 == 9:
                        t3 = 1
            elif scratch2 == 1 or scratch2 == 4:
                if scratch3 != scratch2:
                    if scratch3 == 1 or scratch3 == 4:
                        t3 = 1
            else:
                print("Select a proper number like you were playing on a tic-tac-toe board!\n")
                t3 = 0  

        elif scratch1 == 8:
            if scratch2 == 7 or scratch2 == 9:
                if scratch3 != scratch2:
                    if scratch3 == 7 or scratch3 == 9:
                        t3 = 1
            elif scratch2 == 2 or scratch2 == 5:
                if scratch3 != scratch2:
                    if scratch3 == 2 or scratch3 == 5:
                        t3 = 1
            else:
                print("Select a proper number like you were playing on a tic-tac-toe board!\n")
                t3 = 0  

        elif scratch1 == 9:
            if scratch2 == 5 or scratch2 == 1:
                if scratch3 != scratch2:
                    if scratch3 == 5 or scratch3 == 1:
                        t3 = 1
            elif scratch2 == 8 or scratch2 == 7:
                if scratch3 != scratch2:
                    if scratch3 == 8 or scratch3 == 7:
                        t3 = 1
            elif scratch2 == 3 or scratch2 == 6:
                if scratch3 != scratch2:
                    if scratch3 == 3 or scratch3 == 6:
                        t3 = 1
            else:
                print("Select a proper number like you were playing on a tic-tac-toe board!\n")
                t3 = 0                 

        elif scratch3 == scratch1 or scratch3 == scratch2:
            print("Number already selected! Input a different number.\n")
            t3 = 0

        elif scratch3 not in range (1,10):
            print("Select a valid number! (1 - 9)\n")
            t3 = 0
        
        else:
            t3 = 1
    
    scratch1 = (int(scratch1) - 1)
    scratch2 = (int(scratch2) - 1)
    scratch3 = (int(scratch3) - 1)
    card_scratch1 = random_card_numbers[scratch1-1]
    card_scratch2 = random_card_numbers[scratch2-1]
    card_scratch3 = random_card_numbers[scratch3-1]
    spots = ['*','*','*','*','*','*','*','*','*']
    spots[scratch1] = card_scratch1
    spots[scratch2] = card_scratch2
    spots[scratch3] = card_scratch3
    time.sleep(.7)
    print(f'\n|-----------------|')
    print(f'|   [{spots[0]}] [{spots[1]}] [{spots[2]}]   |')
    print(f'|   [{spots[3]}] [{spots[4]}] [{spots[5]}]   |')
    print(f'|   [{spots[6]}] [{spots[7]}] [{spots[8]}]   |')
    print(f'| Winning Numbers |')
    print(f'|   [{winning_numbers[0]}] [{winning_numbers[1]}] [{winning_numbers[2]}]   |')
    print(f'|-----------------|\n')
    if card_scratch1 in winning_numbers and card_scratch2 in winning_numbers and card_scratch3 in winning_numbers:
        payout = 2500
        bank += payout
        time.sleep(1)
        print(f'Holy cow! Congratulations, you have just won ${payout:.2f}!')
    else:
        print(f'Ah... better luck next time!')
    time.sleep(1)
    input("\nPress Enter to continue...")
    return bank


def play_big_bucket(bank): # plays big bucket and returns bank balance
    print('\nInsert ||[BIG BUCKET!]||',end=''), time.sleep(.5), print('.',end=''), time.sleep(.5), print('.',end=''), time.sleep(.5), print('.\n')
    if bank >= 50:
        bank -= 50
    else:
        print("Woah there... You haven't got enough funds for that!")
        time.sleep(1)
        input("Press enter to return.")
        return bank
    time.sleep(2)
    print("Test your luck at the biggest bucket of them all!")
    time.sleep(1)
    print('Match 1 Number = 20$')
    time.sleep(1)
    print('Match 2 Numbers = 100$!')
    time.sleep(1)
    print('Match 3 Numbers = Win up to 15,000$!!!\n\n')
    time.sleep(2.4)
    print(f'$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    print(f'$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    print(f'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(f'/|------------------------------|\\')
    print(f'\|   [1] [2] [3] [4]  [5]  [6]  |/')
    print(f'/|   [7] [8] [9] [10] [11] [12] |\\')
    print(f'/|                              |\\')
    print(f'\|     ~~~In the Bucket!!~~~    |/')
    print(f'/|                              |\\')
    print(f'/|         [*] [*] [*]          |\\')
    print(f'\|------------------------------|/')
    print(f'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(f'$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    print(f'$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    time.sleep(1)
    print("\nAre you ready... ?\n")
    time.sleep(2)
    winning_numbers = []
    random_card_numbers = []
    i = 0
    while i != 12:
        num = random.randint(1,12)
        if num not in random_card_numbers:
            random_card_numbers.append(num)
            i += 1
        else: 
            i = i
    k = 0
    while k != 3:
        win_num = random.randint(1,12)
        if win_num not in winning_numbers:
            winning_numbers.append(win_num)
            k += 1
        else:
            k = k
    t1 = 0
    while t1 != 1:  
        scratch1 = input("Select the first space to scratch: (1 - 12)\n\t>>> ")
        scratch1 = (int(scratch1))
        if scratch1 not in range (1,13):
            print("Select a valid number! (1 - 12)\n")
            t1 = 0
        else:
            t1 = 1
    time.sleep(1), print("\nPick carefully now... \n"), time.sleep(.5)
    t2 = 0
    while t2 != 1:  
        scratch2 = input("Select the second space to scratch: (1 - 12)\n\t>>> ")
        scratch2 = (int(scratch2))
        if scratch2 not in range (1,13):
            print("Select a valid number! (1 - 12)\n")
            t1 = 0
        elif scratch2 == scratch1:
            print("Number already selected! Input a different number.\n")
            t2 = 0
        else:
            t2 = 1
    time.sleep(1), print("\nLast space!\n"), time.sleep(.5)
    t3 = 0
    while t3 != 1:
        scratch3 = input("Select the third space to scratch: (1 - 12)\n\t>>> ")
        scratch3 = (int(scratch3))
        if scratch3 not in range (1,13):
            print("Select a valid number! (1 - 12)\n")
            t3 = 0
        elif scratch3 == scratch1 or scratch3 == scratch2:
            print("Number already selected! Input a different number.\n")
            t3 = 0
        else:
            t3 = 1
    scratch1 = (int(scratch1) - 1)
    scratch2 = (int(scratch2) - 1)
    scratch3 = (int(scratch3) - 1)
    card_scratch1 = random_card_numbers[scratch1-1]
    card_scratch2 = random_card_numbers[scratch2-1]
    card_scratch3 = random_card_numbers[scratch3-1]
    spots = ['$','$','$','$','$','$','$','$','$','$','$','$']
    spots[scratch1] = card_scratch1
    spots[scratch2] = card_scratch2
    spots[scratch3] = card_scratch3
    time.sleep(2)
    print(f'$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    print(f'$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    print(f'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(f'/|------------------------------|\\')
    print(f'\|   [{spots[0]}] [{spots[1]}] [{spots[2]}] [{spots[3]}] [{spots[4]}] [{spots[5]}]    |/')
    print(f'/|   [{spots[6]}] [{spots[7]}] [{spots[8]}] [{spots[9]}] [{spots[10]}] [{spots[11]}]    |\\')
    print(f'/|                              |\\')
    print(f'\|     ~~~In the Bucket!!~~~    |/')
    print(f'/|                              |\\')
    print(f'/|         [{winning_numbers[0]}] [{winning_numbers[1]}] [{winning_numbers[2]}]           |\\')
    print(f'\|------------------------------|/')
    print(f'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(f'$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    print(f'$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    winning_amount = 0
    matched_numbers = 0
    if card_scratch1 in winning_numbers or card_scratch2 in winning_numbers or card_scratch3 in winning_numbers:
        winning_amount = 20
        matched_numbers = 1
    else:
        pass
    if matched_numbers == 1:
        if card_scratch1 in winning_numbers and card_scratch2 in winning_numbers:
            winning_amount = 100
            matched_numbers = 2
    else:
        pass
    if matched_numbers == 1:
        if card_scratch1 in winning_numbers and card_scratch3 in winning_numbers:
            winning_amount = 100
            matched_numbers = 2
    else:
        pass
    if matched_numbers == 1:
        if card_scratch2 in winning_numbers and card_scratch3 in winning_numbers:
            winning_amount = 100
            matched_numbers = 2
    else:
        pass
    if matched_numbers == 2:
        if card_scratch1 in winning_numbers and card_scratch2 in winning_numbers and card_scratch3 in winning_numbers:
            random_jackpot = random.randint(10,150)
            winning_amount = winning_amount * random_jackpot
            matched_numbers = 3
    time.sleep(2)
    print('\n\n')
    if matched_numbers == 0:
        print("Rats... No luck today!")
    if matched_numbers == 1:
        print(f'Hey, thats somethin\'! You won ${winning_amount:.2f}')
        bank += winning_amount
    if matched_numbers == 2:
        print(f'Woah now! Congratulations! You won ${winning_amount:.2f}')
        bank += winning_amount
    if matched_numbers == 3:
        print(f'Holy Bucket! You won a whoppin\' total of ${winning_amount:.2f}!')
        bank += winning_amount
    print('\n')
    print(f'The winning numbers were: {winning_numbers}')
    print(f'You scratched: [{card_scratch1}, {card_scratch2}, {card_scratch3}]')
    time.sleep(1)
    input("\nPress Enter to continue...")
    return bank
