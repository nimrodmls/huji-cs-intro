#################################################################
# FILE : boggle_game.py
# WRITER : Nimrod M. ; Ruth S.
# EXERCISE : intro2cs1 ex11 2023
# DESCRIPTION: Interface for the Boggle Game
# STUDENTS I DISCUSSED THE EXERCISE WITH: N/A
# WEB PAGES I USED: N/A
# NOTES: N/A
#################################################################

from typing import List, Optional
from common import Coordinate
from ex11_utils import Board, Path, WordsDictionary, is_valid_path_sorted, is_in_neighborhood, max_score_paths_sorted

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

        self._current_path.append(coordinate)
        return True

    def submit_path(self) -> Optional[str]:
        """
        """
        found_word = is_valid_path_sorted(self._board, self._current_path, self._words_dict)

        # If it word wasn't found and it exists in the dictionary, count it,
        #   otherwise just ignore it and reset the current path
        if (found_word is not None) and (found_word not in self._found_words):
            self._score += len(self._current_path) ** 2
            self._found_words.append(found_word)
        elif found_word in self._found_words:
            # Since the word was already found we should show it as invalid
            found_word = None

        # Resetting the current path
        self._current_path = []
        
        return found_word

    def get_score(self) -> int:
        """
        """
        return self._score

    def get_current_word(self) -> str:
        """
        """
        return self._path_to_word(self._current_path)

    def get_hints(self) -> List[str]:
        """
        """
        hints = []
        for path in max_score_paths_sorted(self._board, self._words_dict):
            word = self._path_to_word(self._path_from_legacy_path(path))
            if (word not in self._found_words) and (word not in hints):
                hints.append(word)
        return hints

    @staticmethod
    def _path_from_legacy_path(legacy_path: Path) -> BoardPath:
        """
        """
        new_path = []
        for coordinate in legacy_path:
            new_path.append(Coordinate.from_legacy_coordinate(coordinate))
        return new_path

    def _path_to_word(self, path: BoardPath) -> str:
        """
        """
        word = ""
        for coordinate in path:
            word += self._board[coordinate.row][coordinate.column]
        return word
