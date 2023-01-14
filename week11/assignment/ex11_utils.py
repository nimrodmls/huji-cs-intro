import numpy as np
from typing import List, Tuple, Iterable, Optional

Coordinate = Tuple[int, int]
Board = List[List[str]]
Path = List[Tuple[int, int]]

COORDINATE_ROW_INDEX = 0
COORDINATE_COLUMN_INDEX = 1

def _is_in_neighborhood(coordinate1: Coordinate, coordinate2: Coordinate):
    """
    Returns whether the given coordinates are in the neighborhood of one another
    """
    row_difference = abs(
        coordinate1[COORDINATE_ROW_INDEX] - coordinate2[COORDINATE_ROW_INDEX])
    column_difference = (
        coordinate1[COORDINATE_COLUMN_INDEX] - coordinate2[COORDINATE_COLUMN_INDEX])
    return (row_difference == 1) and (column_difference == 1)

def is_valid_path(board: Board, path: Path, words: Iterable[str]) -> Optional[str]:
    """
    """
    last = None
    current_letters = ""
    current_narrow = []
    for coordinate in path:
        # Making sure the coordinates are in the neighborhood of one another
        #   if at least one coordinate in the path is not in the neighborhood,
        #   return so
        if (last is not None) and (not _is_in_neighborhood(last, coordinate)):
            return None
        current_letters += board[coordinate[COORDINATE_ROW_INDEX]][coordinate[COORDINATE_COLUMN_INDEX]]
        current_narrow = np.extract(np.char.startswith(words, current_letters))
        if 0 == len(current_narrow):
            return None
        last = coordinate
    
    return current_letters

def search_word(word, words):
    current_letters = ""
    current_narrow = words
    for letter in word:
        current_letters += letter
        current_narrow = np.extract(np.char.startswith(current_narrow, current_letters.upper()), current_narrow)
        if 0 == len(current_narrow):
            return False

    return True

with open("week11\\assignment\\boggle_dict.txt", "r") as my_file:
    print(search_word("ANTIODONTALGICS", my_file.readlines()))


def find_length_n_paths(n: int, board: Board, words: Iterable[str]) -> List[Path]:
    """
    """
    pass


def find_length_n_words(n: int, board: Board, words: Iterable[str]) -> List[Path]:
    """
    """
    pass


def max_score_paths(board: Board, words: Iterable[str]) -> List[Path]:
    """
    """
    pass
