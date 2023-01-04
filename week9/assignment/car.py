#################################################################
# FILE : car.py
# WRITER : Nimrod M.
# EXERCISE : intro2cs1 ex9 2023
# DESCRIPTION: Implementing the Car for Rush Hour Game
# STUDENTS I DISCUSSED THE EXERCISE WITH: N/A
# WEB PAGES I USED: N/A
# NOTES: N/A
#################################################################

class Car:
    """
    Add class description here
    """

    COORDINATE_ROW_INDEX = 0
    COORDINATE_CELL_INDEX = 1

    VERTICAL_ORIENTATION = 0
    HORIZONTAL_ORIENTATION = 1

    MOVE_KEY_UP = 'u'
    MOVE_KEY_DOWN = 'd'
    MOVE_KEY_RIGHT = 'r'
    MOVE_KEY_LEFT = 'l'

    def __init__(self, name, length, location, orientation):
        """
        A constructor for a Car object
        :param name: A string representing the car's name
        :param length: A positive int representing the car's length.
        :param location: A tuple representing the car's head (row, col) location
        :param orientation: One of either 0 (VERTICAL) or 1 (HORIZONTAL)
        """
        self._name = name
        self._length = length
        self._location = location
        self._orientation = orientation

    def car_coordinates(self):
        """
        :return: A list of coordinates the car is in
        """
        head_row = self._location[Car.COORDINATE_ROW_INDEX]
        head_column = self._location[Car.COORDINATE_CELL_INDEX]

        if self._orientation is Car.VERTICAL_ORIENTATION:
            return [(head_row + index, head_column) for index in range(self._length)]

        else: # Horizontal orientation
            return [(head_row, head_column + index) for index in range(self._length)]

    def possible_moves(self):
        """
        :return: A dictionary of strings describing possible movements permitted by this car.
        """
        if self._orientation is Car.VERTICAL_ORIENTATION:
            return {
                Car.MOVE_KEY_DOWN: "The car will go one cell downwards",
                Car.MOVE_KEY_UP: "The car will go one cell upwards"
            }

        else: # Horizontal orientation
            return {
                Car.MOVE_KEY_RIGHT: "The car will go one cell to the right",
                Car.MOVE_KEY_LEFT: "The car will go one cell to the left"
            }

    def movement_requirements(self, move_key):
        """ 
        :param move_key: A string representing the key of the required move.
        :return: A list of cell locations which must be empty in order for this move to be legal.
        """
        head_row = self._location[Car.COORDINATE_ROW_INDEX]
        head_column = self._location[Car.COORDINATE_CELL_INDEX]

        if move_key is Car.MOVE_KEY_LEFT:
            return [(head_row, head_column - 1)]
        elif move_key is Car.MOVE_KEY_RIGHT:
            return [(head_row, head_column + self._length)]
        elif move_key is Car.MOVE_KEY_DOWN:
            return [(head_row + self._length, head_column)]
        elif move_key is Car.MOVE_KEY_UP:
            return [(head_row - 1, head_column)]

    def move(self, move_key):
        """ 
        :param move_key: A string representing the key of the required move.
        :return: True upon success, False otherwise
        """
        head_row = self._location[Car.COORDINATE_ROW_INDEX]
        head_column = self._location[Car.COORDINATE_CELL_INDEX]

        moves = {}
        if self._orientation is Car.VERTICAL_ORIENTATION:
            moves = {
                Car.MOVE_KEY_DOWN: (head_row + 1, head_column),
                Car.MOVE_KEY_UP: (head_row - 1, head_column),
            }
        else: # Horizontal Orientation
            moves = {
                Car.MOVE_KEY_LEFT: (head_row, head_column - 1),
                Car.MOVE_KEY_RIGHT: (head_row, head_column + 1)
            }

        if move_key not in moves:
            return False

        self._location = moves[move_key]
        return True

    def get_name(self):
        """
        :return: The name of this car.
        """
        return self._name
