#################################################################
# FILE : boggle_game.py
# WRITER : Nimrod M. ; Ruth S.
# EXERCISE : intro2cs1 ex11 2023
# DESCRIPTION: Interface for the Boggle Game
# STUDENTS I DISCUSSED THE EXERCISE WITH: N/A
# WEB PAGES I USED: N/A
# NOTES: N/A
#################################################################

from typing import List
from common import Coordinate
from ex11_utils import Board, WordsDictionary, is_in_neighborhood

BoardPath = List[Coordinate]

class BoggleGame(object):
    """
    """

    def __init__(self, board: Board, words: WordsDictionary) -> None:
        """
        """
        self._board: Board = board
        self._words_dict: WordsDictionary = words
        self._score: int = 0
        self._current_path: BoardPath = []
        self._found_words: List[str] = []

    def move(self, coordinate: Coordinate) -> bool:
        """
        """
        last_coordinate = self._current_path[-1] if 0 != len(self._current_path) else None

        # Checking if the movement can be performed, i.e. if the requested
        #   coordinate is a neighboring coordinate
        if last_coordinate is not None and not is_in_neighborhood(last_coordinate, coordinate):
            return False

    def submit_path(self):
        """
        """
        found_word = self._path_to_word(self._current_path)
        if found_word in self._found_words:
            # The word has already been found, don't count it
            return

        # Adding the word in the path to the found words,
        #   and incrementing the total score
        self._score = len(self._current_path) ** 2
        self._found_words.append(found_word)

        # Zeroing the current path
        self._current_path = []

    def get_score(self) -> int:
        """
        """
        return self._score

    def _path_to_word(self, path: BoardPath) -> str:
        """
        """
        word = ""
        for coordinate in path:
            word += self._board[coordinate.row][coordinate.column]
        return word
        