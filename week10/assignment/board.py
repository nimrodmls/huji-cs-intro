#################################################################
# FILE : board.py
# WRITERS : Nimrod M. ; Dor K.
# EXERCISE : intro2cs1 ex10 2023
# DESCRIPTION: Implements the game board for the Snake Game
# STUDENTS I DISCUSSED THE EXERCISE WITH: N/A
# WEB PAGES I USED: N/A
# NOTES: N/A
#################################################################

from typing import List, Callable
from game_display import GameDisplay
from common import Coordinate, BaseGameObject, is_in_boundries, draw_coordinates

# Signature for the interaction callback, first game object is the source and
#   the second game object is the destination
InteractionCallback = Callable[[BaseGameObject, BaseGameObject], None]
OutOfBoundsCallback = Callable[[BaseGameObject, bool], bool]

class Board(object):
    """
    """

    def __init__(self, dimensions: Coordinate) -> None:
        """
        """
        self._dimensions = dimensions
        self._game_objects: List[BaseGameObject] = []

    def draw_board(self, gui: GameDisplay):
        """
        """
        priority_draw = []
        priority_color = "blue"
        for game_object in self._game_objects:
            if priority_color == game_object.get_object_color:
                priority_draw.append(game_object.get_coordinates())
            else:
                draw_coordinates(gui, self._dimensions, game_object.get_coordinates(), game_object.get_object_color())
        for coords in priority_draw:
            draw_coordinates(gui, self._dimensions, coords, priority_color)

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
        interactions = []
        out_of_bounds = []
        for game_object in self._game_objects:
            requirement = game_object.movement_requirements()
            # If the game object can move and the requirements are satisfied
            if requirement is not None and self._is_in_boundries(requirement):
                destination_obj =  self._get_object_at_coordinate(requirement)

                # If there is a game object at the destination, interact with it
                if game_object.move() and destination_obj is not None:
                    #interaction_callback(game_object, destination_obj)
                    interactions.append((game_object, destination_obj))
            
            elif requirement is not None and not self._is_in_boundries(requirement):
                game_object.move()

                out_of_bounds.append(game_object)
                # out_of_bounds_callback(game_object,
                #                        self._is_off_board(
                #                              game_object.get_coordinates()))
        for object1, object2 in interactions:
            interaction_callback(object1, object2)
        for object1 in out_of_bounds:
            out_of_bounds_callback(object1, self._is_off_board(object1.get_coordinates()))

    def _is_interacting(self, object1, object2):
        """
        """
        for coordinate in object1.get_coordinates():
            if coordinate in object2.get_coordinates():
                return True
        return False

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
