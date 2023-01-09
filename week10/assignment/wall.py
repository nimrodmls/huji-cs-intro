#################################################################
# FILE : board.py
# WRITERS : Nimrod M. ; Dor K.
# EXERCISE : intro2cs1 ex10 2023
# DESCRIPTION: Implements the Wall for the Snake Game
# STUDENTS I DISCUSSED THE EXERCISE WITH: N/A
# WEB PAGES I USED: N/A
# NOTES: N/A
#################################################################

from typing import List
from common import BaseDynamicGameObject, Coordinate, Direction

class Wall(BaseDynamicGameObject):
    """
    """

    def __init__(self, location: Coordinate, direction: Direction, move_callback) -> None:
        """
        The received location is a coordinate of where the middle of the wall lies.
        """
        super().__init__(direction, self._get_initial_position(location, direction), "blue")
        self._move_callback = move_callback

    def move(self) -> bool:
        """
        """
        # Check if moving is permitted before actually moving
        if self._move_callback():
            self._coordinates.insert(0, self.movement_requirements()) # Adding the new head
            self._coordinates.pop() # Removing the last element (the tail)
            return True
        return False # If no movement made, return so

    def _get_initial_position(
        self, mid_location: Coordinate, direction: Direction) -> List[Coordinate]:
        """
        """
        if direction == Direction.UP:
            return [Coordinate(mid_location.row+row_index, mid_location.column) 
                        for row_index in range(1, -2, -1)]
        elif direction == Direction.DOWN:
            return [Coordinate(mid_location.row+row_index, mid_location.column) 
                        for row_index in range(-1, 2)]
        elif direction == Direction.LEFT:
            return [Coordinate(mid_location.row, mid_location.column+column_index) 
                        for column_index in range(-1, 2)]
        elif direction == Direction.RIGHT:
            return [Coordinate(mid_location.row, mid_location.column+column_index) 
                        for column_index in range(1, -2, -1)]
