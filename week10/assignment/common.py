#################################################################
# FILE : common.py
# WRITER : Nimrod M.
# EXERCISE : intro2cs1 ex10 2023
# DESCRIPTION: Common functionality for use around the codebase
# STUDENTS I DISCUSSED THE EXERCISE WITH: N/A
# WEB PAGES I USED: N/A
# NOTES: N/A
#################################################################

from snake_game import SnakeGame

class Direction(object):
    """
    Used as an Enum for Directions
    """
    LEFT = "Left"
    RIGHT = "Right"
    UP = "Up"
    DOWN = "Down"

class Coordinate(object):
    """
    """

    def __init__(self, row: int, column: int) -> None:
        """
        """
        # Intentionally public, to refrain from getter/setter functions
        self.row = row
        self.column = column

    def __str__(self):
        """
        Prints the coordinates in (row, column) format
        """
        return "({row}, {column})".format(row=self.row, column=self.column)
    
class BaseGameObject(object):
    """
    """

    def interact(self, snake_game: SnakeGame):
        """
        """
        raise NotImplementedError
