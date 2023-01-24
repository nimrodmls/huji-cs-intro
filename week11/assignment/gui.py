#################################################################
# FILE : gui.py
# WRITER : Nimrod M. ; Ruth S.
# EXERCISE : intro2cs1 ex11 2023
# DESCRIPTION: GUI for the Boggle Game
# STUDENTS I DISCUSSED THE EXERCISE WITH: N/A
# WEB PAGES I USED: N/A
# NOTES: N/A
#################################################################

import datetime
from typing import Callable, Dict
import tkinter as tk
from tkinter import font
from boggle_board_randomizer import randomize_board
from common import Coordinate
from ex11_utils import Board

LetterCallback = Callable[[Coordinate], None]
SubmitCallback = Callable[[], None]
TimerCallback = Callable[[], None]
RunStateCallback = Callable[[], None]
MenuCallback = Callable[[str], None]

class BoggleGUICallbacks(object):
    """
    """

    MENU_EVENT_RESET = "Reset"
    MENU_EVENT_DIFFICULTY_HARD = "HardDif"
    MENU_EVENT_DIFFICULTY_NORMAL = "NormalDif"

    def __init__(
        self, 
        letter_callback: LetterCallback,
        submit_callback: SubmitCallback,
        timer_callback: TimerCallback,
        runstate_callback: RunStateCallback,
        menu_callback: MenuCallback) -> None:
        """
        """
        self.letter_callback = letter_callback
        self.submit_callback = submit_callback
        self.timer_callback = timer_callback
        self.runstate_callback = runstate_callback
        self.menu_callback = menu_callback

class BoggleGUI(object):
    """
    """
    BACKGROUND_COLOR_1 = "#03001C"
    BACKGROUND_COLOR_2 = "#301E67"
    COLLECTION_COLOR = "#301E67"
    COLLECTION_HINT_COLOR = "#AF4E4F"
    LETTER_BUTTON_COLOR = "#5B8FB9"
    DISABLED_LETTER_COLOR = "#4C0027"
    SUBMIT_BUTTON_COLOR = "#150050"
    TEXT_COLOR = "white"
    DEFAULT_FONT = "Agency FB"
    TIMER_DELAY = 1000 # in ms
    RUNSTATE_RESUME = "▶"
    RUNSTATE_PAUSE = "⏸"

    def __init__(self, callbacks: BoggleGUICallbacks) -> None:
        """
        """
        self._callbacks = callbacks

        self._primary_window = tk.Tk()
        self._primary_window.title("Boggle Game")
        self._primary_window.resizable(False, False)

        self._create_control_panel(self._primary_window)
        self._create_current_word_label(self._primary_window)

        self._letter_buttons: Dict[str, (Coordinate, tk.Button)] = {}
        self._create_lower_pane(self._primary_window)

        self._words_collection.tag_configure("hint", background=self.COLLECTION_HINT_COLOR)

        self._menu_window = None

    def create_pause_menu(self):
        """
        """
        if self._menu_window is not None:
            self.destroy_pause_menu()

        self._menu_window = tk.Toplevel(
            self._primary_window, 
            background=self.BACKGROUND_COLOR_1)
        self._menu_window.title("Boggle Menu")
        self._menu_window.resizable(False, False)
        reset_button = tk.Button(
            self._menu_window, 
            text="RESET", 
            height=5, 
            width=20,
            bg = self.LETTER_BUTTON_COLOR,
            fg = self.TEXT_COLOR,
            font = font.Font(family=self.DEFAULT_FONT, size=12, weight='bold'),
            borderwidth = 0,
            highlightthickness = 0,
            command=lambda: self._callbacks.menu_callback(
                BoggleGUICallbacks.MENU_EVENT_RESET))
        hard_button = tk.Button(
            self._menu_window, 
            text="HARD DIFFICULTY", 
            height=5, 
            width=20,
            bg = self.LETTER_BUTTON_COLOR,
            fg = self.TEXT_COLOR,
            font = font.Font(family=self.DEFAULT_FONT, size=12, weight='bold'),
            borderwidth = 0,
            highlightthickness = 0,
            command=lambda: self._callbacks.menu_callback(
                BoggleGUICallbacks.MENU_EVENT_DIFFICULTY_HARD))
        normal_button = tk.Button(
            self._menu_window, 
            text="NORMAL DIFFICULTY", 
            height=5, 
            width=20,
            bg = self.LETTER_BUTTON_COLOR,
            fg = self.TEXT_COLOR,
            font = font.Font(family=self.DEFAULT_FONT, size=12, weight='bold'),
            borderwidth = 0,
            highlightthickness = 0,
            command=lambda: self._callbacks.menu_callback(
                BoggleGUICallbacks.MENU_EVENT_DIFFICULTY_NORMAL))
        reset_button.pack(side=tk.TOP, fill=tk.BOTH, padx=10, pady=10)
        normal_button.pack(side=tk.TOP, fill=tk.BOTH, padx=10, pady=10)
        hard_button.pack(side=tk.TOP, fill=tk.BOTH, padx=10, pady=10)

    def destroy_pause_menu(self):
        """
        """
        if self._menu_window is None:
            return

        self._menu_window.destroy()
        self._menu_window = None

    def start(self):
        """
        """
        self._set_timed_event()
        self._primary_window.mainloop()

    def reset(self, board: Board) -> None:
        """
        """
        # Resetting buttons
        self.set_letter_buttons_state(True, hide=False, board=board)

        # Resetting timer & score
        self.set_score(0)
        self.set_timer(datetime.time())

        # Resetting words collection
        self._words_collection.configure(state="normal")
        self._words_collection.delete("1.0", tk.END)
        self._words_collection.configure(state="disable")

    def set_score(self, score: int) -> None:
        """
        """
        self._score_label['text'] = str(score)
        
    def set_timer(self, time: datetime.time) -> None:
        """
        """
        self._timer_label['text'] = time.strftime("%M:%S")

    def set_current_word(self, current_word: str, color: str = "white") -> None:
        """
        """
        self._current_word_label['text'] = current_word
        self._current_word_label['fg'] = color

    def disable_letter_button(self, button_coordinate: Coordinate) -> None:
        """
        """
        button: tk.Button = self._letter_buttons[str(button_coordinate)][1]
        button.configure(background=self.DISABLED_LETTER_COLOR, state='disable')

    def set_letter_buttons_state(self, enable: bool, hide: bool, board: Board=None) -> None:
        """
        """
        for button in self._letter_buttons:
            coordinate: Coordinate = self._letter_buttons[button][0]
            button: tk.Button = self._letter_buttons[button][1]
            new_text = button['text'] if board is None else board[coordinate.row][coordinate.column]
            button.configure(
                background = self.LETTER_BUTTON_COLOR,
                state = 'normal' if enable else 'disable',
                text = "" if hide else new_text)
    
    def add_to_collection(self, word: str) -> None:
        """
        """
        # Enabling edit before inserting, disabling it afterwards
        self._words_collection.configure(state="normal")
        self._words_collection.insert(tk.END, word + "\n")
        self._words_collection.configure(state="disable")

    def add_collection_hint(self, word: str) -> None:
        """
        """
        self._words_collection.configure(state="normal")
        self._words_collection.insert(tk.END, word + "\n", "hint")
        self._words_collection.configure(state="disable")

    def set_run_state(self, resume: bool) -> None:
        """
        """
        if resume:
            self._runstate_button.configure(text=self.RUNSTATE_RESUME, fg="green")
        else:
            self._runstate_button.configure(text=self.RUNSTATE_PAUSE, fg="red")

    def _set_timed_event(self) -> None:
        """
        """
        self._callbacks.timer_callback()
        self._primary_window.after(self.TIMER_DELAY, self._set_timed_event)
    
    ##############################
    # GUI Initialization Methods #
    ##############################

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
            text =self.RUNSTATE_RESUME, 
            fg = "green", 
            bg = self.BACKGROUND_COLOR_1, 
            font = font.Font(
                family=self.DEFAULT_FONT, size=30, weight='bold'), 
            borderwidth = 0, 
            highlightthickness = 0, 
            command=lambda: self._callbacks.runstate_callback())
        self._runstate_button.grid(row=0, column=1, sticky=tk.NSEW, padx=10, pady=10)

        # Setting the timer label, allowing access from outside
        self._timer_label = tk.Label(
            control_panel, 
            fg = self.TEXT_COLOR, 
            bg = self.BACKGROUND_COLOR_1, 
            text = "00:00",
            font = tk.font.Font(family=self.DEFAULT_FONT, size=20, weight='bold'))
        self._timer_label.grid(row=0, column=2, sticky=tk.NSEW)

    def _create_current_word_label(self, parent_window: tk.Frame) -> None:
        """
        """
        label_frame = tk.Frame(self._primary_window, bg=self.BACKGROUND_COLOR_1)
        label_frame.pack(side=tk.TOP, fill=tk.BOTH)
        self._current_word_label = tk.Label(label_frame, fg="white", bg=self.BACKGROUND_COLOR_1, font=font.Font(family=self.DEFAULT_FONT, size=25, weight='bold'))
        self._current_word_label.pack(side=tk.TOP, fill=tk.BOTH)

    def _create_lower_pane(self, parent_window: tk.Frame) -> None:
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
        left_frame = tk.Frame(lower_pane, bg=self.BACKGROUND_COLOR_2)
        left_frame.grid(row=0, column=0, sticky=tk.NSEW)

        button_table = tk.Frame(left_frame, bg=self.BACKGROUND_COLOR_2)
        button_table.grid(row=0, column=0, sticky=tk.NSEW)
        self._create_letter_table(button_table, dimension=4)

        # Creating the submit button
        submit_button = tk.Button(
            left_frame,
            text="SUBMIT",
            bg = self.SUBMIT_BUTTON_COLOR,
            fg=self.TEXT_COLOR,
            font=font.Font(family=self.DEFAULT_FONT, size=30, weight='bold'),
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self._callbacks.submit_callback())
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
            text = "C O L L E C T I ON",
            fg = "white",
            bg = self.BACKGROUND_COLOR_2,
            font = font.Font(family=self.DEFAULT_FONT, size=20, weight="bold", underline=True))
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
            xscrollcommand = words_scrollbar_x,
            yscrollcommand = words_scrollbar_y, 
            wrap = tk.NONE, 
            state = "disable",
            bg = self.COLLECTION_COLOR,
            fg=  "white",
            bd = 0,
            height = 1,
            width = 20,
            font=font.Font(family=self.DEFAULT_FONT, size=20))
        self._words_collection.pack(side=tk.LEFT, fill=tk.BOTH)

    def _create_letter_table(self, parent_frame: tk.Frame, dimension: int) -> None:
        """
        """
        # We rely on the fact that the board is squared 
        #   (hence the dimension is X by X)
        for row_index in range(dimension):
            parent_frame.rowconfigure(row_index, minsize=100)
            for column_index in range(dimension):
                parent_frame.columnconfigure(column_index, minsize=100)
                self._create_letter_button(
                    parent_frame,
                    row_index,
                    column_index)
    
    def _create_letter_button(self, parent: tk.Frame, row: int, column: int) -> None:
        """
        """
        button_coordinate = Coordinate(row, column)
        button = tk.Button(
            parent,
            bg = self.LETTER_BUTTON_COLOR,
            fg = self.TEXT_COLOR,
            font = font.Font(family=self.DEFAULT_FONT, size=30, weight='bold'),
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: self._callbacks.letter_callback(button_coordinate))
        button.grid(
            row = row, 
            column = column, 
            sticky = tk.NSEW, 
            padx = 10, 
            pady = 10)
            
        self._letter_buttons[str(button_coordinate)] = (button_coordinate, button)
        return button
