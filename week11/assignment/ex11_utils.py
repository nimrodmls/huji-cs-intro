import numpy as np
import itertools
from typing import List, Tuple, Iterable, Optional
from boggle_board_randomizer import randomize_board

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
    pass
    


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

def _internal_find(current_word, letters, words):
    """
    """
    for letter in letters:
        pass

def find_new(letter_list, cur_word, board, words, max_len, valid_words):
    """
    """
    if len(cur_word) == max_len:
        if len(words) == 1 and words[0].strip() == cur_word:
            valid_words.append(cur_word)
            return
        else:
            return

    for index, element in enumerate(letter_list):
        new_words = np.extract(np.char.startswith(words, cur_word), words)
        if len(new_words) == 0:
            return
        find_new(np.delete(letter_list, index), cur_word+element, board, new_words, max_len, valid_words)

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
    import random
    random.seed("i")
    board = randomize_board()
    #print(board)
    #print(find_length_n_paths(3, board, my_file.readlines()))
    filedata = my_file.readlines()
    valwords = []
    import time
    prev = time.time()
    find_new(np.array(list(itertools.chain.from_iterable(board))),
        "",
        board,
        np.extract(np.char.str_len(filedata)==4, filedata),
        3,
        valwords)
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
