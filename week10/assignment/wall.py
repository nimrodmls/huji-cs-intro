#################################################################
# FILE : board.py
# WRITER : Nimrod M.
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

    def __init__(self, location: Coordinate, direction: Direction, length: int = 3) -> None:
        """
        """
        super().__init__(coordinates, color)

    def _get_initial_position(self, head_location: Coordinate, direction: Direction) -> List[Coordinate]:
        """
        """
        pass