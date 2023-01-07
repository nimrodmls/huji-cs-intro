#################################################################
# FILE : board.py
# WRITER : Nimrod M.
# EXERCISE : intro2cs1 ex10 2023
# DESCRIPTION: Implements the game board for the Snake Game
# STUDENTS I DISCUSSED THE EXERCISE WITH: N/A
# WEB PAGES I USED: N/A
# NOTES: N/A
#################################################################

from common import Coordinate, BaseGameObject
from snake import Snake

class Board(object):
    """
    """

    def __init__(self, snake: Snake, dimensions: Coordinate) -> None:
        """
        """
        self._dimensions = dimensions
        self._snake = snake

    def __str__(self):
        """
        Prints the game board to the screen
        """
        pass

    def add_object(self, board_object: BaseGameObject) -> bool:
        """
        """
        pass

    def move_snake(self, direction, interaction_callback) -> bool:
        """
        """
        pass
