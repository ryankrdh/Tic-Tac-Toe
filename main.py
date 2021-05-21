
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


test_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
display_board(test_board)


def player_input():
    marker = ''

    while marker != 'X' and marker != 'O':
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return 'X', 'O'
    else:
        return 'O', 'X'

print(player_input())
