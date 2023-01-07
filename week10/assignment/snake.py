#################################################################
# FILE : board.py
# WRITER : Nimrod M.
# EXERCISE : intro2cs1 ex10 2023
# DESCRIPTION: Implements the Snake for the Snake Game
# STUDENTS I DISCUSSED THE EXERCISE WITH: N/A
# WEB PAGES I USED: N/A
# NOTES: N/A
#################################################################

from typing import List
from game_display import GameDisplay
from common import BaseGameObject, Coordinate, Direction, draw_coordinates

class Snake(BaseGameObject):
    """
    """

    def __init__(self, location: Coordinate, length: int) -> None:
        # The coordinates which the snake occupies, the order of this list is
        #   integral to the operation of the object
        super().__init__(self._get_initial_position(location, length), "black")

        self._current_direction = Direction.UP

    def __str__(self) -> str:
        """
        Prints the Snake's Coordinates
        Primarily used for debugging matters.
        """
        return str(self._coordinates)

    def get_coordinates(self) -> List[Coordinate]:
        """
        """
        return self._coordinates

    def movement_requirements(self, direction: Direction) -> Coordinate:
        """
        Returns the requirements for the given direction regardless of 
        whether it is valid or invalid (e.g. if the current direction is
        left and this function is given right)
        """
        head = self._coordinates[0] # The head element of the snake
        if Direction.LEFT == direction:
            return Coordinate(head.row, head.column-1)
        elif Direction.RIGHT == direction:
            return Coordinate(head.row, head.column+1)
        elif Direction.UP == direction:
            return Coordinate(head.row+1, head.column)
        else: # Direction is Down
            return Coordinate(head.row-1, head.column)

    def move(self, direction: Direction, expand=False) -> bool:
        """
        """
        # Checking if the direction is in the valid directions 
        #   for the current snake orientation
        if direction not in self._get_valid_directions():
            return False

        new_coordinate = self.movement_requirements(direction)
        self._coordinates.insert(0, new_coordinate) # Adding the new head
        if not expand: # If expanding the snake length is not necessary, remove the tail element
            self._coordinates.pop() # Removing the last element (the tail)

        # Updating the current direction
        self._current_direction = direction

        return True

    def _get_valid_directions(self) -> List[Direction]:
        """
        """
        if (Direction.LEFT == self._current_direction) or \
                (Direction.RIGHT == self._current_direction):
            return [Direction.UP, Direction.DOWN, self._current_direction]
        else: # Up or Down
            return [Direction.RIGHT, Direction.LEFT, self._current_direction]

    def _get_initial_position(self, head_location: Coordinate, length: int) -> List[Coordinate]:
        """
        """
        # Initializing the starting coordinates of the snake to be under the head location
        return [Coordinate(head_location.row-index, head_location.column) 
                    for index in range(length)]