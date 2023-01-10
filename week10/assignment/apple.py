#################################################################
# FILE : apple.py
# WRITERS : Nimrod M. ; Dor K.
# EXERCISE : intro2cs1 ex10 2023
# DESCRIPTION: Implements the Apple for the Snake Game
# STUDENTS I DISCUSSED THE EXERCISE WITH: N/A
# WEB PAGES I USED: N/A
# NOTES: N/A
#################################################################

from common import BaseGameObject, Coordinate

class Apple(BaseGameObject):
    """
    Represents an Apple object in the Snake Game.
    This class is used only for matters of interaction
        and it implements no special functionality.
    """

    def __init__(self, coordinate: Coordinate) -> None:
        """
        Creates a new apple in the given coordinate.
        Yes, it's a single coordinate, no oversized apples in this realm.
        """
        super().__init__([coordinate], "green")

    def movement_requirements(self):
        """
        Filler function because the interface must have this implemented.
        """
        return None
    
    def move(self) -> bool:
        """
        Filler function because the interface must have this implemented.
        """
        return True
