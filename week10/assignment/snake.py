#################################################################
# FILE : board.py
# WRITER : Nimrod M.
# EXERCISE : intro2cs1 ex10 2023
# DESCRIPTION: Implements the Snake for the Snake Game
# STUDENTS I DISCUSSED THE EXERCISE WITH: N/A
# WEB PAGES I USED: N/A
# NOTES: N/A
#################################################################

from common import BaseGameObject, Coordinate, Direction
from typing import List

class Snake(BaseGameObject):
    """
    """

    def __init__(self, location: Coordinate, length: int) -> None:
        super().__init__()

        self._coordinates = self._get_initial_position(location, length)
        self._head = location
        # Relying on the fact that it is a sorted coordinate list, 
        #   should be relied upon here ONLY!
        self._tail = self._coordinates[-1]
        self._current_direction = Direction.UP

    def _get_initial_position(self, head_location: Coordinate, length: int) -> List[Coordinate]:
        """
        """
        # Initializing the starting coordinates of the snake to be under the head location
        return [Coordinate(head_location.row+index, head_location.column) 
                    for index in range(length)]

    def get_coordinates(self) -> List[Coordinate]:
        """
        """
        return self._coordinates

    def expand(self):
        """
        """
        self._coordinates.append()

    def move(self, direction) -> bool:
        """
        """
        pass

a = Snake(Coordinate(4,5), 3)
for coordinate in a.get_coordinates():
    print(coordinate)
print(a._head, a._tail)