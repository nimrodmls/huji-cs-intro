#################################################################
# FILE : lab4.py
# WRITER : Nimrod M.
# EXERCISE : intro2cs1 lab4 2023
# DESCRIPTION: Implementing the Nim Game
# STUDENTS I DISCUSSED THE EXERCISE WITH: N/A
# WEB PAGES I USED: N/A
# NOTES: N/A
#################################################################

import random

def init_board(rows, max_matches):
    """
    Generating a new play board according to the requirements
    rows (unsigned integer) - How many rows to generate
    max_matches (unsigned integer) - How many matches to include in a row, tops (it may be less)
    Function returns the play board generated.
    """
    return [["|" for matches in range(random.randint(1, max_matches))] for index in range(rows)]

def print_board(board):
    """
    Printing the play board in a nice and neat manner
    Function is not returning anything
    """
    for row_index in range(len(board)):
        print("{index}: {matches}".format(index=row_index+1, matches=" ".join(board[row_index])))

def is_in_range(iterable, index):
    """
    Checking if the index is in range of the iterable, without throwing an exception :)
    Returns true if it is, false otherwise.
    """
    return (index >= 0) and (index < len(iterable))

def get_input(username, board):
    """
    Getting the user input from the specified user and making sure the input 
    is valid according to the received play board
    The function returns a tuple of 2 items - The row input, and the match input.
    """
    # First we receive the row input
    row_input = None
    while row_input is None:
        row_input = input("{username} - Select a row (from 1 to {max_row}): ".format(
            username=username, max_row=len(board)))

        # Making sure the row input is indeed a decimal
        if row_input.isdecimal():
            row_input = int(row_input)-1
            # Making sure the row input is in range
            if not is_in_range(board, row_input):
                print("Invalid row {row_num} - Row is not in range!".format(row_num=row_input+1))
                row_input = None
        else: # Input is bad, try again!
            print("Incorrect input - \'{original_input}\' is not a decimal".format(
                original_input=row_input))
            row_input = None
    
    # Now we get the matches input
    match_count = None
    while match_count is None:
        match_count = input("{username} - Select a match count (from 1 to {max_count}): ".format(
            username=username, max_count=len(board[row_input])))
        
        # Making sure the match input is indeed a decimal
        if match_count.isdecimal():
            match_count = int(match_count)-1
            # Making sure the match input is in range
            if not is_in_range(board[row_input], match_count):
                print("Invalid match count {count} - Count is not in range!".format(
                    count=match_count+1))
                match_count = None
        else: # Input is bad, try again!
            print("Incorrect input - \'{original_input}\' is not a decimal".format(
                original_input=match_count))
            match_count = None
    
    return row_input, match_count

def is_board_empty(board):
    """
    Simply checking if the board is empty, if it is, the game is probably over.
    Function returns a boolean value of whether the board is empty or not.
    """
    return 0 == len(board)

def update_board(board, row, count):
    """
    Deleting matches from the specified row, in the amount of the specified count
    from the given play board.
    The function has no return value.
    """
    # Deleting matches from the 
    for match in range(count+1):
        del(board[row][0])
    if 0 == len(board[row]):
        del(board[row])

def get_next_player(username, board):
    """
    Starting another round for the specified username
    Function is printing the play board, getting the input from the user and
    updating the play board accordingly.
    At the end, the function returns True if the player has won, or False otherwise.
    """
    print_board(board)
    row, count = get_input(username, board)
    update_board(board, row, count)
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
    print("Player {username} has won!".format(username=players[current_player]))

# Starting the game
if __name__ == "__main__":
    run_game()