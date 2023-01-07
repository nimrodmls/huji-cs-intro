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

    def movement_requirements(self):
        """
        """
        raise NotImplementedError

    def move(self):
        """
        """
        raise NotImplementedError

    def interact(self, snake_game, source):
        """
        snake_game should be a SnakeGame object, 
        it is not typed in order to prevent circular dependencies
        """
        raise NotImplementedError

def draw_coordinates(gui: GameDisplay, coordinates: List[Coordinate], color) -> None:
    """
    """
    for coordinate in coordinates:
        gui.draw_cell(coordinate.column, coordinate.row, color)
