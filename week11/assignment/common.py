#################################################################
# FILE : common.py
# WRITER : Nimrod M. ; Ruth S.
# EXERCISE : intro2cs1 ex11 2023
# DESCRIPTION: Common functionality for the game
# STUDENTS I DISCUSSED THE EXERCISE WITH: N/A
# WEB PAGES I USED: N/A
# NOTES: N/A
#################################################################

from typing import Tuple

LegacyCoordinate = Tuple[int, int]

class Coordinate(object):
    """
    Represents a coordinate in a Two-Dimensional Coordinate System
    """

    def __init__(self, row: int, column: int) -> None:
        """
        Initializes the coordinate with the given Y (row) and X (column) values
        """
        # Attributes are intentionally public, to refrain from getter/setter functions
        self.row = row
        self.column = column

    @staticmethod
    def from_legacy_coordinate(legacy_coordinate: LegacyCoordinate):
        """
        Creating a Coordinate from a legacy (Y, X) Tuple Coordinate
        """
        return Coordinate(legacy_coordinate[0], legacy_coordinate[1])

    def __str__(self) -> str:
        """
        Prints the coordinates in (row, column) format
        """
        return "({row}, {column})".format(row=self.row, column=self.column)

    def __repr__(self) -> str:
        """
        Returns the coordinates in a string format (similar to __str__)
        """
        return self.__str__()

    def __eq__(self, other: object) -> bool:
        """
        Compares one coordinate to another.
        A coordinate is equal if both the row and column coordinates are exact.
        """
        if (other.row == self.row) and (other.column == self.column):
            return True
        return False
    