import numpy as np
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

def find_new(letter_list, cur_word, board, words, max_len, valid_words, last_coord):
    """
    """
    if len(cur_word) == max_len:
        try:
            if cur_word not in words[max_len]["".join(sorted(cur_word))]:
                return
            valid_words.append(cur_word)
        except KeyError:
            return

    for index, element in enumerate(letter_list):
        if last_coord is not None and not _is_in_neighborhood(element, last_coord):
            continue
        letter = board[element[0]][element[1]]
        find_new(np.delete(letter_list, index, 0), 
            cur_word+letter, board, words, max_len, valid_words, element)

def _find_all_valid_paths(
    max_len: int, board: Board, words: SortedWords, valid_coords: List[str], current_word: str, path: Path, valid_paths: Path):
    """
    """
    if len(current_word) == max_len:
        try:
            if current_word not in words[max_len]["".join(sorted(current_word))]:
                return
            valid_paths.append(path)
        except KeyError:
            return

    for index, element in enumerate(valid_coords):
        if 0 != len(path) and _is_in_neighborhood(element, path[-1]):
            continue
        letter = board[element[0]][element[1]]
        path.append(element)
        _find_all_valid_paths( 
            max_len, board, words, np.delete(valid_coords, index, 0), current_word + letter, path, valid_paths)
        path.remove(element)

def find_length_n_paths(n: int, board: Board, words: Iterable[str]) -> List[Path]:
    """
    """
    board_coordinates = [(row_index, column_index)
        for row_index in range(len(board)) for column_index in range(len(board[0]))]
    words_dict = _create_words_dict(words)

    paths = []
    _find_all_valid_paths(n, board, words_dict, np.array(board_coordinates), "", [], paths)
    return paths

def path_to_word(board, path):
    word = ""
    for coor in path:
        word += board[coor[0]][coor[1]]
    return word

import copy

def _get_valid_paths(board, max_len, valid_coordinates, words, current_path, current_word, paths):
    if max_len == len(current_word):
        try:
            if current_word not in words[len(current_path)]["".join(sorted(current_word))]:
                return
            paths.append(copy.deepcopy(current_path))
        except KeyError:
            return

    for index, element in enumerate(valid_coordinates):
        if 0 != len(current_path) and _is_in_neighborhood(element, current_path[-1]):
            continue
        letter = board[element[0]][element[1]]
        current_path.append(element)
        _get_valid_paths(board, max_len, np.delete(valid_coordinates, index, 0), words, current_path, current_word+letter, paths)
        current_path.pop()

def _assemble_word(board_map, word, last_coordinate, current_path, all_paths):

    if len(word) == 0:
        all_paths.append(copy.deepcopy(current_path))
        return

    letter_instances = np.extract((board_map['letter'] == word[0]), board_map)
    if len(letter_instances) != 0:
        for instance in letter_instances:
            instance_coord = instance[1]
            if last_coordinate is not None and not _is_in_neighborhood(last_coordinate, instance_coord):
                continue
            current_path.append(instance_coord)
            _assemble_word(board_map[board_map != instance], word[1:], instance_coord, current_path, all_paths)
            current_path.pop()

with open("week11\\assignment\\boggle_dict.txt", "r") as my_file:
    sorted_dict = {}
    filedata = my_file.read().split()
    import time
    prev = time.time()
    word_dict = _create_words_dict(filedata)
    print(time.time() - prev)
    import random
    random.seed("c")
    board = randomize_board()
    board_map = np.array([(board[row_index][column_index], (row_index, column_index)) 
        for row_index in range(len(board)) for column_index in range(len(board[0]))], dtype=[('letter', 'U1'), ('coordinate', tuple)])
    all_paths = []
    #_assemble_word(board_map, "OXFI", None, [], all_paths)
    for path in all_paths:
        print(path_to_word(board, path))
    board_coordinates = {(row_index, column_index): board[row_index][column_index]
        for row_index in range(len(board)) for column_index in range(len(board[0]))}
    combs = itertools.combinations(board_coordinates.items(), 5)
    cnt = 0
    prev = time.time()
    paths = []
    for comb in combs:
        current = dict(comb)
        anagram = "".join(sorted(current.values()))
        try:
            if anagram in word_dict[len(anagram)]:
                for word in word_dict[len(anagram)][anagram]:
                     _assemble_word(board_map, word, None, [], paths)
                #_get_valid_paths(board, 6, np.asarray(list(current.keys())), word_dict, [], "", paths)
        except KeyError:
            pass
    print(time.time() - prev)
    for line in board:
        print(line)
    for path in paths:
        print(path)
        print(path_to_word(board, path))
    #paths = find_length_n_paths(6, board, filedata)
    #for path in paths:
    #    print(path_to_word(board, path))


def find_length_n_words(n: int, board: Board, words: Iterable[str]) -> List[Path]:
    """
    """
    pass


def max_score_paths(board: Board, words: Iterable[str]) -> List[Path]:
    """
    """
    pass
