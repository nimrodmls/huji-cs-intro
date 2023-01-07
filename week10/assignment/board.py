#################################################################
# FILE : board.py
# WRITER : Nimrod M.
# EXERCISE : intro2cs1 ex10 2023
# DESCRIPTION: Implements the game board for the Snake Game
# STUDENTS I DISCUSSED THE EXERCISE WITH: N/A
# WEB PAGES I USED: N/A
# NOTES: N/A
#################################################################

from game_display import GameDisplay
from common import Coordinate, BaseGameObject, Direction
from snake import Snake

class Board(object):
    """
    """

    def __init__(self, snake: Snake, dimensions: Coordinate) -> None:
        """
        """
        self._dimensions = dimensions
        self._snake = snake
        self._walls = []
        self._apples = []

    def draw_board(self, gui: GameDisplay):
        """
        """
        for game_object in (self._walls + self._apples + [self._snake]):
            game_object.draw_object(gui)

    def add_object(self, board_object: BaseGameObject) -> bool:
        """
        """
        pass

    def move_snake(self, direction: Direction, expand: bool, interaction_callback) -> bool:
        """
        """
        in_boundries = True
        requirement = self._snake.movement_requirements(direction)
        # Checking the row coordinate is within the boundries
        if requirement.row > self._dimensions.row or requirement.row < 0:
            in_boundries = False 

        # Checking the column coordinate is within the boundries
        if requirement.column > self._dimensions.column or requirement.column < 0:
            in_boundries = False 

        # Whether inside or outside the boundries, we try to move, 
        #   the game object will decide if it should end the game
        # Not checking the return value on purpose, we've nothing to do with it
        self._snake.move(direction, expand)

        return in_boundries
