#################################################################
# FILE : gui.py
# WRITER : Nimrod M. ; Ruth S.
# EXERCISE : intro2cs1 ex11 2023
# DESCRIPTION: GUI for the Boggle Game
# STUDENTS I DISCUSSED THE EXERCISE WITH: N/A
# WEB PAGES I USED: N/A
# NOTES: N/A
#################################################################

from typing import Callable
import tkinter as tk
from tkinter import font, scrolledtext
from pathlib import Path
from boggle_board_randomizer import randomize_board
from common import Coordinate
from ex11_utils import Board

LetterClickCallback = Callable[[Coordinate], None]

class BoggleGUICallbacks(object):

    def __init__(
        self, 
        letter_click_callback: LetterClickCallback,
        submit_click_callback,
        timer_callback,
        runstate_callback) -> None:
        """
        """
        self.letter_click_callback = letter_click_callback
        self.submit_click_callback = submit_click_callback
        self.timer_callback = timer_callback
        self.runstate_callback = runstate_callback

class BoggleGUI(object):
    """
    """
    BACKGROUND_COLOR_1 = "#2C3639"
    BACKGROUND_COLOR_2 = "#3F4E4F"
    COLLECTION_COLOR = "#3F4E4F"
    LETTER_BUTTON_COLOR = "#A27B5C"
    SUBMIT_BUTTON_COLOR = "#DCD7C9"
    TEXT_COLOR = "white"
    DEFAULT_FONT = "Agency FB"

    def __init__(self, board: Board, callbacks: BoggleGUICallbacks) -> None:
        """
        """
        self._callbacks = callbacks

        self._primary_window = tk.Tk()
        self._primary_window.title("Boggle Game")
        self._primary_window.resizable(False, False)

        self._create_control_panel(self._primary_window)
        self._create_current_word_label(self._primary_window)

        self._letter_buttons = {}
        self._create_lower_pane(self._primary_window, board)

    def _loop_score(self):
        self._configure_run_state(self._runstate)
        self.set_score(int(self._score_label['text']) + 10)
        self._primary_window.after(2000, self._loop_score)
        self._runstate = not self._runstate

    def start(self):
        """
        """
        self._runstate = True
        self._loop_score()
        self._primary_window.mainloop()

    def set_score(self, score: int) -> None:
        """
        """
        self._score_label['text'] = str(score)

    def set_current_word(self, current_word: str) -> None:
        """
        """
        self._current_word_label['text'] = current_word

    def disable_letter_button(self, button_coordinate: Coordinate):
        """
        """
    
    def add_to_collection(self, word: str) -> None:
        """
        """
        # Enabling edit before inserting, disabling it afterwards
        self._words_collection.configure(state="normal")
        self._words_collection.insert(tk.END, word + "\n")
        self._words_collection.configure(state="disable")

    def _configure_run_state(self, resume) -> None:
        """
        """
        if resume:
            self._runstate_button.configure(text='▶', fg="green")
        else:
            self._runstate_button.configure(text='⏸', fg="red")

    def _create_control_panel(self, parent_frame: tk.Frame) -> None:
        """
        """
        control_panel = tk.Frame(parent_frame, bg=self.BACKGROUND_COLOR_1)
        control_panel.pack(side=tk.TOP, fill=tk.BOTH)

        # Configurting the sizes of each element on the control panel
        # The leftmost element is the score, the middle is the pause/resume button
        #   and the rightmost element is the timer.
        control_panel.columnconfigure(0, weight=2, minsize=200)
        control_panel.columnconfigure(1, weight=1, minsize=100)
        control_panel.columnconfigure(2, weight=2, minsize=200)

        # Setting the score label, allowing access from outside
        self._score_label = tk.Label(
            control_panel, 
            fg = self.TEXT_COLOR, 
            bg = self.BACKGROUND_COLOR_1,
            font = font.Font(
                family=self.DEFAULT_FONT, size=20, weight='bold')
        )
        self._score_label["text"] = "0"
        self._score_label.grid(row=0, column=0, sticky=tk.NSEW)

        # Setting the pause/resume button
        self._runstate_button = tk.Button(
            control_panel, 
            text = "▶", 
            fg = "green", 
            bg = self.BACKGROUND_COLOR_1, 
            font = font.Font(
                family=self.DEFAULT_FONT, size=30, weight='bold'), borderwidth=0, highlightthickness=0, command=lambda: print("button_1 clicked"))
        self._runstate_button.grid(row=0, column=1, sticky=tk.NSEW, padx=10, pady=10)

        # Setting the timer label, allowing access from outside
        self._timer_label = tk.Label(control_panel, fg=self.TEXT_COLOR, bg=self.BACKGROUND_COLOR_1, font=tk.font.Font(family='Agency FB', size=20, weight='bold'))
        self._timer_label.grid(row=0, column=2, sticky=tk.NSEW)

    def _create_current_word_label(self, parent_window: tk.Frame) -> None:
        """
        """
        label_frame = tk.Frame(self._primary_window, bg=self.BACKGROUND_COLOR_1)
        label_frame.pack(side=tk.TOP, fill=tk.BOTH)
        self._current_word_label = tk.Label(label_frame, fg="white", bg=self.BACKGROUND_COLOR_1, font=tk.font.Font(family='Agency FB', size=25, weight='bold'))
        self._current_word_label.pack(side=tk.TOP, fill=tk.BOTH)

    def _create_lower_pane(self, parent_window: tk.Frame, board: Board) -> None:
        """
        """
        # Initializing the lower pane to have 2 columns,
        #   one for the letter buttons table, the other for the word collection
        lower_pane = tk.Frame(parent_window, bg=self.BACKGROUND_COLOR_2)
        lower_pane.pack(side=tk.TOP, fill=tk.BOTH)
        lower_pane.columnconfigure(0, weight=4)
        lower_pane.columnconfigure(1, weight=1, minsize=200)

        # The right frame is for the word collection
        right_frame = tk.Frame(
            lower_pane, bg=self.BACKGROUND_COLOR_2, bd=0)
        right_frame.grid(row=0, column=1, sticky=tk.NSEW)
        self._create_word_collection(right_frame)

        # The left frame is for the buttons table and the submit button
        # Creating all the buttons on the GUI
        self._letter_buttons = {}
        left_frame = tk.Frame(lower_pane, bg=self.BACKGROUND_COLOR_2)
        left_frame.grid(row=0, column=0, sticky=tk.NSEW)

        button_table = tk.Frame(left_frame, bg=self.BACKGROUND_COLOR_2)
        button_table.grid(row=0, column=0, sticky=tk.NSEW)
        self._create_letter_table(button_table, board)

        # Creating the submit button
        submit_button = tk.Button(
            left_frame,
            text="SUBMIT",
            bg = self.SUBMIT_BUTTON_COLOR,
            fg=self.TEXT_COLOR,
            font=tk.font.Font(family='Agency FB', size=30, weight='bold'),
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("SUBMIT"))
        submit_button.grid(
            row=1, 
            sticky=tk.NSEW, 
            padx=10, 
            pady=10)

    def _create_word_collection(self, parent_window: tk.Frame) -> None:
        """
        """
        # Setting the label for the collection, it is constant so we don't
        #   have any use for it later
        collection_label = tk.Label(
            parent_window,
            text = "COLLECTION",
            fg = "white",
            bg = self.BACKGROUND_COLOR_2,
            font = font.Font(family=self.DEFAULT_FONT, size=20))
        collection_label.pack(side=tk.TOP, fill=tk.BOTH)

        # Setting the scrollbars (horizontal and vertical)
        words_scrollbar_x = tk.Scrollbar(parent_window, orient=tk.HORIZONTAL)
        words_scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)

        words_scrollbar_y = tk.Scrollbar(parent_window, orient=tk.VERTICAL)
        words_scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Creating the text box for the words collection, it is set to disabled
        #   starting state in order to prevent editing from the user,
        #   it should be set to 'normal' whenever editing is necessary
        self._words_collection = tk.Text(
            parent_window,
            xscrollcommand=words_scrollbar_x,
            yscrollcommand=words_scrollbar_y, 
            wrap=tk.NONE, 
            state="disable",
            bg=self.COLLECTION_COLOR,
            fg="white",
            bd=0,
            height=1,
            width=25)
        self._words_collection.pack(side=tk.LEFT, fill=tk.BOTH)

    def _create_letter_table(self, parent_frame: tk.Frame, board: Board) -> None:
        """
        """
        # We rely on the fact that the board is squared
        for row_index in range(len(board)):
            parent_frame.rowconfigure(row_index, minsize=100)
            for column_index in range(len(board)):
                parent_frame.columnconfigure(column_index, minsize=100)
                self._create_letter_button(
                    parent_frame,
                    board[row_index][column_index],
                    row_index,
                    column_index)
    
    def _create_letter_button(self, parent: tk.Frame, text: str, row: int, column: int) -> None:
        """
        """
        button_coordinate = Coordinate(row, column)
        button = tk.Button(
            parent,
            text = text,
            bg = self.LETTER_BUTTON_COLOR,
            fg = self.TEXT_COLOR,
            font = font.Font(family=self.DEFAULT_FONT, size=30, weight='bold'),
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: self._callbacks.letter_click_callback(button_coordinate))
        button.grid(
            row = row, 
            column = column, 
            sticky = tk.NSEW, 
            padx = 10, 
            pady = 10)
            
        self._letter_buttons[str(button_coordinate)] = (button_coordinate, button)    
        return button

def demo_callback(coordinate: Coordinate):
    print(coordinate)
callbacks = BoggleGUICallbacks(demo_callback, None, None, None)
gui = BoggleGUI(randomize_board(), callbacks)
gui.start()