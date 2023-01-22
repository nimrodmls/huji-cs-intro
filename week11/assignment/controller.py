#################################################################
# FILE : controller.py
# WRITER : Nimrod M. ; Ruth S.
# EXERCISE : intro2cs1 ex11 2023
# DESCRIPTION: Game-to-GUI Interface & Controller
# STUDENTS I DISCUSSED THE EXERCISE WITH: N/A
# WEB PAGES I USED: N/A
# NOTES: N/A
#################################################################

import datetime
from typing import List
from ex11_utils import create_words_dict, max_score_paths_sorted
from boggle_board_randomizer import randomize_board
from gui import BoggleGUI, BoggleGUICallbacks
from boggle_game import BoggleGame
from common import Coordinate
from ex11_utils import WordsDictionary

class BoggleController(object):
    """
    """

    def __init__(self, words_dict: WordsDictionary, round_time_seconds=180) -> None:
        """
        """
        callbacks = BoggleGUICallbacks(
            self._letter_callback,
            self._submit_callback,
            self._timer_callback,
            self._runstate_callback)
        self._gui = BoggleGUI(callbacks)
        self._round_time = round_time_seconds
        self._words_dict = words_dict
        # Should be updated once a game starts, and overriden when
        #   a new game begins
        self._current_board = None
        self._current_game = None
        self._timer = 0

    def run_game(self) -> None:
        """
        """
        self._gui.start()

    def _start_new_round(self) -> None:
        """
        """
        self._current_board = randomize_board()
        self._current_game = BoggleGame(self._current_board, self._words_dict)
        self._gui.reset(self._current_board)
        self._timer = 0

    def _letter_callback(self, coordinate: Coordinate):
        """
        """
        if self._current_game is None:
            return
            
        # Trying to move on the board, if the movement is
        #   succesful, then we disable the button until the word is submitted
        if self._current_game.move(coordinate):
            self._gui.disable_letter_button(coordinate)
            self._gui.set_current_word(self._current_game.get_current_word())
    
    def _timer_callback(self):
        """
        """
        if self._current_game is None:
            return

        time_left = self._round_time - self._timer
            
        if 0 >= time_left:
            self._gui.set_timer(datetime.time())
            self._gui.set_letter_buttons_state(False)
            self._add_final_hints(self._current_game.get_hints())
            self._gui.set_run_state(True)
            self._current_board = None
            self._current_game = None
        else:
            self._gui.set_timer(
                datetime.time(minute=time_left // 60, second=time_left % 60))
        
        self._timer += 1 # Adding one second

    def _add_final_hints(self, hints: List[str]) -> None:
        """
        """
        for hint in hints:
            self._gui.add_collection_hint(hint)

    def _submit_callback(self):
        """
        """
        if self._current_game is None:
            return

        submitted_word = self._current_game.submit_path()

        if submitted_word is not None:
            self._gui.add_to_collection(submitted_word)

        self._gui.set_score(self._current_game.get_score())
        self._gui.set_current_word("")

        # Re-enabling all the buttons upon submission,
        #   whether succesful or not
        self._gui.set_letter_buttons_state(True)

    def _runstate_callback(self, resume: bool):
        """
        """
        if self._current_game is None:
            self._start_new_round()
        else:
            self._gui.set_run_state(not resume)


filedata = ""
with open("week11\\assignment\\boggle_dict.txt", "r") as my_file:
    filedata = my_file.read().split()
wordsdict = create_words_dict(filedata)
controller = BoggleController(wordsdict)
controller.run_game()