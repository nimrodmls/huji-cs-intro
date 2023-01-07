#################################################################
# FILE : puzzle_solver.py
# WRITER : Nimrod M.
# EXERCISE : intro2cs1 ex10 2023
# DESCRIPTION: Common functionality for use around the codebase
# STUDENTS I DISCUSSED THE EXERCISE WITH: N/A
# WEB PAGES I USED: N/A
# NOTES: N/A
#################################################################

from snake_game import SnakeGame

class Coordinate(object):
    """
    """

    def __init__(self, row: int, column: int):
        """
        """
        # Intentionally public, to refrain from getter/setter functions
        self.row = row
        self.column = column
    
class BaseGameObject(object):
    """
    """

    def interact(self, snake_game: SnakeGame):
        """
        """
        raise NotImplementedError
