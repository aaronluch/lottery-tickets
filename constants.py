# Constants for the Deck and Deck Values, as well as additional Graphics


# constants
# card deck
DECK_NAMES = {'SA': ['ace of spades', '1', 'S', '14'],
        'S2': ['two of spades', '2', 'S', '2'],
        'S3': ['three of spades', '3', 'S', '3'],
        'S4': ['four of spades', '4', 'S', '4'],
        'S5': ['five of spades', '5', 'S', '5'],
        'S6': ['six of spades', '6', 'S', '6'],
        'S7': ['seven of spades', '7', 'S', '7'],
        'S8': ['eight of spades', '8', 'S', '8'],
        'S9': ['nine of spades', '9', 'S', '9'],
        'S10': ['ten of spades', '10', 'S', '10'],
        'SJ': ['jack of spades', '10', 'S', '11'],
        'SQ': ['queen of spades', '10', 'S', '12'],
        'SK': ['king of spades', '10', 'S', '13'],
        'CA': ['ace of clubs', '1', 'C', '14'],
        'C2': ['two of clubs', '2', 'C', '2'],
        'C3': ['three of clubs', '3', 'C', '3'],
        'C4': ['four of clubs', '4', 'C', '4'],
        'C5': ['five of clubs', '5', 'C', '5'],
        'C6': ['six of clubs', '6', 'C', '6'],
        'C7': ['seven of clubs', '7', 'C', '7'],
        'C8': ['eight of clubs', '8', 'C', '8'],
        'C9': ['nine of clubs', '9', 'C', '9'],
        'C10': ['ten of clubs', '10', 'C', '10'],
        'CJ': ['jack of clubs', '10', 'C', '11'],
        'CQ': ['queen of clubs', '10', 'C', '12'],
        'CK': ['king of clubs', '10', 'C', '13'],
        'HA': ['ace of hearts', '1', 'H', '14'],
        'H2': ['two of hearts', '2', 'H', '2'],
        'H3': ['three of hearts', '3', 'H', '3'],
        'H4': ['four of hearts', '4', 'H', '4'],
        'H5': ['five of hearts', '5', 'H', '5'],
        'H6': ['six of hearts', '6', 'H', '6'],
        'H7': ['seven of hearts', '7', 'H', '7'],
        'H8': ['eight of hearts', '8', 'H', '8'],
        'H9': ['nine of hearts', '9', 'H', '9'],
        'H10': ['ten of hearts', '10', 'H', '10'],
        'HJ': ['jack of hearts', '10', 'H', '11'],
        'HQ': ['queen of hearts', '10', 'H', '12'],
        'HK': ['king of hearts', '10', 'H', '13'],
        'DA': ['ace of diamonds', '1', 'D', '14'],
        'D2': ['two of diamonds', '2', 'D', '2'],
        'D3': ['three of diamonds', '3', 'D', '3'],
        'D4': ['four of diamonds', '4', 'D', '4'],
        'D5': ['five of diamonds', '5', 'D', '5'],
        'D6': ['six of diamonds', '6', 'D', '6'],
        'D7': ['seven of diamonds', '7', 'D', '7'],
        'D8': ['eight of diamonds', '8', 'D', '8'],
        'D9': ['nine of diamonds', '9', 'D', '9'],
        'D10': ['ten of diamonds', '10', 'D', '10'],
        'DJ': ['jack of diamonds', '10', 'D', '11'],
        'DQ': ['queen of diamonds', '10', 'D', '12'],
        'DK': ['king of diamonds', '10', 'D', '13'],
        '00': ['joker', '0', 'X', '0']}

DECK = ['SA', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'SJ', 'SQ', 'SK',
        'CA', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'CJ', 'CQ', 'CK',
        'HA', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10', 'HJ', 'HQ', 'HK',
        'DA', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'DJ', 'DQ', 'DK'] 
POKER_WINS = ['royal flush', 'straight flush', 'four of a kind', 'full house', 'flush', 'straight', 'three of a kind', 'two pair', 'pair', 'high card']
WIN_STRENGTHS = {'royal flush': 9, 'straight flush': 8, 'four of a kind': 7, 'full house': 6, 'flush': 5, 'straight': 4, 'three of a kind': 3, 'two pair': 2, 'pair': 1}
DECK_VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14']

# prices
entry_amount = 1000
super_winner_price = 10
mini_scratch_price = 1
lotto_4_price = 20
big_bucket_price = 50
cola_price = 2
hot_dog_price = 5
chips_price = 2
coffee_price = 1

# titles and graphics
TITLE_1 = ' ' + '_' * 28
TITLE_2 = '|' + '*' * 28 + '|'
TITLE_3 = '|' + '*' + ' ' * 26 + '*' + '|'
TITLE_4 = '|' + '*' + ' ' * 8 + 'WELCOME TO' + ' ' * 8 + '*' + '|' 
TITLE_5 = '|' + '*' + ' ' * 11 + ' THE' + ' ' * 11 + '*' + '|'
TITLE_6 = '|' + '*' + ' ' * 7 + 'LOTTO  STAND' + ' ' * 7 + '*' + '|'
TITLE_7 = '|' + '*' + ' ' * 26 + '*' + '|'
TITLE_8 = '|' + '*' * 28 + '|'
TITLE_9 = "'" + '-' * 28 + "'"
TITLE = TITLE_1 + '\n' + TITLE_2 + '\n' + TITLE_3 + '\n' + TITLE_4 + '\n' + TITLE_5 + '\n' + TITLE_6 + '\n' + TITLE_7 + '\n' + TITLE_8 + '\n' + TITLE_9
COUNTER_TITLE = '\n\nTHE FRONT COUNTER\n' + '*' * 17
CLERK = '\n' + ' ' * 10 + 'Well...what can I do for you?\n' + ' ' * 10 + '-' * 29 + '\n' + ' ' * 11 + '____     | /' + '\n' + ' ' * 10 + \
        '/    \    |/' + '\n' + ' ' * 8 + '~' * 10 + '\n' + ' ' * 9 + 'l ^ ,^|' + '\n' + ' ' * 10 + '\  o /  _' + '\n' + ' ' * 10 + '| ---   i)' + \
        '\n' + ' ' * 8 + '/  \./\=\/ /' + '\n' + ' ' * 7 + '/    |  \ _/' + '\n' + ' ' * 7 + "'--- |"
LOTTO_TIX_1 = '            __    ____  ________________     ___________  __'
LOTTO_TIX_2 = '           / /   / __ \/_  __/_  __/ __ \   /_  __/  _/ |/ /'
LOTTO_TIX_3 = '          / /   / / / / / /   / / / / / /    / /  / / |   / '
LOTTO_TIX_4 = '         / /___/ /_/ / / /   / / / /_/ /    / / _/ / /   |  '
LOTTO_TIX_5 = '        /_____/\____/ /_/   /_/  \____/    /_/ /___//_/|_|  '                                                  
LOTTO_TIX_6 = '  ' + '_' * 70
LOTTO_TIX_7 = ' |   _________________     _________________     ____________________   |'
LOTTO_TIX_8 = ' |  |  "SUPER WINNER" |   | mini scratch. $' + str(mini_scratch_price) + '|   | ****************** |  |'
LOTTO_TIX_9 = ' |  |     DELUXE!!    |   | hit  3  to win  |   | *                * |  |'
LOTTO_TIX_10 = ' |  |  per play: $' + str(super_winner_price) + '  |   |   { } { } { }   |   | *    LOTTO       * |  |'
LOTTO_TIX_11 = " |  '-----------------'   '-----------------'   | *     4  LOW     * |  |"
LOTTO_TIX_12 = ' |   _______________________________________    | *                * |  |'
LOTTO_TIX_13 = ' |  |---------------------------------------|   | *   >> $' + str(lotto_4_price) + ' <<    * |  |'
LOTTO_TIX_14 = " |  | redstonelottery.com's                 |   | *                * |  |"
LOTTO_TIX_15 = ' |  |    BIG BUCKET SUPER WINNER SCRATCHER  |   | *  scratch to    * |  |'
LOTTO_TIX_16 = ' |  |              { $' + str(big_bucket_price) + ' entry }            |   | * reveal ur win! * |  |'
LOTTO_TIX_17 = ' |  |   ___   ___   ___   ___   ___   ___   |   | *                * |  |'
LOTTO_TIX_18 = ' |  |  {   } {   } {   } {   } {   } {   }  |   | *  { }  { }  { } * |  |'
LOTTO_TIX_19 = ' |  |   ___   ___   ___   ___   ___   ___   |   | *  { }  { }  { } * |  |'
LOTTO_TIX_20 = ' |  |  {   } {   } {   } {   } {   } {   }  |   | *  { }  { }  { } * |  |'
LOTTO_TIX_21 = ' |  |_______________________________________|   | ****************** |  |'
LOTTO_TIX_22 = " |  '---------------------------------------'   '--------------------'  |"
LOTTO_TIX_23 = " '----------------------------------------------------------------------'"
LOTTO_TIX = LOTTO_TIX_1 + '\n' + LOTTO_TIX_2 + '\n' + LOTTO_TIX_3 + '\n' + LOTTO_TIX_4 + '\n' + LOTTO_TIX_5 + '\n' + LOTTO_TIX_6 + '\n' + \
            LOTTO_TIX_7 + '\n' + LOTTO_TIX_8 + '\n' + LOTTO_TIX_9 + '\n' + LOTTO_TIX_10 + '\n' + LOTTO_TIX_11 + '\n' + LOTTO_TIX_12 + '\n' + \
            LOTTO_TIX_13 + '\n' + LOTTO_TIX_14 + '\n' + LOTTO_TIX_15 + '\n' + LOTTO_TIX_16 + '\n' + LOTTO_TIX_17 + '\n' + LOTTO_TIX_18 + '\n' + \
            LOTTO_TIX_19 + '\n' + LOTTO_TIX_20 + '\n' + LOTTO_TIX_21 + '\n' + LOTTO_TIX_22 + '\n' + LOTTO_TIX_23 
SNACK_1 = ',---------------------------------------------------------------------------,'
SNACK_2 = '| ,---.  ,--.  ,--.  ,---.   ,-----.,--. ,--.    ,-----.    ,---.  ,------. |'
SNACK_3 = "|'   .-' |  ,'.|  | /  O  \ '  .--./|  .'   /    |  |) /_  /  O  \ |  .--. '|"
SNACK_4 = "|`.  `-. |  |' '  ||  .-.  ||  |    |  .   '     |  .-.  \|  .-.  ||  '--'.'|"
SNACK_5 = "|.-'    ||  | `   ||  | |  |'  '--'\|  |\   \    |  '--' /|  | |  ||  |\  \ |"
SNACK_6 = "|`-----' `--'  `--'`--' `--' `-----'`--' '--'    `------' `--' `--'`--' '--'|"
SNACK_7 = "'---------------------------------------------------------------------------'" + '\n'
SNACK_8 = '    [===]                ___       _____________________'
SNACK_9 = '     ] [             ___/   |/\   |---------------------|'
SNACK_10 = '    [   ]           /  /    / /   )                     |'
SNACK_11 = '   |     |         /  / ~  / /    (     _    _          |'
SNACK_12 = '  [       ]       /  /    / /     |  __| |_ (_)_ __ ___ (    _____________===.'
SNACK_13 = "  |_______|      /  / ~  / /      | / _| ' \| | '_ (_-< |   (________________)"
SNACK_14 = '  |  cola |     /  /    / /       ) \__|_||_|_| .__/__/ )    |              |'
SNACK_15 = '  (  ^^^^ )    /  / ~  / /        |           |_|       (    |--------------|'
SNACK_16 = '   )-----(    /  /    / /         |   potato            |    |  cuppajoe    |'
SNACK_17 = '  (       )  (  /    / /          (                     |    (______________)'
SNACK_18 = '  |       |   \(    | /           |_____________________/     \            / '
SNACK_19 = "   \__.__/     '\__/-'            '--------------------'       '=========='"
SNACK_20 = f'     ${cola_price}          ${hot_dog_price}                         ${chips_price}                      ${coffee_price}'
SNACK = SNACK_1 + '\n' + SNACK_2 + '\n' + SNACK_3 + '\n' + SNACK_4 + '\n' + SNACK_5 + '\n' + SNACK_6 + '\n' + SNACK_7 + '\n' + SNACK_8 + '\n' + \
        SNACK_9 + '\n' + SNACK_10 + '\n' + SNACK_11 + '\n' + SNACK_12 + '\n' + SNACK_13 + '\n' + SNACK_14 + '\n' + SNACK_15 + '\n' + SNACK_16 + \
        '\n' + SNACK_17 + '\n' + SNACK_18 + '\n' + SNACK_19 + '\n\n' + SNACK_20
CASINO_1 = '\n' + '   /////Welcome//to//the///////////////////////////////////////////////////////////////////////////////////////////////'
CASINO_2 = '  ::================================================================================================================::/'
CASINO_3 = '  [] ______    _____  _____  __ __      _____   _______       _____    _____    ______   __    __   __     _____    []/'
CASINO_4 = '  []/ ____/\ /\_____\/\ __/\/_/\__/\  /\_____\/\_______)\    /\ __/\  /\___/\  / ____/\ /\_\  /_/\ /\_\   ) ___ (   []/'
CASINO_5 = '  []) ) __\/( (_____/) )__\/) ) ) ) )( (_____/\(___  __\/    ) )__\/ / / _ \ \ ) ) __\/ \/_/  ) ) \ ( (  / /\_/\ \  []/'
CASINO_6 = '  [] \ \ \   \ \__\ / / /  /_/ /_/_/  \ \__\    / / /       / / /    \ \(_)/ /  \ \ \    /\_\/_/   \ \_\/ /_/ (_\ \ []/'
CASINO_7 = '  [] _\ \ \  / /__/_\ \ \_ \ \ \ \ \  / /__/_  ( ( (        \ \ \_   / / _ \ \  _\ \ \  / / /\ \ \   / /\ \ )_/ / / []/'
CASINO_8 = '  [])____) )( (_____\) )__/\)_) ) \ \( (_____\  \ \ \        ) )__/\( (_( )_) ))____) )( (_(  )_) \ (_(  \ \/_\/ /  []/'
CASINO_9 = '  []\____\/  \/_____/\/___\/\_\/ \_\/ \/_____/  /_/_/        \/___\/ \/_/ \_\/ \____\/  \/_/  \_\/ \/_/   )_____(   []/'
CASINO_10 = '  []                                                                                                                []/'
CASINO_11 = '  ::================================================================================================================::/' + '\n'
CASINO_12 = "       Lucky you! You've found my secret casino."
CASINO_13 = '       -----------------------------------------'
CASINO_14 = '                                        \ |    ____'
CASINO_15 = '                                         \|   /    \  '
CASINO_16 = '                 oo                         ~~~~~~~~~~'
CASINO_17 = '                 /\                          |^, ^ l'
CASINO_18 = '                 ||                           \ .  /'
CASINO_19 = "             .---||---,                       _'-- |"
CASINO_20 = "            |  '-==-'  |                     / _\./ \    "
CASINO_21 = "             \--------/                   .--\____  |----."
CASINO_22 = '              |      |                   /      ##       |    '
CASINO_23 = '              |      |                  /     # # #      /'
CASINO_24 = '             /________\                 |________________|' + '\n\n'
CASINO = CASINO_1 + '\n' + CASINO_2 + '\n' + CASINO_3 + '\n' + CASINO_4 + '\n' + CASINO_5 + '\n' + CASINO_6 + '\n' + CASINO_7 + '\n' + CASINO_8 + \
         '\n' + CASINO_9 + '\n' + CASINO_10 + '\n' + CASINO_11 + '\n' + CASINO_12 + '\n' + CASINO_13 + '\n' + CASINO_14 + '\n' + CASINO_15 + '\n' + \
         CASINO_16 + '\n' + CASINO_17 + '\n' + CASINO_18 + '\n' + CASINO_19 + '\n' + CASINO_20 + '\n' + CASINO_21 + '\n' + CASINO_22 + '\n' + CASINO_23 + '\n' + CASINO_24 
