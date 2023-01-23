#################################################################
# FILE : ex11_utils.py
# WRITER : Nimrod M. ; Ruth S.
# EXERCISE : intro2cs1 ex11 2023
# DESCRIPTION: Utility functionality for operations with the
#              words dictionary and performance maximizing.
# STUDENTS I DISCUSSED THE EXERCISE WITH: N/A
# WEB PAGES I USED: N/A
# NOTES: N/A
#################################################################

import numpy as np
import copy
import itertools
from typing import List, Tuple, Iterable, Optional, Dict, Callable

from common import LegacyCoordinate, Coordinate

Board = List[List[str]]
Path = List[Tuple[int, int]]
# The structure of the words dictionary (post-sorting).
#   The dictionary contains length-to-anagrams mapping,
#   with the anagrams themselves being anagram-to-words
#   mapping, with words being all the words built from the
#   anagram
WordsDictionary = Dict[int, Dict[str, List]]
# Condition callback for _find_valid_paths, receives the relevant word (str)
#   and the paths associated with it (List[Path]). Callback should return
#   boolean specifying whether the word is valid.
ConditionCallback = Callable[[str, List[Path]], bool]

# Indices specifying access to the legacy coordinate
COORDINATE_ROW_INDEX = 0
COORDINATE_COLUMN_INDEX = 1

def create_words_dict(words: Iterable[str]) -> WordsDictionary:
    """
    """
    sorted_dict = {}
    for word in words:
        if len(word) not in sorted_dict:
            sorted_dict[len(word)] = {}
        
        anagram = "".join(sorted(word))
        if anagram not in sorted_dict[len(word)]:
            sorted_dict[len(word)][anagram] = set()

        sorted_dict[len(word)][anagram].add(word)

    return sorted_dict

def is_in_neighborhood(coordinate1: Coordinate, coordinate2: Coordinate) -> bool:
    """
    """
    row_difference = abs(coordinate1.row - coordinate2.row)
    column_difference = abs(coordinate1.column - coordinate2.column)
    return (row_difference in [1, 0]) and (column_difference in [1, 0])

def _is_in_neighborhood_legacy(coordinate1: LegacyCoordinate, coordinate2: LegacyCoordinate) -> bool:
    """
    Returns whether the given coordinates are in the neighborhood of one another
    """
    return is_in_neighborhood(Coordinate.from_legacy_coordinate(coordinate1),
                              Coordinate.from_legacy_coordinate(coordinate2))

def _assemble_word(valid_coordinates, word: str, last_coordinate, current_path, all_paths):
    """
    """
    if len(word) == 0:
        all_paths.append(copy.deepcopy(current_path))
        return
    
    # Extract all the words which start with the FIRST letter of the current
    #   combination in the coordinate
    letter_instances = np.extract((np.char.startswith(valid_coordinates['letter'], word[0])), valid_coordinates)
    for instance in letter_instances:
        # Now check that the word actually starts with all the letters of the combination
        if not word.startswith(instance['letter']):
            continue
        
        instance_coord = instance['coordinate']
        if last_coordinate is not None and not _is_in_neighborhood_legacy(last_coordinate, instance_coord):
            continue

        current_path.append(instance_coord)
        _assemble_word(
            valid_coordinates[valid_coordinates != instance], 
            word[len(instance['letter']):], 
            instance_coord, 
            current_path, 
            all_paths)
        current_path.pop()

def _find_valid_paths(path_length: int, 
                      board: Board, 
                      word_dict: WordsDictionary, 
                      condition_callback: ConditionCallback = None) -> List[Path]:
    """
    """
    # Laying down all the coordinates of the board with their 
    #   respective value as a dictionary for better traversal
    board_coordinates = {(row_index, column_index): board[row_index][column_index]
        for row_index in range(len(board)) for column_index in range(len(board[0]))}
    
    # Generating all letter combinations (no repeatitions, order doesn't matter)
    combinations = itertools.combinations(board_coordinates.items(), path_length)

    paths = []
    # Iterate on all possible combinations
    for current_comb in combinations:
        current = dict(current_comb)
        # Create the anagram - First we join all the coordinate values,
        #   then we sort (in order to support coordinates storing
        #   more than one letter in them, e.g. QU)
        anagram = "".join(sorted("".join(current.values())))

        try:
            if anagram in word_dict[len(anagram)]:
                for word in word_dict[len(anagram)][anagram]:
                    word_paths = []
                    # Organize all the coordinates in a ordered matter so
                    #   each letter can be accessed by coordinate or letter.
                    # Constant: We allow max of 100 letters for each coordinate.
                    coordinate_map = np.array(
                        list(current_comb), dtype=[('coordinate', tuple), ('letter', 'U100')])
                    _assemble_word(coordinate_map, word, None, [], word_paths)
                    # If either of the two conditions are true, 
                    #   add the paths to the rest of valid paths
                    # Condition 1: There are some paths, there is a condition callback,
                    #   and the callback returned that the paths should be added.
                    # Condition 2: There is no condition callback, 
                    #   so add the paths unconditionally
                    if ((len(word_paths) != 0) and 
                         condition_callback and 
                         condition_callback(word, word_paths)) or \
                        (not condition_callback):
                        paths += word_paths
        except KeyError:
            pass # This anagram doesn't exist, move on to the next combination

    return paths

def is_valid_path_sorted(board: Board, path: List[Coordinate], words: WordsDictionary) -> Optional[str]:
    """
    """
    last_coordinate = None
    current_word = ""
    for coordinate in path:
        # Making sure the coordinates are in the neighborhood of one another
        #   if at least one coordinate in the path is not in the neighborhood,
        #   return with failure
        if (last_coordinate is not None) and (not is_in_neighborhood(last_coordinate, coordinate)):
            return None
        
        # Check that the coordinates are within the board boundries
        if (coordinate.row >= len(board) or coordinate.row < 0) or \
           (coordinate.column >= len(board[0]) or coordinate.column < 0):
           return None

        # Narrowing the list of words by the letter on the current coordinate
        current_word += board[coordinate.row][coordinate.column]

        # Updating the last coordinate we handled, so it can be checked in the
        #   next coordinate 
        last_coordinate = coordinate

    # Try to find the word in the dict
    try:
        if current_word not in words[len(current_word)]["".join(sorted(current_word))]:
            return None
    except KeyError:
        return None # The anagram doesn't exist, or length doesn't exist

    return current_word

def is_valid_path(board: Board, path: Path, words: Iterable[str]) -> Optional[str]:
    """
    """
    words_dict = create_words_dict(words)
    new_path = []
    for coordinate in path:
        new_path.append(Coordinate.from_legacy_coordinate(coordinate))
    return is_valid_path_sorted(board, new_path, words_dict)

def find_length_n_paths(n: int, board: Board, words: Iterable[str]) -> List[Path]:
    """
    """
    # Sorting the given words by length and anagrams
    word_dict = create_words_dict(words)
    return _find_valid_paths(n, board, word_dict)

def find_length_n_words(n: int, board: Board, words: Iterable[str]) -> List[Path]:
    """
    """
    # Sorting the given words by length and anagrams
    word_dict = create_words_dict(words)
    return _find_valid_paths(n, board, word_dict, lambda word, word_paths: len(word) == n)

def max_score_paths_sorted(board: Board, words_dict: WordsDictionary) -> List[Path]:
    """
    """
    words = {}

    # Iterating on the number of possible path lengths according to
    #   the board's dimensions.
    for current_path_len in range(len(board) * len(board[0])):

        # A special function for selecting only 1 instance of
        #   a word instead of receiving multiple paths of the same word
        #   by the return value of the _find_valid_paths
        def path_condition(word, word_paths, current_words):
            current_words[word] = word_paths[0]
            return True

        # We don't care about the return value as we picked only 1 instance 
        #   of the word already via path_condition
        _find_valid_paths(current_path_len, board, words_dict, lambda word, word_paths: path_condition(word, word_paths, words))            
        
    return words.values()

def max_score_paths(board: Board, words: Iterable[str]) -> List[Path]:
    """
    """
    word_dict = create_words_dict(words)
    return max_score_paths_sorted(board, word_dict)
