import random

def init_board(rows, max_matches):
    """
    """
    return [["|" for matches in range(random.randint(1, max_matches))] for index in range(rows)]

def print_board(board):
    """
    """
    for row_index in range(len(board)):
        print("{index}: {matches}".format(index=row_index+1, matches=" ".join(board[row_index])))

def is_in_range(iterable, index):
    """
    """
    return (index >= 0) and (index < len(iterable))

def get_input(username, board):
    """
    """
    row_input = None
    while row_input is None:
        row_input = input("{username} - Select a row (from 1 to {max_row}): ".format(
            username=username, max_row=len(board)))

        # Making sure the row input is indeed a decimal
        if row_input.isdecimal():
            row_input = int(row_input)-1
        else:
            print("Incorrect input - \'{original_input}\' is not a decimal".format(
                original_input=row_input))
            row_input = None

        # Checking additional conditions for the row input
        if not is_in_range(board, row_input):
            print("Invalid row {row_num} - Row is not in range!".format(row_num=row_input+1))
            row_input = None
        elif 0 == len(board[row_input]):
            print("Invalid row {row_num} - This row is empty!".format(row_num=row_input+1))
            row_input = None
    
    index_input = None
    while index_input is None:
        index_input = input("{username} - Select a index (from 1 to {max_index}): ".format(
            username=username, max_index=len(board[row_input])))
        if index_input.isdecimal():
            index_input = int(index_input)-1
        else:
            print("Incorrect input - {original_input} is not a number".format(
                original_input=row_input))
            index_input = None

        if not is_in_range(board[row_input], index_input):
            print("Invalid match index {index} - Index is not in range!".format(
                index=index_input+1))
            index_input = None
    
    return row_input, index_input

def is_board_empty(board):
    """
    """
    return 0 == len(board)

def update_board(board, row, index):
    """
    """
    for match in range(index+1):
        del(board[row][match])
    if 0 == len(board[row]):
        del(board[row])

def get_next_player(username, board):
    """
    """
    print_board(board)
    row, index = get_input(username, board)
    update_board(board, row, index)
    # The board is empty, the player has won!
    return is_board_empty(board)

def run_game():
    """
    """
    # We generate a board of 10 rows max, and max of 8 matches in each row
    play_board = init_board(random.randint(1,10), random.randint(2,8))
    players = ["mallis1", "mallis2"]
    current_player = 0
    while not get_next_player(players[current_player], play_board):
        # Reset the current player index, or increment it
        if len(players)-1 == current_player:
            current_player = 0
        else:
            current_player += 1

run_game()