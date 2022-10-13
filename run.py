# Legend
# X for placement of ship and hit of ballteship
# ' ' for space that is avalible
# '#' for hit battle ship


from random import randint

HIDDEN_BOARD = [[" "] * 8 for x in range(8)]

GUESS_BOARD = [[" "] * 8 for i in range(8)]