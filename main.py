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
test_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
display_board(test_board)


# TAKING PLAYER INPUT AND ASSIGNING X OR O.
def player_input():
    marker = ''

    # For some reason the following syntax won't provide the user input in pycharm
    # while not (marker == 'X' or marker == 'O'):
    while marker != 'X' and marker != 'O':
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return 'X', 'O'
    else:
        return 'O', 'X'


print(player_input())


# FUNCTION THAT TAKES IN THE BOARD LIST OBJECT, MARKER, AND POSITION
def place_marker(board, marker, position):

    board[position] = marker


# TESTING THE PLACE MARKER FUNCTION
place_marker(test_board,'@',4)
display_board(test_board)


# CHECKING FOR WINNING CONDITIONS
def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # TOP ROW
    (board[4] == mark and board[5] == mark and board[6] == mark) or # MIDDLE ROW
    (board[1] == mark and board[2] == mark and board[3] == mark) or # BOTTOM ROW
    (board[7] == mark and board[4] == mark and board[1] == mark) or # LEFT COLUMN
    (board[8] == mark and board[5] == mark and board[2] == mark) or # MIDDLE COLUMN
    (board[9] == mark and board[6] == mark and board[3] == mark) or # RIGHT COLUMN
    (board[7] == mark and board[5] == mark and board[3] == mark) or # TOP LEFT TO LOWER RIGHT DIAGONAL
    (board[9] == mark and board[5] == mark and board[1] == mark)) # TOP RIGHT TO LOWER LEFT DIAGONAL


# CHECKING FOR WINNING PLAYER
display_board(test_board)
print(win_check(test_board, 'X'))
