#################################################################
# FILE : gui.py
# WRITER : Nimrod M. ; Ruth S.
# EXERCISE : intro2cs1 ex11 2023
# DESCRIPTION: GUI for the Boggle Game
# STUDENTS I DISCUSSED THE EXERCISE WITH: N/A
# WEB PAGES I USED: N/A
# NOTES: N/A
#################################################################

import tkinter as tk
from tkinter import font
from pathlib import Path
from boggle_board_randomizer import randomize_board
from common import Coordinate

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Projects\huji-cs-intro\week11\assignment\build\assets\frame0")
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class BoggleGUI(object):
    """
    """

    def __init__(self, assets_path) -> None:
        """
        """
        self._assets_path = Path(__file__).parent.resolve() / assets_path
    
        self._primary_window = tk.Tk()
        self._primary_window.title("Boggle Game")

        self._control_panel = tk.Frame(
            self._primary_window, bg="#212020"
        )
        self._control_panel.pack(side=tk.TOP, fill=tk.BOTH)
        self._control_panel.columnconfigure(0, weight=2, minsize=200)
        lbl1 = tk.Label(self._control_panel, bg="#212020", font=tk.font.Font(family='Agency FB', size=20, weight='bold'))
        lbl1["text"] = "SCORE"
        lbl1.grid(row=0, column=0, sticky=tk.NSEW)
        self._control_panel.columnconfigure(1, weight=1, minsize=50)
        button = tk.Button(self._control_panel, text="▶", fg="green", bg = "#212020", font=tk.font.Font(family='Agency FB', size=30, weight='bold'), borderwidth=0, highlightthickness=0, command=lambda: print("button_1 clicked"))
        button.grid(row=0, column=1, sticky=tk.NSEW, padx=10, pady=10)
        self._control_panel.columnconfigure(2, weight=2, minsize=200)
        lbl2 = tk.Label(self._control_panel, bg="#212020", font=tk.font.Font(family='Agency FB', size=20, weight='bold'))
        lbl2["text"] = "TIME"
        lbl2.grid(row=0, column=2, sticky=tk.NSEW)

        self._upper_frame = tk.Frame(
            self._primary_window, bg="#212020"
        )
        self._upper_frame.pack(side=tk.TOP, fill=tk.BOTH)
        self._lbl = tk.Label(self._upper_frame, bg="#212020", font=tk.font.Font(family='Agency FB', size=25, weight='bold'))
        self._lbl["text"] = "WORD DISPLAY PLACEHOLDER"
        self._lbl.pack(side=tk.TOP, fill=tk.BOTH)

        self._lower_frame = tk.Frame(
            self._primary_window, bg="#212020"
        )
        self._lower_frame.pack(side=tk.TOP, fill=tk.BOTH)

        self._words_frame = tk.Frame(
            self._lower_frame, bg="#212020", bd=0, highlightbackground="#212020", highlightthickness=2
        )
        self._words_frame.pack(side=tk.RIGHT, fill=tk.BOTH)

        word_labels = []
        self._words_frame.columnconfigure(0, weight=1, minsize=200)
        self._words_frame.rowconfigure(0, weight=1)
        current_label = tk.Label(self._words_frame)
        current_label["text"] = "COLLECTION"
        current_label.grid(row=0, column=0, sticky=tk.NSEW)
        for i in range(1, 10):
            self._words_frame.rowconfigure(i, weight=1)
            
            current_label = tk.Label(self._words_frame)
            current_label["text"] = "tst{i}"
            current_label.grid(row=i, column=0, sticky=tk.NSEW)

        self._button_frame = tk.Frame(
            self._lower_frame, bg = "white")
        self._button_frame.pack(side=tk.LEFT, fill=tk.BOTH)
        self._letter_buttons = {}
        self._create_letter_table(self._button_frame, randomize_board())

        self._primary_window.resizable(False, False)


    def start(self):
        """
        """
        self._primary_window.mainloop()

    def _create_letter_table(self, parent_frame: tk.Frame, board) -> None:
        """
        """
        # We rely on the fact that the board is squared
        for row_index in range(len(board)):
            parent_frame.rowconfigure(row_index, minsize=100)
            for column_index in range(len(board)):
                parent_frame.columnconfigure(column_index, minsize=100)
                button = self._create_letter_button(
                    parent_frame,
                    board[row_index][column_index],
                    row_index,
                    column_index)
                self._letter_buttons[str(Coordinate(row_index, column_index))] = button
    
    def _create_letter_button(self, parent, text, row, column) -> tk.Button:
        """
        """
        button = tk.Button(
            parent,
            text=text,
            bg = "grey",
            fg="#212020",
            font=tk.font.Font(family='Agency FB', size=35, weight='bold'),
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print(text))
        button.grid(
            row=row, 
            column=column, 
            sticky=tk.NSEW, 
            padx=10, 
            pady=10)
        return button

    def _get_asset_file(self, name: str) -> tk.PhotoImage:
        """
        """
        img = tk.PhotoImage(file=self._assets_path / name)
        return img

gui = BoggleGUI("build\\assets\\frame0")
gui.start()
