# Legend
# X for placement of ship and hit of ballteship
# ' ' for space that is avalible
# '#' for hit battle ship


from random import randint


HIDDEN_BOARD = [[" "] * 8 for x in range(8)]

GUESS_BOARD = [[" "] * 8 for i in range(8)]

letters_to_numbers = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7
}

def print_board(board):
    print('A B C D E F G H')
    print('\\\\\\\\///////')
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1

def create_battleships(board):
    for ship in range(5):
        ship_row, ship_column = randint(0, 7), randint(0, 7)
        while board[ship_row][ship_column] == "X":
            ship_row, ship_column = randint(0, 7), randint(0, 7)
            board[ship_row][ship_column] = "X"

