#################################################################
# FILE : common.py
# WRITERS : Nimrod M. ; Dor K.
# EXERCISE : intro2cs1 ex10 2023
# DESCRIPTION: Common functionality for use around the codebase
# STUDENTS I DISCUSSED THE EXERCISE WITH: N/A
# WEB PAGES I USED: N/A
# NOTES: N/A
#################################################################

from typing import List, Tuple
from game_display import GameDisplay

class Direction(object):
    """
    Used as an Enum for Directions
    """
    LEFT = "Left"
    RIGHT = "Right"
    UP = "Up"
    DOWN = "Down"

    Directions = [LEFT, RIGHT, UP, DOWN]

class Coordinate(object):
    """
    Represents a coordinate in a Two-Dimensional Coordinate System
    """

    def __init__(self, row: int, column: int) -> None:
        """
        Initializes the coordinate with the given Y (row) and X (column) values
        """
        # Attributes are intentionally public, to refrain from getter/setter functions
        self.row = row
        self.column = column

    @staticmethod
    def from_legacy_coordinate(legacy_coordinate: Tuple[int, int]):
        """
        Creating a Coordinate from a legacy (X, Y) Tuple Coordinate
        """
        return Coordinate(legacy_coordinate[1], legacy_coordinate[0])

    def __str__(self) -> str:
        """
        Prints the coordinates in (row, column) format
        """
        return "({row}, {column})".format(row=self.row, column=self.column)

    def __repr__(self) -> str:
        """
        Returns the coordinates in a string format (similar to __str__)
        """
        return self.__str__()

    def __eq__(self, other: object) -> bool:
        """
        Compares one coordinate to another.
        A coordinate is equal if both the row and column coordinates are exact.
        """
        if (other.row == self.row) and (other.column == self.column):
            return True
        return False
    
class BaseGameObject(object):
    """
    Represents a basic game object for the Snake Game.
    All game objects set on the board should inherit from this class
    and implement its functions
    """

    def __init__(self, coordinates: List[Coordinate], color: str) -> None:
        """
        Initializes the object.

        :param coordinates: List of coordinates occupied 
                            by the object on initialization.
        :param color: The color of the object when shown graphically.
        """
        self._coordinates = coordinates
        self._color = color

    def __str__(self) -> str:
        """
        Prints the game object's Coordinates
        Primarily used for debugging matters.
        """
        return str(self._coordinates)

    def __len__(self) -> int:
        """
        Returns the length of the object.
        The length is how many cells the object occupies 
        in a two dimensional coordinate system.
        
        Builtin len() function should be used.
        """
        return len(self._coordinates)

    def get_object_color(self):
        """
        Returns the color of the object.
        """
        return self._color
        
    def get_coordinates(self) -> List[Coordinate]:
        """
        Returns the coordinates the object occupies.
        """
        return self._coordinates

    def movement_requirements(self) -> Coordinate:
        """
        Relevant mostly for moving game objects.
        Should specify the coordinate the game object
        requires to be empty before moving.

        Calling this directly will throw
        NotImplementedError Exception.
        """
        raise NotImplementedError

    def move(self) -> bool:
        """
        Relevant mostly for moving game objects.
        Should move the object in any way seem fit.
        
        Calling this directly will throw
        NotImplementedError Exception.
        """
        raise NotImplementedError

class BaseDynamicGameObject(BaseGameObject):
    """
    Represents a dynamic game object, which is on the move during the game.
    This is an addition over the regular BaseGameObject in a manner which
    allows easier interface for more complicated moving objects.
    """

    def __init__(self, starting_direction, coordinates: List[Coordinate], color: str) -> None:
        """
        Initializes the object with the given starting direction,
        coordinates occupied by the object, and the color of the object on display.
        """
        super().__init__(coordinates, color)

        self._current_direction = starting_direction

    def movement_requirements(self) -> Coordinate:
        """
        Returns the requirements for the given direction regardless of 
        whether it is valid or invalid (e.g. if the current direction is
        left and this function is given right)
        """
        head = self._coordinates[0] # The head element
        if Direction.LEFT == self._current_direction:
            return Coordinate(head.row, head.column-1)
        elif Direction.RIGHT == self._current_direction:
            return Coordinate(head.row, head.column+1)
        elif Direction.UP == self._current_direction:
            return Coordinate(head.row+1, head.column)
        else: # Direction is Down
            return Coordinate(head.row-1, head.column)

class SnakeException(Exception):
    """
    Generic exception for the Snake Package.
    """
    pass

def is_in_boundries(height: int, width: int, coordinate: Coordinate) -> bool:
    """
    Checks if a coordinate is within the given height X width dimensions.
    """
    # Checking the row coordinate is within the boundries
    if coordinate.row >= height or coordinate.row < 0:
        return False

    # Checking the column coordinate is within the boundries
    if coordinate.column >= width or coordinate.column < 0:
        return False 

    return True

def draw_coordinates(gui: GameDisplay, coordinates: List[Coordinate], color) -> None:
    """
    Draws a list of coordinates on a game display, with the given color.
    """
    for coordinate in coordinates:
        # Only if the coordinate is within the display board draw it
        if is_in_boundries(gui.height, gui.width, coordinate):
            gui.draw_cell(coordinate.column, coordinate.row, color)
