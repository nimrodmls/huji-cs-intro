import random

def init_board(rows):
    """
    """
    return [["|" for matches in range(random.randint(1, 5))] for index in range(rows)]

def print_board(board):
    """
    """
    for row_index in range(len(board)):
        print("{index}: {matches}".format(index=row_index+1, matches=" ".join(board[row_index])))

def is_in_range(iterable, index):
    """
    """
    return (index > 0) and (index < len(iterable))

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

board = init_board(5)
print_board(board)
get_input("mallis", board)

def update_board(board, row, index):
    """
    """
    del(board[row][index])

def get_next_player(username, board):
    """
    """
    print_board()
    get_input()
    update_board()

def run_game():
    """
    """
    play_board = init_board(5)
    players = ["mallis1", "mallis2"]
    while not get_next_player():
        