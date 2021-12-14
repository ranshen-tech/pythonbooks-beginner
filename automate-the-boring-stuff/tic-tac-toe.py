the_board = {
    'top-L': 'O', 'top-M': 'O', 'top-R': 'O',
    'mid-L': 'X', 'mid-M': 'X', 'mid-R': ' ',
    'low-L': ' ', 'low-M': ' ', 'low-R': 'X'
    }

def print_board(board):
    print(f"{board['top-L']} | {board['top-M']} | {board['top-R']}")
    print('- + - + -')
    print(f"{board['mid-L']} | {board['mid-M']} | {board['mid-R']}")
    print('- + - + -')
    print(f"{board['low-L']} | {board['low-M']} | {board['low-R']}")

print_board(the_board)