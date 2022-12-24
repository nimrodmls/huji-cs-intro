#################################################################
# FILE : board.py
# WRITER : Nimrod M.
# EXERCISE : intro2cs1 ex9 2023
# DESCRIPTION: Implementing the Board for Rush Hour Game
# STUDENTS I DISCUSSED THE EXERCISE WITH: N/A
# WEB PAGES I USED: N/A
# NOTES: N/A
#################################################################

from helper import load_json

#class Coordinate(object):
#    """
#    """
#    DEFAULT_VALUE = '.'
#
#    def __init__(self, row_index, cell_index, cell_value=DEFAULT_VALUE):
#        """
#        """
#        self._row_index = row_index
#        self._cell_index = cell_index
#        self._cell_value = cell_value
#
#    def get_coordinates():
#        """
#        """
#        return 

class InvalidCoordinateException(Exception):
    """
    Raised when the given coordinate is invalid
    """
    pass

class Board:
    """
    Add a class description here.
    Write briefly about the purpose of the class
    """

    BOARD_SIZE = 7
    EMPTY_CELL_VALUE = '.'
    EXIT_CELL = (3, 7)
    COORDINATE_ROW_INDEX = 0
    COORDINATE_CELL_INDEX = 1

    def __init__(self):
        """
        Initializes a new & empty board
        """
        self._board = [[Board.EMPTY_CELL_VALUE for cell_index in range(Board.BOARD_SIZE)] 
                            for row_index in range(Board.BOARD_SIZE)]
        self._cars = []

    def __str__(self):
        """
        This function is called when a board object is to be printed.
        :return: A string of the current status of the board
        """
        # The game may assume this function returns a reasonable representation
        # of the board for printing, but may not assume details about it.
        # implement your code and erase the "pass"
        final_str = ""
        for row in self._board:
            final_str += " ".join(row) + "\n"
        return final_str

    def cell_list(self):
        """
        This function returns the coordinates of cells in this board
        :return: list of coordinates
        """
        cells = [(row_index, cell_index) for row_index in range(Board.BOARD_SIZE) 
                    for cell_index in range(Board.BOARD_SIZE)]
        cells.append(Board.EXIT_CELL)
        return cells

    def possible_moves(self):
        """
        This function returns the legal moves of all cars in this board
        :return: list of tuples of the form (name,move_key,description)
                 representing legal moves
        """
        all_moves = []
        for car in self._cars:
            moves = car.possible_moves()
            all_moves += [(car.get_name(), move, moves[move]) for move in moves]
        return all_moves

    def target_location(self):
        """
        This function returns the coordinates of the location which is to be filled for victory.
        :return: (row,col) of goal location
        """
        return Board.EXIT_CELL

    def cell_content(self, coordinate):
        """
        Checks if the given coordinates are empty.
        Raises InvalidCoordinateException if the given coordinate is invalid.
        :param coordinate: tuple of (row,col) of the coordinate to check
        :return: The name if the car in coordinate, None if empty
        """
        if not self._is_valid_coordinate(coordinate):
            raise InvalidCoordinateException

        row_index = coordinate[Board.COORDINATE_ROW_INDEX]
        cell_index = coordinate[Board.COORDINATE_CELL_INDEX]
        cell_value = self._board[row_index][cell_index]

        return None if Board.EMPTY_CELL_VALUE == cell_value else cell_value

    def add_car(self, car):
        """
        Adds a car to the game.
        :param car: car object of car to add
        :return: True upon success. False if failed
        """
        # Remember to consider all the reasons adding a car can fail.
        # You may assume the car is a legal car object following the API.
        # implement your code and erase the "pass"
        pass

    def move_car(self, name, move_key):
        """
        moves car one step in given direction.
        :param name: name of the car to move
        :param move_key: Key of move in car to activate
        :return: True upon success, False otherwise
        """
        # implement your code and erase the "pass"
        pass

    def _is_valid_coordinate(self, coordinate):
        """
        Validates the given coordinate with the board.
        :return: True for valid, False for invalid
        """
        for index in coordinate:
            if index >= Board.BOARD_SIZE or index < 0:
                return False
        return True

board = Board()
print(board.cell_content((99,4)))