import random


# DISPLAYING THE BOARD
def display_board(board):
    print('     |     |')
    print('  ' + board[7] + '  |  ' + board[8] + '  |  ' + board[9])
    print('     |     |')
    print('-----------------')
    print('     |     |')
    print('  ' + board[4] + '  |  ' + board[5] + '  |  ' + board[6])
    print('     |     |')
    print('-----------------')
    print('     |     |')
    print('  ' + board[1] + '  |  ' + board[2] + '  |  ' + board[3])
    print('     |     |')


# TESTING THE BOARD
# test_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
# display_board(test_board)


# TAKING PLAYER INPUT AND ASSIGNING X OR O.
def player_input():
    marker = ''
    playerCPU = False

    # For some reason the following syntax won't provide the user input in pycharm
    # while not (marker == 'X' or marker == 'O'):
    while marker != 'X' and marker != 'O':
        marker = input('Player 1: Do you want to be X or O?').upper()
        playerCPU = input('Would you like to play with a CPU? yes or no').lower()
        if playerCPU == 'yes':
            playerCPU = True
            print('Player 2 will now be a CPU.')
        else:
            playerCPU = False
            print('Player 2 will be another player.')
    if marker == 'X' and playerCPU == True:
        return ('X', 'O', playerCPU)
    else:
        return ('O', 'X', playerCPU)
    if marker == 'X' and playerCPU == False:
        return ('X', 'O')
    else:
        return ('O', 'X')




# print(playerCPU)
# FUNCTION THAT TAKES IN THE BOARD LIST OBJECT, MARKER, AND POSITION
def place_marker(board, marker, position):
    board[position] = marker


# TESTING THE PLACE MARKER FUNCTION
# place_marker(test_board,'@',4)
# display_board(test_board)


# CHECKING FOR WINNING CONDITIONS
def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # TOP ROW
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # MIDDLE ROW
            (board[1] == mark and board[2] == mark and board[3] == mark) or  # BOTTOM ROW
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # LEFT COLUMN
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # MIDDLE COLUMN
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # RIGHT COLUMN
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # TOP LEFT TO LOWER RIGHT DIAGONAL
            (board[9] == mark and board[5] == mark and board[1] == mark))  # TOP RIGHT TO LOWER LEFT DIAGONAL


# CHECKING FOR WINNING PLAYER
# display_board(test_board)
# print(win_check(test_board, 'X'))


# FUNCTION THAT DETERMINES WHICH PLAYER GOES FIRST
def choose_first():
    flip = random.randint(0, 1)

    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'


# CHECK TO SEE IF SPACE IS AVAILABLE
def space_check(board, position):
    return board[position] == ' '


# CHECK TO SEE IF BOARD IS FULL
def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


# IF THE SPACE IS FREE, INPUT MARKER
def player_choice(board):
    position = 0

    while position not in range(1, 10) or not space_check(board, position):
        position = int(input('Choose a position: (1-9) '))

    return position

# CPU strategy
def cpu_choice(board):
    position = 0

    while position not in range(1, 10) or not space_check(board, position):
        position = 1 or 3 or 7 or 9

    return position


# ASKING THE PLAYER IF THEY WANT TO PLAY AGAIN
def replay():
    choice = ''

    while choice != 'YES' and choice != 'NO':
        choice = input('Play again? Enter YES or NO').upper()

        print('\n' * 100)
    return choice == 'YES'


print('Welcome to Tic Tac Toe!')

while True:

    # PLAY THE GAME

    # SET EVERYTHING UP (BOARD, WHO GOES FIRST, CHOOSE MARKERS)
    the_board = [' '] * 10
    player1_marker, player2_marker, cpu_marker = player_input()

    turn = choose_first()
    print(turn + ' will go first')

    play_game = input('Ready to play? yes or no?').lower()

    if play_game == 'yes':
        game_on = True
    else:
        game_on = False

    if cpu_marker:
        print('You are playing against a CPU. The CPU has a ' + player2_marker + ' marker')

    ## GAMEPLAY WITH CPU
    while cpu_marker and game_on:

        ### PLAYER ONE TURN
        if turn == 'Player 2':

            # Show the board
            display_board(the_board)

            # Choose a position
            position = player_choice(the_board)
            # Place the marker on the position
            place_marker(the_board, player2_marker, position)
            # Check if they won
            if win_check(the_board, player2_marker):
                print('\n' * 100)
                display_board(the_board)
                print('CPU has won')
                game_on = False
            else:
                # Or check if there is a tie
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Tie game')
                    game_on = False
                else:
                    # No tie and no Win? then next player's turn
                    turn = 'Player 1'
                    print('\n' * 100)

        ### PLAYER ONE TURN
        else:
            # Show the board
            display_board(the_board)

            # Choose a position
            position = player_choice(the_board)
            # Place the marker on the position
            place_marker(the_board, player1_marker, position)
            # Check if they won
            if win_check(the_board, player1_marker):
                print('\n' * 100)
                display_board(the_board)
                print('Player 1 has won')
                game_on = False
            else:
                # Or check if there is a tie
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Tie game')
                    game_on = False
                else:
                    # No tie and no Win? then next player's turn
                    turn = 'Player 2'
                    print('\n' * 100)

    ## GAMEPLAY
    while game_on and not cpu_marker:

        ### PLAYER ONE TURN
        if turn == 'Player 1':

            # Show the board
            display_board(the_board)

            # Choose a position
            position = player_choice(the_board)
            # Place the marker on the position
            place_marker(the_board, player1_marker, position)
            # Check if they won
            if win_check(the_board, player1_marker):
                print('\n' * 100)
                display_board(the_board)
                print('Player 1 has won')
                game_on = False
            else:
                # Or check if there is a tie
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Tie game')
                    game_on = False
                else:
                    # No tie and no Win? then next player's turn
                    turn = 'Player 2'
                    print('\n' * 100)

        ### PLAYER TWO TURN
        else:
            # Show the board
            display_board(the_board)

            # Choose a position
            position = player_choice(the_board)
            # Place the marker on the position
            place_marker(the_board, player2_marker, position)
            # Check if they won
            if win_check(the_board, player2_marker):
                print('\n' * 100)
                display_board(the_board)
                print('Player 2 has won')
                game_on = False
            else:
                # Or check if there is a tie
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Tie game')
                    game_on = False
                else:
                    # No tie and no Win? then next player's turn
                    turn = 'Player 1'
                    print('\n' * 100)

    # BREAK OUT OF THE WHILE LOOP ON replay()
    if not replay():
        break
