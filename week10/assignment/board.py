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
from common import Coordinate, BaseGameObject, is_in_boundries
from snake import Snake

# Signature for the interaction callback, first game object is the source and
#   the second game object is the destination
InteractionCallback = Callable[[BaseGameObject, BaseGameObject], None]
OutOfBoundsCallback = Callable[[BaseGameObject, bool], bool]

class Board(object):
    """
    """

    def __init__(self, snake: Snake, dimensions: Coordinate) -> None:
        """
        """
        self._dimensions = dimensions
        self._game_objects: List[BaseGameObject] = [snake] if snake is not None else []

    def draw_board(self, gui: GameDisplay):
        """
        """
        for game_object in self._game_objects:
            game_object.draw_object(gui)

    def add_game_object(self, game_object: BaseGameObject) -> bool:
        """
        """
        # Making sure the object doesn't overlap with any other object first
        for coordinate in game_object.get_coordinates():
            if self._get_object_at_coordinate(coordinate) is not None:
                return False
                
        self._game_objects.append(game_object)
        return True 

    def remove_game_object(self, game_object: BaseGameObject) -> None:
        """
        """
        # If the object is not on the board, don't even try to remove it
        if game_object in self._game_objects:
            self._game_objects.remove(game_object)

    def move_game_objects(self, 
                          interaction_callback: InteractionCallback,
                          out_of_bounds_callback: OutOfBoundsCallback) -> bool:
        """
        """
        for game_object in self._game_objects:
            requirement = game_object.movement_requirements()
            # If the game object can move and the requirements are satisfied
            if requirement is not None and self._is_in_boundries(requirement):
                destination_obj =  self._get_object_at_coordinate(requirement)
                game_object.move()
                
                # If there is a game object at the destination, interact with it
                if destination_obj is not None:
                    interaction_callback(game_object, destination_obj)
            
            elif requirement is not None and not self._is_in_boundries(requirement):
                game_object.move()

                out_of_bounds_callback(game_object,
                                       self._is_off_board(
                                             game_object.get_coordinates()))

    def _get_object_at_coordinate(self, coordinate: Coordinate) -> BaseGameObject:
        """
        """
        for game_object in self._game_objects:
            if coordinate in game_object.get_coordinates():
                return game_object

        return None # No object at the specified coordinate

    def _is_off_board(self, coordinates: List[Coordinate]) -> bool:
        """
        """
        for coordinate in coordinates:
            # Checking if at least one coordinate is on the board
            if self._is_in_boundries(coordinate):
                return False
        return True

    def _is_in_boundries(self, coordinate: Coordinate) -> bool:
        """
        """
        return is_in_boundries(self._dimensions.row, self._dimensions.column, coordinate)
