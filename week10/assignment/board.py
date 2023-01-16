#################################################################
# FILE : board.py
# WRITERS : Nimrod M. ; Dor K.
# EXERCISE : intro2cs1 ex10 2023
# DESCRIPTION: Implements the game board for the Snake Game
# STUDENTS I DISCUSSED THE EXERCISE WITH: N/A
# WEB PAGES I USED: N/A
# NOTES: N/A
#################################################################

from typing import List, Callable, Optional
from game_display import GameDisplay
from common import Coordinate, BaseGameObject, is_in_boundries, draw_coordinates

# Signature for the interaction callback, first game object is the source and
#   the second game object is the destination
InteractionCallback = Callable[[BaseGameObject, BaseGameObject], None]
# Signature for the out of bounds callback, called upon interaction of an object
#   with the Board's boundries. The boolean parameter is a flag for whether the whole
#   object went outside the boundries
OutOfBoundsCallback = Callable[[BaseGameObject, bool], bool]

class Board(object):
    """
    Represents the Game Board for Snake.
    The Board houses generic game objects and is responsible for their state
    and interaction with the board.
    """

    def __init__(self, dimensions: Coordinate) -> None:
        """
        Creates a new board with the given rows X columns dimensions.
        """
        self._dimensions: Coordinate = dimensions
        self._game_objects: List[BaseGameObject] = []

    def draw_board(self, gui: GameDisplay) -> None:
        """
        Draws the board to the given Game Display.
        The board assumes the Game Display is of the same dimensions
        as the Board itself.
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
        Adds the game obejct to the board
        If the object shares coordinates with another object already placed
        on the board, the method will fail and return False, True otherwise.
        """
        # Making sure the object doesn't overlap with any other object first
        for coordinate in game_object.get_coordinates():
            if self._get_object_at_coordinate(coordinate) is not None:
                return False
                
        self._game_objects.append(game_object)
        return True 

    def remove_game_object(self, game_object: BaseGameObject) -> None:
        """
        Removing the game object from the board, if it exists
        """
        # If the object is not on the board, don't even try to remove it
        if game_object in self._game_objects:
            self._game_objects.remove(game_object)

    def move_game_objects(self, 
                          interaction_callback: InteractionCallback,
                          out_of_bounds_callback: OutOfBoundsCallback) -> bool:
        """
        Moving all game objects one after the other, then checks if any
        object interacts with another, if so, interaction_callback is called.
        If an object interacts with the boundries of the border,
        out_of_bounds_callback is called.
        """
        interactions = []
        interactions = {}
        out_of_bounds = []

        # Iterating on all objects and moving them
        for game_object in self._game_objects:
            requirement = game_object.movement_requirements()
            # If the game object can move and the requirements are satisfied
            if requirement is not None and self._is_in_boundries(requirement):
                destination_obj =  self._get_object_at_coordinate(requirement)

                # If there is a game object at the destination, 
                #   add to possible interactions, it will be checked later if the
                #   interaction is still relevant after all objects moved
                if game_object.move() and destination_obj is not None:
                    #interactions.append((game_object, destination_obj))
                    interactions[(requirement.column, requirement.row)] = (game_object, destination_obj)

            # If the game object is moving out of bounds, let the caller know            
            elif requirement is not None and not self._is_in_boundries(requirement):
                game_object.move()
                out_of_bounds.append(game_object)

        # Executing interaction between the objects
        for coordinate in interactions:
            # Making sure after the movement that the objects still interact with eachother
            if Coordinate.from_legacy_coordinate(coordinate) in interactions[coordinate][1].get_coordinates():
                if interactions[coordinate][0] is interactions[coordinate][1] and self._is_hitting_itself(interactions[coordinate][0]):
                    interaction_callback(interactions[coordinate][0], interactions[coordinate][1])
                elif interactions[coordinate][0] is not interactions[coordinate][1]:
                    interaction_callback(interactions[coordinate][0], interactions[coordinate][1])

        # Executing interaction between objects to the board boundries
        for object1 in out_of_bounds:
            out_of_bounds_callback(object1, self._is_off_board(object1.get_coordinates()))

    def _is_hitting_itself(self, object1: BaseGameObject):
        """
        """
        coordinates = object1.get_coordinates()
        # If the object has no coordinates, we shouldn't check anything
        if 0 == len(coordinates):
            return False
        # If the object has a coordinate twice, then it hit itself
        if 1 != coordinates.count(coordinates[0]):
            return True

        return False

    def _is_interacting(self, coordinate, object1: BaseGameObject, object2: BaseGameObject) -> bool:
        """
        Returns whether the two objects interact with each other
        (e.g. share some coordinate(s) at the given moment)
        """
        for coordinate in object1.get_coordinates():
            if coordinate in object2.get_coordinates():
                return True
        return False

    def _get_object_at_coordinate(self, coordinate: Coordinate) -> Optional[BaseGameObject]:
        """
        Returns the object residing in the requested coordinate.
        If no object exists at the specified coordinate None is returned.
        """
        for game_object in self._game_objects:
            if coordinate in game_object.get_coordinates():
                return game_object

        return None # No object at the specified coordinate

    def _is_off_board(self, coordinates: List[Coordinate]) -> bool:
        """
        Checks if the given coordinates are completely off the game board
        (e.g. none of the coordinates are within the board's boundries)
        Returns True if all are off board, False if at least one is on board.
        """
        for coordinate in coordinates:
            # Checking if at least one coordinate is on the board
            if self._is_in_boundries(coordinate):
                return False
        return True

    def _is_in_boundries(self, coordinate: Coordinate) -> bool:
        """
        Checks if the given coordinate is within the board's boundries.
        Returns True if exists, False otherwise.
        """
        return is_in_boundries(self._dimensions.row, self._dimensions.column, coordinate)
