#################################################################
# FILE : common.py
# WRITER : Nimrod M.
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
    """

    def __init__(self, row: int, column: int) -> None:
        """
        """
        # Intentionally public, to refrain from getter/setter functions
        self.row = row
        self.column = column

    @staticmethod
    def from_legacy_coordinate(legacy_coordinate: Tuple[int, int]):
        """
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
        if (other.row == self.row) and (other.column == self.column):
            return True
        return False
    
class BaseGameObject(object):
    """
    """
    def __init__(self, coordinates: List[Coordinate], color: str) -> None:
        """
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
        return len(self._coordinates)

    def draw_object(self, gui: GameDisplay) -> None:
        """
        """
        draw_coordinates(gui, self._coordinates, self._color)

    def get_coordinates(self) -> List[Coordinate]:
        """
        """
        return self._coordinates

    def movement_requirements(self) -> Coordinate:
        """
        """
        raise NotImplementedError

    def move(self) -> bool:
        """
        """
        raise NotImplementedError

    def interact(self, snake_game, source):
        """
        snake_game should be a SnakeGame object, 
        it is not typed in order to prevent circular dependencies
        """
        raise NotImplementedError

class BaseDynamicGameObject(BaseGameObject):
    """
    """
    def __init__(self, starting_direction, coordinates: List[Coordinate], color: str) -> None:
        super().__init__(coordinates, color)
        self._current_direction = starting_direction

    def movement_requirements(self) -> Coordinate:
        """
        Returns the requirements for the given direction regardless of 
        whether it is valid or invalid (e.g. if the current direction is
        left and this function is given right)
        """
        head = self._coordinates[0] # The head element of the snake
        if Direction.LEFT == self._current_direction:
            return Coordinate(head.row, head.column-1)
        elif Direction.RIGHT == self._current_direction:
            return Coordinate(head.row, head.column+1)
        elif Direction.UP == self._current_direction:
            return Coordinate(head.row+1, head.column)
        else: # Direction is Down
            return Coordinate(head.row-1, head.column)

def is_in_boundries(height: int, width: int, coordinate: Coordinate) -> bool:
    """
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
    """
    for coordinate in coordinates:
        # Only if the coordinate is within the display board draw it
        if is_in_boundries(gui.height, gui.width, coordinate):
            gui.draw_cell(coordinate.column, coordinate.row, color)
