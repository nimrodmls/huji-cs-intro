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
    
    MOVE_NAME_INDEX = 0
    MOVE_KEY_INDEX = 1
    MOVE_DESCRIPTION_INDEX = 2

    def __init__(self):
        """
        Initializes a new & empty board
        """
        self._board = [[Board.EMPTY_CELL_VALUE for cell_index in range(Board.BOARD_SIZE)] 
                            for row_index in range(Board.BOARD_SIZE)]
        self._cars = {}

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

    def _get_car_moves(self, car):
        """
        """
        all_moves = {}
        move_keys = car.possible_moves()
        # Iterating on each key from the possible moves of that car object 
        for move_key in move_keys:
            requirements = car.movement_requirements(move_key)
            # Checking the requirements for each key, and making sure each on is fulfilled
            #   if it is, then it's added to the result
            for requirement in requirements:
                if self.cell_content(requirement) is None:
                    all_moves[move_key] = move_keys[move_key]
        return all_moves

    def possible_moves(self):
        """
        This function returns the legal moves of all cars in this board
        :return: list of tuples of the form (name,move_key,description)
                 representing legal moves
        """
        all_moves = []
        # Iterating on all cars on the board
        for car in self._cars:
            current_moves = self._get_car_moves(car)
            for move in current_moves:
                all_moves.append((car.get_name(), move, current_moves[move]))
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
        :param coordinate: tuple of (row,col) of the coordinate to check
        :return: The name if the car in coordinate, None if empty
        """
        row_index = coordinate[Board.COORDINATE_ROW_INDEX]
        cell_index = coordinate[Board.COORDINATE_CELL_INDEX]
        cell_value = self._board[row_index][cell_index]

        return None if Board.EMPTY_CELL_VALUE == cell_value else cell_value

    def _update_board(self, value, new_coordinates, old_coordinates=None):
        """
        """
        # Emptying the old coordinates
        if old_coordinates is not None:
            for coordinate in old_coordinates:
                row_index = coordinate[Board.COORDINATE_ROW_INDEX]
                cell_index = coordinate[Board.COORDINATE_CELL_INDEX]
                self._board[row_index][cell_index] = Board.EMPTY_CELL_VALUE
        
        # Setting the new coordinates
        for coordinate in new_coordinates:
            row_index = coordinate[Board.COORDINATE_ROW_INDEX]
            cell_index = coordinate[Board.COORDINATE_CELL_INDEX]
            self._board[row_index][cell_index] = value

    def add_car(self, car):
        """
        Adds a car to the game.
        :param car: car object of car to add
        :return: True upon success. False if failed
        """
        # First we check that the coordinates are OK, 
        # only then we proceed to place the car on the board
        for coordinate in car.car_coordinates():
            if self.cell_content(coordinate) is not None:
                return False

        self._update_board(car.get_name(), car.car_coordinates())
        self._cars[car.get_name()] = car

        return True

    def move_car(self, name, move_key):
        """
        moves car one step in given direction.
        :param name: name of the car to move
        :param move_key: Key of move in car to activate
        :return: True upon success, False otherwise
        """
        # First checking if that car even exists in the records
        if name not in self._cars:
            return False

        current_car = self._cars[name]

        # Now finding out if that move_key is possible
        if move_key not in self._get_car_moves(current_car):
            return False 

        old_coordinates = set(current_car.car_coordinates())
        # Letting the car know that it should update its coordinates
        self._cars[name].move(move_key)

        # Updating the board accordingly
        new_coordinates = set(current_car.car_coordinates())
        self._update_board(current_car.get_name(), new_coordinates, old_coordinates)
        

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