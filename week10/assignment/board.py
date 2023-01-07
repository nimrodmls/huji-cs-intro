#################################################################
# FILE : board.py
# WRITER : Nimrod M.
# EXERCISE : intro2cs1 ex10 2023
# DESCRIPTION: Implements the game board for the Snake Game
# STUDENTS I DISCUSSED THE EXERCISE WITH: N/A
# WEB PAGES I USED: N/A
# NOTES: N/A
#################################################################

from typing import List, Callable
from game_display import GameDisplay
from common import Coordinate, BaseGameObject, Direction
from snake import Snake

# Signature for the interaction callback, first game object is the source and
#   the second game object is the destination
InteractionCallback = Callable[[BaseGameObject, BaseGameObject], None]

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
        for game_object in self._get_game_objects():
            game_object.draw_object(gui)

    def add_object(self, board_object: BaseGameObject) -> bool:
        """
        """
        pass

    def remove_object(self, board_object: BaseGameObject):
        """
        """
        

    def _get_game_objects(self) -> List[BaseGameObject]:
        """
        """
        return self._walls + self._apples + [self._snake]

    def _get_object_at_coordinate(self, coordinate: Coordinate) -> BaseGameObject:
        """
        """
        for game_object in self._get_game_objects():
            if coordinate in game_object.get_coordinates():
                return game_object

    def _is_in_boundries(self, coordinate: Coordinate) -> bool:
        """
        """
        # Checking the row coordinate is within the boundries
        if coordinate.row > self._dimensions.row or coordinate.row < 0:
            return False

        # Checking the column coordinate is within the boundries
        if coordinate.column > self._dimensions.column or coordinate.column < 0:
            return False 

        return True

    def move_snake(self, direction: Direction, expand: bool, interaction_callback: InteractionCallback) -> bool:
        """
        """
        requirement = self._snake.movement_requirements(direction)
        in_boundries = self._is_in_boundries(requirement)
        
        # If the requested coordinate is within the board, then check
        #   if there is another object at the requested coordinate,
        #   and in case there is, then let the caller know via the interaction_callback
        if in_boundries:
            destination_obj = self._get_object_at_coordinate(requirement)
            if destination_obj is not None:
                interaction_callback(self._snake, destination_obj)

        # Whether inside or outside the boundries, we try to move, 
        #   the game object will decide if it should end the game
        # Not checking the return value on purpose, we've nothing to do with it
        self._snake.move(direction, expand)

        return in_boundries
