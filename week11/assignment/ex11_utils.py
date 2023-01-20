import numpy as np
import copy
import itertools
import os
from typing import List, Tuple, Iterable, Optional, Dict
from boggle_board_randomizer import randomize_board

Coordinate = Tuple[int, int]
Board = List[List[str]]
Path = List[Tuple[int, int]]
SortedWords = Dict[int, Dict[str, List]]

COORDINATE_ROW_INDEX = 0
COORDINATE_COLUMN_INDEX = 1

def _create_words_dict(words: Iterable[str]) -> SortedWords:
    """
    """
    sorted_dict = {}
    for word in filedata:
        if len(word) not in sorted_dict:
            sorted_dict[len(word)] = {}
        
        anagram = "".join(sorted(word))
        if anagram not in sorted_dict[len(word)]:
            sorted_dict[len(word)][anagram] = set()

        sorted_dict[len(word)][anagram].add(word)

    return sorted_dict

def _is_in_neighborhood(coordinate1: Coordinate, coordinate2: Coordinate):
    """
    Returns whether the given coordinates are in the neighborhood of one another
    """
    row_difference = abs(
        coordinate1[COORDINATE_ROW_INDEX] - coordinate2[COORDINATE_ROW_INDEX])
    column_difference = abs(
        coordinate1[COORDINATE_COLUMN_INDEX] - coordinate2[COORDINATE_COLUMN_INDEX])
    return (row_difference in [1, 0]) and (column_difference in [1, 0])

def _assemble_word(valid_coordinates, word, last_coordinate, current_path, all_paths):
    """
    """
    if len(word) == 0:
        all_paths.append(copy.deepcopy(current_path))
        return

    letter_instances = np.extract((valid_coordinates['letter'] == word[0]), valid_coordinates)
    if len(letter_instances) != 0:
        for instance in letter_instances:

            instance_coord = instance[0]
            if last_coordinate is not None and not _is_in_neighborhood(last_coordinate, instance_coord):
                continue

            current_path.append(instance_coord)
            _assemble_word(
                valid_coordinates[valid_coordinates != instance], word[1:], instance_coord, current_path, all_paths)
            current_path.pop()

def _find_valid_paths(path_length, board, word_dict, condition_callback = None):
    """
    """
    # Laying down all the coordinates of the board with their 
    #   respective value as a dictionary for better traversal
    board_coordinates = {(row_index, column_index): board[row_index][column_index]
        for row_index in range(len(board)) for column_index in range(len(board[0]))}
    
    # Generating all letter combinations (no repeatitions, order doesn't matter)
    combinations = itertools.combinations(board_coordinates.items(), path_length)

    paths = []
    for current_comb in combinations:
        current = dict(current_comb)
        anagram = "".join(sorted(current.values()))

        try:
            if anagram in word_dict[len(anagram)]:
                for word in word_dict[len(anagram)][anagram]:
                    word_paths = []
                    coordinate_map = np.array(
                        list(current_comb), dtype=[('coordinate', tuple), ('letter', 'U1')])
                    _assemble_word(coordinate_map, word, None, [], word_paths)
                    if (condition_callback and condition_callback(word)) or (not condition_callback):
                        paths += word_paths
        except KeyError:
            pass # This anagram doesn't exist, move on to the next combination

    return paths

def _is_valid_path_sorted(board: Board, path: Path, words: Iterable[str]) -> Optional[str]:
    """
    """
    last_coordinate = None
    current_word = ""
    for coordinate in path:
        # Making sure the coordinates are in the neighborhood of one another
        #   if at least one coordinate in the path is not in the neighborhood,
        #   return with failure
        if (last_coordinate is not None) and (not _is_in_neighborhood(last_coordinate, coordinate)):
            return None

        # Narrowing the list of words by the letter on the current coordinate
        current_word += board[coordinate[COORDINATE_ROW_INDEX]][coordinate[COORDINATE_COLUMN_INDEX]]

        # Updating the last coordinate we handled, so it can be checked in the
        #   next coordinate 
        last_coordinate = coordinate

    try:
        if current_word not in words[len(current_word)]["".join(sorted(current_word))]:
            return None
    except KeyError:
        return None

    return current_word

def is_valid_path(board: Board, path: Path, words: Iterable[str]) -> Optional[str]:
    """
    """
    words_dict = _create_words_dict(words)
    return _is_valid_path_sorted(board, path, words_dict)

def find_length_n_paths(n: int, board: Board, words: Iterable[str]) -> List[Path]:
    """
    """
    # Sorting the given words by length and anagrams
    word_dict = _create_words_dict(words)
    return _find_valid_paths(n, board, word_dict)

def find_length_n_words(n: int, board: Board, words: Iterable[str]) -> List[Path]:
    """
    """
    # Sorting the given words by length and anagrams
    word_dict = _create_words_dict(words)
    return _find_valid_paths(n, board, word_dict, lambda word: len(word) == n)

def max_score_paths(board: Board, words: Iterable[str]) -> List[Path]:
    """
    """
    pass


def path_to_word(board, path):
    word = ""
    for coor in path:
        word += board[coor[0]][coor[1]]
    return word


with open("week11\\assignment\\boggle_dict.txt", "r") as my_file:
    sorted_dict = {}
    filedata = my_file.read().split()
    import time
    import random
    random.seed("c")
    board = randomize_board()
    prev = time.time()
    for path in find_length_n_words(5, board, filedata):
        print(path)
        print(path_to_word(board, path))
    print(time.time() - prev)