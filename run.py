from time import sleep
from random import randint

# Legend
# X for placement of ship and hit of ballteship
# ' ' for space that is avalible
# '#' for hit battle ship
# Board Battleship for there locatons on the board
HIDDEN_BOARD = [[" "] * 8 for x in range(8)]
# Board for displaying hits and misses
GUESS_BOARD = [[" "] * 8 for i in range(8)]


def title():
    """
    Refreshes the title when the screen has been cleared
    """
    print("<==>  /Battleship/  <==>\n")
    sleep(1)


def introduction():
    """
    This gives the user a brief background story
    """

    intro = [
        "\nYour Mission\n",
        "Russian forces are grouping on the north pacific!\n",
        "The enemy forces are setting a blockade " +
        "The enemy will have full control of main shiping lanes. " +
        "Your mission is to destroy the main guarding force of the blockade" +
        "To allow the other ships" +
        "To make a wedge to stop enemy reinforcements"
        "\nGoodLuck!\n"
    ]
    title()
    print("\nIncoming message from Fleet Command......\n")
    sleep(2)
    for i in intro:
        print(i)
    resume_key()


def controls():
    """
    This functions provides instructions to the user on playing the game
    """

    controls_list = [
        "You must input a number and a letter seperatly" +
        "Select the grid ROW which will appear as a NUMBER",
        "Select the grid COLUMN which will appear as a LETTER",
        "To select the grid you want to target:",
        "* If a ship is within the grid coordinates you selected, " +
        "a hit will be registered as an X",
        "* If the grid is empty, it will be registered as a miss #",
    ]
    title()
    print("\nThis is what you must do to be successful\n:")
    sleep(2)
    for i in controls_list:
        print(i)
    sleep(2)
    resume_key()


def print_board(board):
    """
    generates board for battleship game
    """
    print('\n  A B C D E F G H\n')
    print('\n_______________________________\n')
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
    """
    creates 5 battleships on the board
    """
    for ship in range(5):
        ship_row, ship_column = randint(0, 7), randint(0, 7)
        while board[ship_row][ship_column] == "X":
            ship_row, ship_column = randint(0, 7), randint(0, 7)
        board[ship_row][ship_column] = "X"

# when input is incorrect print error messages


def get_battleship_location():
    """
    when entering the wrong input to either row or column print error message
    """
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
introduction()
controls()
create_battleships(HIDDEN_BOARD)
turns = 10
while turns > 0:
    print('\nGuess a battleship location\n')
    print_board(GUESS_BOARD)
    rows, columns = get_battleship_location()
    if GUESS_BOARD[rows][columns] == "-":
        print("\nYou guessed that one already.\n")
    elif HIDDEN_BOARD[rows][columns] == "X":
        print("\nHit\n")
        GUESS_BOARD[rows][columns] = "X"
        turns -= 1
    else:
        print("\nMISS!\n")
        GUESS_BOARD[rows][columns] = "#"
        turns -= 1
    if count_hit_battleships(GUESS_BOARD) == 5:
        print("\nYou win Congrats!\n")
        break
    print("\nYou have " + str(turns) + " turns left\n")
    if turns == 0:
        print("\nNo turns left Game over\n")
        break


def main():
    """
    Runs all program functions
    """
    introduction()
    controls()

main()