import numpy as np
import itertools
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

def _is_word_in_dictionary(word: str, words: Iterable[str]) -> bool:
    """
    Yummy, efficiency
    """
    


def is_valid_path(board: Board, path: Path, words: Iterable[str]) -> Optional[str]:
    """
    """
    last_coordinate = None
    current_word = ""
    current_narrow = None
    for coordinate in path:
        # Making sure the coordinates are in the neighborhood of one another
        #   if at least one coordinate in the path is not in the neighborhood,
        #   return with failure
        if (last_coordinate is not None) and (not _is_in_neighborhood(last_coordinate, coordinate)):
            return None

        # Narrowing the list of words by the letter on the current coordinate
        current_word += board[coordinate[COORDINATE_ROW_INDEX]][coordinate[COORDINATE_COLUMN_INDEX]]
        current_narrow = np.extract(np.char.startswith(current_narrow, current_word), current_narrow)
        # If we narrowed the words list and there are no words with start with
        #   the requested letters we should return with failure
        if 0 == len(current_narrow):
            return None

        # Updating the last coordinate we handled, so it can be checked in the
        #   next coordinate 
        last_coordinate = coordinate
    
    return current_word

def find_length_n_paths(n: int, board: Board, words: Iterable[str]) -> List[Path]:
    """
    """
    # Flattening the board to get all the letters 
    #   in a single 1-dimensional list
    board_letters = itertools.chain.from_iterable(board)
    # Getting all the possible permutations of a word with the
    #   board's letters. Letters don't repeat as per the game's rules.
    word_permutations = itertools.permutations(board_letters)



def find_length_n_words(n: int, board: Board, words: Iterable[str]) -> List[Path]:
    """
    """
    pass


def max_score_paths(board: Board, words: Iterable[str]) -> List[Path]:
    """
    """
    pass
