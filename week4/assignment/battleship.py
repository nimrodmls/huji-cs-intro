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
import copy

def init_board(rows, columns):
    """
    """
    return [[helper.WATER for column in range(columns)] for row in range(rows)]

def cell_loc(name):
    """
    """
    column = name[:1].upper()
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

def is_out_of_bounds(board, row, column, ship_size=0):
    """
    """
    if (row + ship_size >= len(board)) or (row < 0):
        return True
    if (column >= len(board[row]) or (column < 0)):
        return True
    return False

def valid_ship(board, size, loc):
    """
    """
    requested_row = loc[0]
    requested_column = loc[1]

    # Validating input
    if is_out_of_bounds(board, requested_row, requested_column, ship_size=(size-1)):
        return False

    # Making sure there are no other ships in the requested cells
    for index in range(size):
        if helper.WATER != board[requested_row + index][requested_column]:
            return False

    return True

def get_user_ship_coordinate(board, ship_size):
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

def get_user_torpedo_target(board):
    """
    """
    loc = None
    while loc is None:
        user_input = helper.get_input("Enter coordinate for torpedo target: ")
        loc = cell_loc(user_input)
        if loc is None:
            print("Invalid input - Try again in format [A-Z][1-99]")
        elif is_out_of_bounds(board, loc[0], loc[1]):
            print("Invalid location {location}".format(location=user_input))
            loc = None
        elif board[loc[0]][loc[1]] in (helper.HIT_SHIP, helper.HIT_WATER):
            print("Location was already fired upon, try another location")
            loc = None

    return loc

def place_ship(board, ship_size, row, column):
    """
    """
    for row_index in range(ship_size):
        board[row + row_index][column] = helper.SHIP

def find_available_ship_cells(board, ship_size):
    """
    """
    return {(row_index, column_index) for row_index in range(len(board)) 
        for column_index in range(len(board[row_index])) 
            if valid_ship(board, ship_size, (row_index, column_index))}

def get_potential_targets(board):
    return {(row_index, column_index) for row_index in range(len(board)) 
        for column_index in range(len(board[row_index])) 
            if board[row_index][column_index] in (helper.WATER, helper.SHIP)}

def create_cpu_board(rows, columns, ship_sizes):
    """
    """
    cpu_board = init_board(rows, columns)

    for ship_size in ship_sizes:
        row, column = helper.choose_ship_location(cpu_board, ship_size, 
            find_available_ship_cells(cpu_board, ship_size))
        place_ship(cpu_board, ship_size, row, column)

    return cpu_board

def create_player_board(rows, columns, ship_sizes):
    """
    """
    play_board = init_board(rows, columns)

    for ship_size in ship_sizes:
        row, column = get_user_ship_coordinate(play_board, ship_size)
        place_ship(play_board, ship_size, row, column)
    
    return play_board

def hide_ships(board):
    """
    """
    # Creating a copy so we won't alter the original
    hidden_board = copy.deepcopy(board)

    for row in range(len(hidden_board)):
        for cell in range(len(hidden_board[row])):
            if helper.SHIP == hidden_board[row][cell]:
                hidden_board[row][cell] = helper.WATER

    return hidden_board

def fire_torpedo(board, loc):
    """
    """
    if helper.SHIP == board[loc[0]][loc[1]]:
        board[loc[0]][loc[1]] = helper.HIT_SHIP
    elif helper.WATER == board[loc[0]][loc[1]]:
        board[loc[0]][loc[1]] = helper.HIT_WATER

    return board

def is_fleet_destroyed(board):
    """
    """
    for row in board:
        for cell in row:
            if helper.SHIP == cell:
                return False
    return True

def start_game():
    """
    """
    player_board = create_player_board(
        helper.NUM_ROWS, helper.NUM_COLUMNS, helper.SHIP_SIZES)
    cpu_board = create_cpu_board(
        helper.NUM_ROWS, helper.NUM_COLUMNS, helper.SHIP_SIZES)

    #print("All set, the game is starting!")

    while (not is_fleet_destroyed(cpu_board)) and (not is_fleet_destroyed(player_board)):

        helper.print_board(player_board, hide_ships(cpu_board))
        # Do the player's turn
        fire_torpedo(cpu_board, get_user_torpedo_target(cpu_board))

        #  if the player didn't win this round
        # Let CPU do its turn, we pass an hidden board of the player (the CPU's opponent), 
        # along with the possible target locations.
        cpu_target = helper.choose_torpedo_target(
            hide_ships(player_board), get_potential_targets(player_board))
        fire_torpedo(player_board, cpu_target)

    helper.print_board(player_board, cpu_board)

def main():
    """
    """
    continue_game = True
    while continue_game:
        start_game()

        user_input = None
        while user_input is None:
            user_input = helper.get_input("Do you wish to start another round? (Y/N): ")
            if ("Y" == user_input) or ("N" == user_input):
                continue_game = ("Y" == user_input)
            else:
                print("Invalid input - Choose Y to continue or N to quit")
                user_input = None
    
if __name__ == "__main__":
    main()
