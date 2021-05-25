import random


# DISPLAYING THE BOARD
def display_board(board):
    print('     |     |')
    print('  ' + board[1] + '  |  ' + board[2] + '  |  ' + board[3])
    print('     |     |')
    print('-----------------')
    print('     |     |')
    print('  ' + board[4] + '  |  ' + board[5] + '  |  ' + board[6])
    print('     |     |')
    print('-----------------')
    print('     |     |')
    print('  ' + board[7] + '  |  ' + board[8] + '  |  ' + board[9])
    print('     |     |')


# THIS BOARD IS USED FOR POSITIONING
the_board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}


# THIS FUNCTION CHECKS TO SEE IF A PLAYER WON THE GAME
def check_if_won():
    if the_board[1] == the_board[2] and the_board[1] == the_board[3] and the_board[1] != ' ':
        return True
    elif the_board[4] == the_board[5] and the_board[4] == the_board[6] and the_board[4] != ' ':
        return True
    elif the_board[7] == the_board[8] and the_board[7] == the_board[9] and the_board[7] != ' ':
        return True
    elif the_board[1] == the_board[4] and the_board[1] == the_board[7] and the_board[1] != ' ':
        return True
    elif the_board[2] == the_board[5] and the_board[2] == the_board[8] and the_board[2] != ' ':
        return True
    elif the_board[3] == the_board[6] and the_board[3] == the_board[9] and the_board[3] != ' ':
        return True
    elif the_board[1] == the_board[5] and the_board[1] == the_board[9] and the_board[1] != ' ':
        return True
    elif the_board[7] == the_board[5] and the_board[7] == the_board[3] and the_board[7] != ' ':
        return True
    else:
        return False


# THIS FUNCTION CHECKS TO SEE WHICH MARK WON THE GAME
def check_which_mark(mark):
    return ((the_board[7] == mark and the_board[8] == mark and the_board[9] == mark) or  # TOP ROW
            (the_board[4] == mark and the_board[5] == mark and the_board[6] == mark) or  # MIDDLE ROW
            (the_board[1] == mark and the_board[2] == mark and the_board[3] == mark) or  # BOTTOM ROW
            (the_board[7] == mark and the_board[4] == mark and the_board[1] == mark) or  # LEFT COLUMN
            (the_board[8] == mark and the_board[5] == mark and the_board[2] == mark) or  # MIDDLE COLUMN
            (the_board[9] == mark and the_board[6] == mark and the_board[3] == mark) or  # RIGHT COLUMN
            (the_board[7] == mark and the_board[5] == mark and the_board[3] == mark) or  # DIAGONAL
            (the_board[9] == mark and the_board[5] == mark and the_board[1] == mark))  # DIAGONAL


# PLAYER GETS TO DECIDE THE MARKER 'O' OR 'X'
def player_input():
    marker = ''

    # For some reason the following syntax won't provide the user input in pycharm
    # while not (marker == 'X' or marker == 'O'):
    while marker != 'X' and marker != 'O':
        marker = input("Player 1: Do you want to be X or O?").upper()
    if marker == 'X':
        return 'X', 'O'
    else:
        return 'O', 'X'


# PERMISSION TO HAVE BOT TAKE CONTROL OF PLAYER 2
def bot_input():
    enable_player_bot = False

    while enable_player_bot != 'yes' and enable_player_bot != 'no':
        enable_player_bot = input("Would you like to play with a CPU? yes or no").lower()
        if enable_player_bot == 'yes':
            print(" ** Player 2 will now be a BOT **.")
            return True
        else:
            print(" ** Player 2 will be another player **. ")
            return False


# RANDOM DETERMINATION OF WHICH PLAYER GOES FIRST
def first_round():
    coin_toss = random.randint(0, 1)

    if coin_toss == 0:
        return 'Player 1'
    else:
        return 'Player 2'


# CHECK TO SEE IF THE POSITION ALREADY HAS A MARK
def space_check(position):
    if the_board[position] == ' ':
        return True
    else:
        return False


# ENTER MARK OF THE PLAYER IN THE POSITION AND CHECK FOR WIN
def player_position_choice(letter, position):
    if space_check(position):
        the_board[position] = letter
        display_board(the_board)
        if check_if_draw():
            print(" ** DRAW! **")
            print("Thanks for playing!")
            exit()
        if check_if_won():
            if letter == player2_marker:
                print(" ** Player 2 WINS! ** ")
                print("Thanks for playing!")
                exit()
            else:
                print(" ** Player 1 WINS! ** ")
                print("Thanks for playing!")
                exit()
        return
    else:
        print("That space is full!")
        position = int(input("Please enter a new position:  "))
        player_position_choice(letter, position)
        return


# CHECKS TO SEE IF THERE IS A DRAW
def check_if_draw():
    for key in the_board.keys():
        if the_board[key] == ' ':
            return False
    return True


# ASKING THE PLAYER IF THEY WANT TO PLAY AGAIN
def replay():
    choice = ''

    while choice != 'yes' and choice != 'no':
        choice = input("Play again? Enter YES or NO").lower()

        print("\n" * 3)
    return choice == 'YES'


# ASKING PLAYER ONE TO MOVE
def player_one_move():
    position = 0

    while position not in range(1, 10):
        position = int(input("Enter the position for " + player1_marker + ": "))
    player_position_choice(player1_marker, position)
    print("\n" * 2)
    return


# ASKING PLAYER TWO TO MOVE
def player_two_move():
    position = 0

    while position not in range(1, 10):
        position = int(input("Enter the position for " + player2_marker + ": "))
    player_position_choice(player2_marker, position)
    print("\n" * 2)
    return


# MINIMAX AI BOT FOR PLAYER TWO
def player_two_bot():
    high_score = -100
    best_position = 0
    for key in the_board.keys():
        if the_board[key] == ' ':
            the_board[key] = player2_marker
            score = minimax(the_board, 0, False)
            the_board[key] = ' '
            if score > high_score:
                high_score = score
                best_position = key

    player_position_choice(player2_marker, best_position)
    print("\n" * 2)
    return


# MINIMAX AI BOT FOR PLAYER TWO
def minimax(board, depth, maximizing):
    if check_which_mark(player2_marker):
        return 1
    elif check_which_mark(player1_marker):
        return -1
    elif check_if_draw():
        return 0

    if maximizing:
        high_score = -100
        for key in the_board.keys():
            if the_board[key] == ' ':
                the_board[key] = player2_marker
                score = minimax(board, depth + 1, False)
                the_board[key] = ' '
                if score > high_score:
                    high_score = score
        return high_score

    else:
        high_score = 100
        for key in the_board.keys():
            if the_board[key] == ' ':
                the_board[key] = player1_marker
                score = minimax(board, depth + 1, True)
                the_board[key] = ' '
                if score < high_score:
                    high_score = score
        return high_score


# GAME INSTRUCTIONS
print("The board positions go from 1-9 from the top:")
print('     |     |')
print('  1  |  2  |  3')
print('     |     |')
print('-----------------')
print('     |     |')
print('  4  |  5  |  6')
print('     |     |')
print('-----------------')
print('     |     |')
print('  7  |  8  |  9')
print('     |     |')
print("\n")


# DETERMINES WHICH PLAYER GOES FIRST, WHICH MARK, AND BOT
turn = first_round()
print("First turn will be randomized.")
print(turn + " will be going first this game!")
player1_marker, player2_marker = player_input()
bot = bot_input()


# STARTS THE GAME
while not check_if_won():
    while bot:
        if turn == 'Player 1':
            print("Player 1 TURN")
            player_one_move()
            print("Player 2 TURN")
            player_two_bot()
        else:
            print("Player 2 TURN")
            player_two_bot()
            print("Player 1 TURN")
            player_one_move()
    if turn == 'Player 1':
        print("Player 1 TURN")
        player_one_move()
        print("Player 2 TURN")
        player_two_move()
    else:
        print("Player 2 TURN")
        player_two_move()
        print("Player 1 TURN")
        player_one_move()
