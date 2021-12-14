the_board = {
    'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
    'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
    'low-L': ' ', 'low-M': ' ', 'low-R': ' '
    }

def print_board(board):
    print(f"{board['top-L']} | {board['top-M']} | {board['top-R']}")
    print('- + - + -')
    print(f"{board['mid-L']} | {board['mid-M']} | {board['mid-R']}")
    print('- + - + -')
    print(f"{board['low-L']} | {board['low-M']} | {board['low-R']}")

print_board(the_board)