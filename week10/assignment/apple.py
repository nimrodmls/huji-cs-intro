#################################################################
# FILE : board.py
# WRITER : Nimrod M.
# EXERCISE : intro2cs1 ex10 2023
# DESCRIPTION: Implements the Apple for the Snake Game
# STUDENTS I DISCUSSED THE EXERCISE WITH: N/A
# WEB PAGES I USED: N/A
# NOTES: N/A
#################################################################

from common import BaseGameObject, Coordinate
from snake import Snake

class Apple(BaseGameObject):
    """
    """

    def __init__(self, coordinate: Coordinate) -> None:
        super().__init__([coordinate], "green")

    def movement_requirements(self):
        """
        """
        return None
    
    def move(self) -> None:
        """
        """
        return None
