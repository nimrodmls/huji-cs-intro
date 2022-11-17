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
    """
    """
    column = name[:1]
    row = name[1:]

    # Column index is not from the alphabet or it is not capital
    if (ord('Z') < ord(column)) or (ord('A') > ord(column)):
        return None
    # A is the base index of columns, we decrement it from the ASCII value we received
    column = ord(column) - ord('A')
    
    # Row index is not a decimal, this is wrong
    if not helper.is_int(row):
        return None
    row = int(row)-1 # This is safe, we decrement 1 so it would identify as list index

    return row, column

def valid_ship(board, size, loc):
    """
    """
    requested_row = loc[0]
    requested_column = loc[1]

    # Validating input
    if (requested_row + (size-1) >= len(board)) or (requested_row < 0):
        return False
    if (requested_column >= len(board[requested_row]) or (requested_column < 0)):
        return False

    # Making sure there are no other ships in the requested cells
    for index in range(size):
        if helper.WATER != board[requested_row + index][requested_column]:
            return False

    return True

def get_user_coordinate(board, ship_size):
    """
    """
    loc = None
    while loc is None:
        helper.print_board(board)
        user_input = helper.get_input(
            "Enter top coordinate for ship of size {ship_size}: ".format(ship_size=ship_size))
        loc = cell_loc(user_input)
        if loc is None:
            print("Invalid input - Try again in format [A-Z][1-99]")
        elif not valid_ship(board, ship_size, loc):
            print("Invalid location {location}".format(location=user_input))
            loc = None

    return loc

def place_ship(board, ship_size, row, column):
    """
    """
    for row_index in range(ship_size):
        board[row + row_index][column] = helper.SHIP

def find_available_cells(board, ship_size):
    """
    """
    available_cells = []
    for row_index in range(len(board)):
        for column_index in range(len(board[row_index])):
            if valid_ship(board, ship_size, (row_index, column_index)):
                available_cells.append((row_index, column_index))
    return available_cells

def create_cpu_board(rows, columns, ship_sizes):
    """
    """
    cpu_board = init_board(rows, columns)

    for ship_size in ship_sizes:
        row, column = helper.choose_ship_location(cpu_board, ship_size, find_available_cells(cpu_board, ship_size))
        place_ship(cpu_board, ship_size, row, column)

    return cpu_board

def create_player_board(rows, columns, ship_sizes):
    """
    """
    play_board = init_board(rows, columns)

    for ship_size in ship_sizes:
        row, column = get_user_coordinate(play_board, ship_size)
        place_ship(play_board, ship_size, row, column)
    
    return play_board


def fire_torpedo(board, loc):
    """
    """
    requested_cell = board[loc[0]][loc[1]]
    if helper.SHIP == requested_cell:
        requested_cell = helper.HIT_SHIP
    elif helper.WATER == requested_cell:
        requested_cell == helper.HIT_WATER

    return board

def start_game():
    """
    """
    cpu_board = create_cpu_board(helper.NUM_ROWS, helper.NUM_COLUMNS, helper.SHIP_SIZES)
    player_board = create_player_board(helper.NUM_ROWS, helper.NUM_COLUMNS, helper.SHIP_SIZES)

    print("All set, the game is starting!")



def main():
    """
    """
    start_game()


if __name__ == "__main__":
    main()
