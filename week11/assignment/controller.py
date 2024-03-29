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

from boggle_board_randomizer import randomize_board
from gui import BoggleGUI, BoggleGUICallbacks
from boggle_game import BoggleGame
from common import Coordinate
from ex11_utils import WordsDictionary

class BoggleController(object):
    """
    Interfacing between the GUI and the Boggle Game
    """

    def __init__(self, words_dict: WordsDictionary, round_time_seconds=180) -> None:
        """
        Initializing the controller.
        Each round of Boggle will be with the given words dictionary, with
        the board being generated randomly.
        """
        callbacks = BoggleGUICallbacks(
            self._letter_callback,
            self._submit_callback,
            self._timer_callback,
            self._runstate_callback,
            self._menu_callback)
        self._gui = BoggleGUI(callbacks)
        self._round_time = round_time_seconds
        self._words_dict = words_dict

        # Should be updated once a game starts, and overriden when
        #   a new game begins
        self._current_board = None
        self._current_game = None
        self._timer = 0
        self._runstate = False
        self._difficulty = BoggleGUICallbacks.MENU_EVENT_DIFFICULTY_NORMAL
        self._score_penalty = 0
        self._failed_submits = 0

    def run_game(self) -> None:
        """
        Starting the operation of the game
        """
        self._gui.start()

    def _start_new_round(self) -> None:
        """
        Starting a new game round, without closing the GUI
        """
        self._current_board = randomize_board()
        self._current_game = BoggleGame(self._current_board, self._words_dict)
        self._gui.reset(self._current_board)
        self._timer = 0
        self._score_penalty = 0
        self._failed_submits = 0

    def _menu_callback(self, menu_event: str) -> None:
        """
        Called upon clicking of a button on the GUI's Pause Menu.
        
        :param menu_event: The event which risen the callback.
        """
        # Game resetting handling
        if BoggleGUICallbacks.MENU_EVENT_RESET == menu_event:
            self._start_new_round()
            self._set_run_state(True)
        # Difficulty handling
        elif (BoggleGUICallbacks.MENU_EVENT_DIFFICULTY_NORMAL == menu_event) or \
             (BoggleGUICallbacks.MENU_EVENT_DIFFICULTY_HARD == menu_event):
            self._difficulty = menu_event

    def _letter_callback(self, coordinate: Coordinate):
        """
        Called upon clicking of a letter button.
        Attempting to move the game object to the selected coordinate
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
        Called upon timed event of the GUI.
        Used for handling the round timer.
        """
        # Making sure we have a game running
        if (self._current_game is None) or (not self._runstate):
            return

        # Calculating the remaining time
        time_left = self._round_time - self._timer
            
        # If no remaining time is left, end the round
        if 0 >= time_left:
            self._gui.set_timer(datetime.time())
            self._gui.set_letter_buttons_state(False, hide=False)
            self._add_final_hints(self._current_game.get_hints())
            self._gui.set_run_state(True)
            self._current_board = None
            self._current_game = None
        else:
            # Otherwise update the clock
            self._gui.set_timer(
                datetime.time(minute=time_left // 60, second=time_left % 60))
        
        self._timer += 1 # Adding one second

    def _add_final_hints(self, hints: List[str]) -> None:
        """
        When the game finishes, we add all the possible words which
        can be assembled from the current board to the collection.
        Those are marked in a unique way to those found.
        """
        for hint in hints:
            self._gui.add_collection_hint(hint)

    def _submit_callback(self):
        """
        Called upon pressing the submit button on the GUI.
        This callback submits the word to the game and updates the score
        and collection accordingly.
        """
        if self._current_game is None:
            return

        submitted_word = self._current_game.submit_path()

        if submitted_word is not None:
            self._gui.add_to_collection(submitted_word)
            self._failed_submits = 0
        else:
            if self._is_hard_difficulty():
                # The submitted word is either wrong or already submitted,
                #   we should add penalty if it's hard difficulty
                self._score_penalty += 5
                self._timer += 5
            self._failed_submits += 1

        self._gui.set_score(self._current_game.get_score() - self._score_penalty)

        # Easteregg prompts
        if self._failed_submits >= 2 and self._failed_submits <= 4:
            self._gui.set_current_word("¯\_(ツ)_/¯", color="orange")
        elif self._failed_submits > 4:
            self._gui.set_current_word("(╯°□°）╯︵ ┻━┻", color="red")
        else:
            self._gui.set_current_word("")

        # Re-enabling all the buttons upon submission,
        #   whether succesful or not
        self._gui.set_letter_buttons_state(True, hide=False)
    
    def _set_run_state(self, new_state: bool) -> None:
        """
        Setting the running state of the game to paused or resumed.
        When the game is paused, a menu appears, when resumed the menu will
        be destroyed.
        """
        self._runstate = new_state
        self._gui.set_letter_buttons_state(new_state, hide=not new_state, board=self._current_board)
        self._gui.set_run_state(not new_state)
        
        # The game is running, runstate is True, so destroy the pause menu
        if self._runstate:
            self._gui.destroy_pause_menu()
        else: # The game is paused, create the pause menu
            self._gui.create_pause_menu()

    def _runstate_callback(self) -> None:
        """
        Called upon pressing of the running state button, and
        moving the game to resumed or paused state.
        """
        if self._current_game is None:
            self._start_new_round()
            self._set_run_state(True)
        else:
            self._set_run_state(not self._runstate)

    def _is_hard_difficulty(self):
        """
        Checking if the current difficulty level set is hard.
        """
        return (BoggleGUICallbacks.MENU_EVENT_DIFFICULTY_HARD == self._difficulty)
        