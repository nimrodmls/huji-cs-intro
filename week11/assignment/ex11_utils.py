import numpy as np
import itertools
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
            sorted_dict[len(word)][anagram] = []

        sorted_dict[len(word)][anagram].append(word)

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
    
def _validate_paths(coords):
    perms = itertools.permutations(coords, 16)
    import time
    prev = time.time()
    for path in perms:
        last_coord = None
        for coord in path:
            if last_coord is not None and _is_in_neighborhood(coord, last_coord):
                pass
            last_coord = coord
    print(time.time() - prev)

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
    print(current_word)
    return current_word


def is_valid_path(board: Board, path: Path, words: Iterable[str]) -> Optional[str]:
    """
    """
    last_coordinate = None
    current_word = ""
    current_narrow = words
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

def find_improved(n: int, board: Board, words: Iterable[str]):
    """
    """
    sorted_words_dict = _create_words_dict(words)
    board_letters = [(row_index, column_index)
        for row_index in range(len(board)) for column_index in range(len(board[0]))]
    # Getting all the possible permutations of a word with the
    #   board's letters. Letters don't repeat as per the game's rules.
    path_permutations = itertools.permutations(board_letters, n)
    valid_paths = []
    for path in path_permutations:
        if _is_valid_path_sorted(board, path, sorted_words_dict) is not None:
            valid_paths.append(path)

    return valid_paths

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

def find_length_n_paths(n: int, board: Board, words: Iterable[str]) -> List[Path]:
    """
    """
    # Flattening the board to get all the letters 
    #   in a single 1-dimensional list
    board_letters2 = itertools.chain.from_iterable(board)
    board_letters = [(row_index, column_index)
        for row_index in range(len(board)) for column_index in range(len(board[0]))]
    # Getting all the possible permutations of a word with the
    #   board's letters. Letters don't repeat as per the game's rules.
    path_permutations = itertools.permutations(board_letters, n)
    valid_paths = []
    for path in path_permutations:
        if is_valid_path(board, path, np.extract(np.char.str_len(words)==n, words)):
            valid_paths.append(list(path))
    return valid_paths

with open("week11\\assignment\\boggle_dict.txt", "r") as my_file:
    sorted_dict = {}
    filedata = my_file.read().split()
    import time


    import random
    #random.seed("i")
    board = randomize_board()

    #prev = time.time()
    #print(find_improved(16, board, filedata))
    #print(time.time() - prev)
    #print(board)
    #print(find_length_n_paths(3, board, my_file.readlines()))
    valwords = []
    prev = time.time()
    board_letters = [(row_index, column_index)
        for row_index in range(len(board)) for column_index in range(len(board[0]))]
    word_dict = _create_words_dict(filedata)
    find_new(np.array(board_letters),
        "",
        board,
        word_dict,
        7,
        valwords,
        None)
    print(valwords)
    print(time.time() - prev)
    # data = my_file.readlines()
    # new_data = np.extract(np.char.str_len(data)==5, data)
    # for i in range(40):
    #     print(new_data[i])


def find_length_n_words(n: int, board: Board, words: Iterable[str]) -> List[Path]:
    """
    """
    pass


def max_score_paths(board: Board, words: Iterable[str]) -> List[Path]:
    """
    """
    pass
