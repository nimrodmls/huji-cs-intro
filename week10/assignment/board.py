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
        self._game_objects: List[BaseGameObject] = [snake]

    def draw_board(self, gui: GameDisplay):
        """
        """
        for game_object in self._game_objects:
            game_object.draw_object(gui)

    def add_game_object(self, game_object: BaseGameObject) -> bool:
        """
        """
        self._game_objects.append(game_object)

    def remove_game_object(self, game_object: BaseGameObject):
        """
        """
        self._game_objects.remove(game_object)

    def _get_object_at_coordinate(self, coordinate: Coordinate) -> BaseGameObject:
        """
        """
        for game_object in self._game_objects:
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

    def move_game_objects(self, interaction_callback: InteractionCallback) -> bool:
        """
        """
        for game_object in self._game_objects:
            requirement = game_object.movement_requirements()
            # If the game object can move and the requirements are satisfied
            if requirement is not None and self._is_in_boundries(requirement):

                # If there is a game object at the destination, interact with it
                destination_obj = self._get_object_at_coordinate(requirement)
                if destination_obj is not None:
                    interaction_callback(game_object, destination_obj)

                game_object.move()
