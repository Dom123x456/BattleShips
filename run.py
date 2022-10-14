# Legend
# X for placement of ship and hit of ballteship
# ' ' for space that is avalible
# '#' for hit battle ship

from time import sleep
from random import randint
# Board Battleship for there locatons on the board
HIDDEN_BOARD = [[" "] * 8 for x in range(8)]
# Board for displaying hits and misses
GUESS_BOARD = [[" "] * 8 for i in range(8)]


def title():
    """
    Refreshes the title after each screen has been cleared
    """
    print("<==>  /Battleship/  <==>\n")
    sleep(1)






def print_board(board):
    print(' A B C D E F G H')
    print('\\\\\\\\///////')
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1


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

# computer create 5 ships onto the board


def create_battleships(board):
    for number in range(5):
        ship_row, ship_column = randint(0, 7), randint(0, 7)
        while board[ship_row][ship_column] == "X":
            ship_row, ship_column = randint(0, 7), randint(0, 7)
            board[ship_row][ship_column] = "X"

# when input is incorrect print error messages


def get_battleship_location():
    row = input("Enter the row of the Battleship: ").upper()
    while row not in "12345678":
        print('Not valid choice, select a valid row.')
        row = input("Enter row of the Battleship: ").upper()
    column = input("Enter column of the Battleship: ").upper()
    while column not in "ABCDEFGH":
        print('Not valid choice, select a valid column.')
        column = input("Enter the column of the Battleship: ").upper()
    return int(row) - 1, letters_to_numbers[column]


# check if ships are hit

def count_hit_battleships(board):
    """
    Function to see if ships are hit
    """
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count


# turns amount and if turns are gone print message game over or repeated input

create_battleships(HIDDEN_BOARD)
turns = 10
print_board(HIDDEN_BOARD)
print_board(GUESS_BOARD)
while turns > 0:
    print('Guess a battleship location')
    print_board(GUESS_BOARD)
    rows, columns = get_battleship_location()
    if GUESS_BOARD[rows][columns] == "-":
        print("You guessed that one already.")
    elif HIDDEN_BOARD[rows][columns] == "X":
        print("Hit")
        GUESS_BOARD[rows][columns] = "X"
        turns -= 1
    else:
        print("MISS!")
        GUESS_BOARD[rows][columns] = "#"
        turns -= 1
    if count_hit_battleships(GUESS_BOARD) == 5:
        print("You win Congrats!")
        break
    print("You have " + str(turns) + " turns left")
    if turns == 0:
        print("No turns left Game over")
        break
