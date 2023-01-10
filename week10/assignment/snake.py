#################################################################
# FILE : snake.py
# WRITERS : Nimrod M. ; Dor K.
# EXERCISE : intro2cs1 ex10 2023
# DESCRIPTION: Implements the Snake for the Snake Game
# STUDENTS I DISCUSSED THE EXERCISE WITH: N/A
# WEB PAGES I USED: N/A
# NOTES: N/A
#################################################################

from typing import List
from common import BaseDynamicGameObject, Coordinate, Direction, SnakeException

class TerminatingSnakeSplit(SnakeException):
    """
    Exception raised upon Snake Object being split to death
    """
    pass

class Snake(BaseDynamicGameObject):
    """
    Represents the Snake Game Object in the game.
    The object is intended to be placed on a board, although it's not mandatory.
    """

    def __init__(self, location: Coordinate, length: int = 3) -> None:
        """
        Creates a new Snake with its head in the given coordinate and initial given length.
        The Snake starts at an upwards orientation, with the starting coordinates being
        from head to the tail perpendicular to the X-Axis.
        """
        # The coordinates which the snake occupies, the order of this list is
        #   integral to the operation of the object
        super().__init__(Direction.UP, self._get_initial_position(location, length), "black")
        self._expansion = 0
        self._to_split = None

    def move(self) -> bool:
        """
        Moving the Snake in the set direction.
        To set the direction use change_direction.

        If the Snake is during expansion phase, it will not empty
        the coordinates it occupies until the expansion phase is done.
        (e.g. the tail is not removed during this phase)
        """
        if self._to_split is not None:             
            self._coordinates = self._coordinates[:self._to_split]
            self._to_split = None
        
        new_coordinate = self.movement_requirements()
        self._coordinates.insert(0, new_coordinate) # Adding the new head

        # If expanding the snake length is not necessary, remove the tail element
        if 0 == self._expansion:
            self._coordinates.pop() # Removing the last element (the tail)
        else: # Otherwise, expand by 1 and decrement the expanion ratio
            self._expansion -= 1

        # Moving the snake cannot fail
        return True

    def change_direction(self, direction: Direction) -> bool:
        """
        Changes the direction the snake is moving to.
        If the direction is invalid False is returned, True otherwise.
        """
        # Checking if the direction is in the valid directions 
        #   for the current snake orientation
        if direction not in self._get_valid_directions():
            return False

        # Updating the current direction
        self._current_direction = direction
        return True

    def expand(self, amount: int) -> None:
        """
        Ordering the Snake to expand on the next moves by the given amount.
        Expansion process is taking 'amount' of calls to move to fully complete.
        """
        self._expansion += amount

    def split(self, coordinate: Coordinate) -> None:
        """
        Ordering the Snake to split part of its body from the given
        coordinate (included) to the tail
        Raises TerminatingSnakeSplit if the split is causing the Snake to terminate.
        """
        self._to_split = self._coordinates.index(coordinate)
        if self._to_split in [0,1]:
            raise TerminatingSnakeSplit

    def _get_valid_directions(self) -> List[Direction]:
        """
        Returns the valid directions for the snake to move at its current orientation.
        It is not permitted for the snake to move down (up) if it's oriented up (down)
        or to move left (right) if it's oriented right (left).
        """
        if (Direction.LEFT == self._current_direction) or \
                (Direction.RIGHT == self._current_direction):
            return [Direction.UP, Direction.DOWN, self._current_direction]
        else: # Up or Down
            return [Direction.RIGHT, Direction.LEFT, self._current_direction]

    def _get_initial_position(self, head_location: Coordinate, length: int) -> List[Coordinate]:
        """
        Returns the initial coordinates considering the location of the head and length.
        The function expects that the snake would be oriented UPWARDS.
        """
        # Initializing the starting coordinates of the snake to be under the head location
        return [Coordinate(head_location.row-index, head_location.column) 
                    for index in range(length)]