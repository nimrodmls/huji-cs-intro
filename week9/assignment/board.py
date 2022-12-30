#################################################################
# FILE : board.py
# WRITER : Nimrod M.
# EXERCISE : intro2cs1 ex9 2023
# DESCRIPTION: Implementing the Board for Rush Hour Game
# STUDENTS I DISCUSSED THE EXERCISE WITH: N/A
# WEB PAGES I USED: N/A
# NOTES: N/A
#################################################################

import car

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
        self._cars = {}

    def __str__(self):
        """
        This function is called when a board object is to be printed.
        :return: A string of the current status of the board
        """
        # The game may assume this function returns a reasonable representation
        # of the board for printing, but may not assume details about it.
        # implement your code and erase the "pass"
        board = [[Board.EMPTY_CELL_VALUE for cell_index in range(Board.BOARD_SIZE)] 
                            for row_index in range(Board.BOARD_SIZE)]

        for car in self._cars:
            for coordinate in self._cars[car].car_coordinates():
                if coordinate in self.cell_list():
                    row_index = coordinate[Board.COORDINATE_ROW_INDEX]
                    cell_index = coordinate[Board.COORDINATE_CELL_INDEX]
                    board[row_index][cell_index] = self._cars[car].get_name()

        final_str = ""
        for row in board:
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
                if self._is_valid_coordinate(requirement) and self.cell_content(requirement) is None:
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
            current_moves = self._get_car_moves(self._cars[car])
            for move in current_moves:
                all_moves.append((self._cars[car].get_name(), move, current_moves[move]))
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
        for car in self._cars:
            if coordinate in self._cars[car].car_coordinates():
                return self._cars[car].get_name()
        return None

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

        self._cars[name].move(move_key)
        return True

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
new_car = car.Car("O", 3, (2, 0), car.Car.HORIZONTAL_ORIENTATION)
board.add_car(new_car)
print(board.move_car('o', 'r'))
print(board)
print(board.move_car('O', 'r'))
print(board)
print(board.move_car('O', 'r'))
print(board)
print(board.move_car('O', 'r'))
print(board)
print(board.move_car('O', 'r'))
print(board)
print(board.move_car('O', 'r'))
print(board)
print(car)