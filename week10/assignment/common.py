#################################################################
# FILE : common.py
# WRITER : Nimrod M.
# EXERCISE : intro2cs1 ex10 2023
# DESCRIPTION: Common functionality for use around the codebase
# STUDENTS I DISCUSSED THE EXERCISE WITH: N/A
# WEB PAGES I USED: N/A
# NOTES: N/A
#################################################################

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
    
class BaseGameObject(object):
    """
    """

    def interact(self, snake_game):
        """
        """
        raise NotImplementedError
