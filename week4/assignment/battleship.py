#################################################################
# FILE : battleship.py
# WRITER : Nimrod M.
# EXERCISE : intro2cs1 ex4 2023
# DESCRIPTION: Implementing the Battleships Game
# STUDENTS I DISCUSSED THE EXERCISE WITH: N/A
# WEB PAGES I USED: N/A
# NOTES: N/A
#################################################################

import helper

def init_board(rows, columns):
    """
    """
    return [[helper.WATER for column in range(columns)] for row in range(rows)]

def cell_loc(name):
    column = name[:1]
    row = name[1:]

    # Column index is not from the alphabet or it is not capital
    if (ord('Z') < ord(column)) or (ord('A') > ord(column)):
        return None
    # A is the base index of columns, we decrement it from the ASCII value we received
    column = ord(column) - ord('A')
    
    # Row index is not a decimal, this is wrong
    if not row.isdecimal():
        return None
    row = int(row)-1 # This is safe, we decrement 1 so it would identify as list index

    return row, column


def valid_ship(board, size, loc):
    pass


def create_player_board(rows, columns, ship_sizes):
    pass


def fire_torpedo(board, loc):
    pass


def main():
    print(cell_loc('Z53'))


if __name__ == "__main__":
    main()
