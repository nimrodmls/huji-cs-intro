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
from tkinter import font, scrolledtext
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
    BACKGROUND_COLOR_1 = "#2C3639"
    BACKGROUND_COLOR_2 = "#3F4E4F"
    COLLECTION_COLOR = "#3F4E4F"
    LETTER_BUTTON_COLOR = "#A27B5C"
    SUBMIT_BUTTON_COLOR = "#DCD7C9"
    TEXT_COLOR = "white"

    def __init__(self, assets_path) -> None:
        """
        """
        self._primary_window = tk.Tk()
        self._primary_window.title("Boggle Game")

        self._control_panel = tk.Frame(self._primary_window, bg=self.BACKGROUND_COLOR_1)
        self._control_panel.pack(side=tk.TOP, fill=tk.BOTH)

        self._control_panel.columnconfigure(0, weight=2, minsize=200)
        self._score_label = tk.Label(self._control_panel, fg=self.TEXT_COLOR, bg=self.BACKGROUND_COLOR_1, font=tk.font.Font(family='Agency FB', size=20, weight='bold'))
        self._score_label["text"] = "0"
        self._score_label.grid(row=0, column=0, sticky=tk.NSEW)

        self._control_panel.columnconfigure(1, weight=1, minsize=50)
        button = tk.Button(self._control_panel, text="▶", fg="green", bg = self.BACKGROUND_COLOR_1, font=tk.font.Font(family='Agency FB', size=30, weight='bold'), borderwidth=0, highlightthickness=0, command=lambda: print("button_1 clicked"))
        button.grid(row=0, column=1, sticky=tk.NSEW, padx=10, pady=10)

        self._control_panel.columnconfigure(2, weight=2, minsize=200)
        lbl2 = tk.Label(self._control_panel, fg=self.TEXT_COLOR, bg=self.BACKGROUND_COLOR_1, font=tk.font.Font(family='Agency FB', size=20, weight='bold'))
        lbl2["text"] = "TIME"
        lbl2.grid(row=0, column=2, sticky=tk.NSEW)

        self._upper_frame = tk.Frame(self._primary_window, bg=self.BACKGROUND_COLOR_1)
        self._upper_frame.pack(side=tk.TOP, fill=tk.BOTH)
        self._lbl = tk.Label(self._upper_frame, fg="white", bg=self.BACKGROUND_COLOR_1, font=tk.font.Font(family='Agency FB', size=25, weight='bold'))
        self._lbl["text"] = "WORD DISPLAY PLACEHOLDER"
        self._lbl.pack(side=tk.TOP, fill=tk.BOTH)

        self._lower_frame = tk.Frame(self._primary_window, bg=self.BACKGROUND_COLOR_2)
        self._lower_frame.pack(side=tk.TOP, fill=tk.BOTH)
        self._lower_frame.columnconfigure(0, weight=4)
        self._lower_frame.columnconfigure(1, weight=1, minsize=200)

        self._right_frame = tk.Frame(
            self._lower_frame, bg=self.BACKGROUND_COLOR_2, bd=0)#, highlightbackground="#212020", highlightthickness=2)
        self._right_frame.grid(row=0, column=1, sticky=tk.NSEW)
        #self._right_frame.pack(side=tk.RIGHT, fill=tk.BOTH)
        #self._right_frame.columnconfigure(0, weight=1, minsize=200)
        collection_label = tk.Label(
            self._right_frame,
            text="COLLECTION",
            fg="white",
            bg=self.BACKGROUND_COLOR_2,
            font=tk.font.Font(family='Agency FB', size=20))
        collection_label.pack(side=tk.TOP, fill=tk.BOTH)
        #collection_label.grid(column=0, row=0)
        
        # words_frame = tk.Frame(
        #     self._right_frame, bg="#ABCDEF", bd=0, highlightbackground="#212020", highlightthickness=2)
        # words_frame.pack(side=tk.TOP, fill=tk.BOTH)
        # self._words_collection_2 = scrolledtext.ScrolledText(
        #     self._right_frame, height=30, width=40
        # )
        # self._words_collection_2.pack(side=tk.TOP, fill=tk.Y)
        #self._words_collection_2.grid(column=0, row=1)
        

        self._words_scrollbar_x = tk.Scrollbar(self._right_frame, orient=tk.HORIZONTAL)
        self._words_scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)

        self._words_scrollbar_y = tk.Scrollbar(self._right_frame, orient=tk.VERTICAL)
        self._words_scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
        
        self._words_collection = tk.Text(self._right_frame,
        xscrollcommand=self._words_scrollbar_x,
        yscrollcommand=self._words_scrollbar_y, wrap=tk.NONE, state="disable",
        bg=self.COLLECTION_COLOR,
        fg="white",
        bd=0,
        height=1,
        width=25)
        self._words_collection.pack(side=tk.LEFT, fill=tk.BOTH)


        for i in range(20):
            self._words_collection.configure(state="normal")
            self._words_collection.insert(tk.END, "blabla" + str(i) + "\n")
            self._words_collection.configure(state="disable")
        # word_labels = []
        # self._words_frame.columnconfigure(0, weight=1, minsize=200)
        # self._words_frame.rowconfigure(0, weight=1)
        # current_label = tk.Label(self._words_frame)
        # current_label["text"] = "COLLECTION"
        # current_label.grid(row=0, column=0, sticky=tk.NSEW)
        # for i in range(1, 10):
        #     self._words_frame.rowconfigure(i, weight=1)
            
        #     current_label = tk.Label(self._words_frame)
        #     current_label["text"] = "tst{i}"
        #     current_label.grid(row=i, column=0, sticky=tk.NSEW)

        # Creating all the buttons on the GUI
        self._letter_buttons = {}
        self._left_frame = tk.Frame(self._lower_frame, bg=self.BACKGROUND_COLOR_2)
        #self._left_frame.rowconfigure(1, minsize=100)
        self._left_frame.grid(row=0, column=0, sticky=tk.NSEW)

        self._button_frame = tk.Frame(self._left_frame, bg=self.BACKGROUND_COLOR_2)
        self._button_frame.grid(row=0, column=0, sticky=tk.NSEW)
        #self._button_frame.pack(side=tk.LEFT, fill=tk.BOTH)
        self._create_letter_table(self._button_frame, randomize_board())

        submit_button = tk.Button(
            self._left_frame,
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

        self._primary_window.resizable(False, False)

    def _loop_score(self):
        self.set_score(int(self._score_label['text']) + 10)
        self._primary_window.after(2000, self._loop_score)

    def start(self):
        """
        """
        self._loop_score()
        self._primary_window.mainloop()

    def set_score(self, score: int):
        """
        """
        self._score_label['text'] = str(score)

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
            bg = self.LETTER_BUTTON_COLOR,
            fg=self.TEXT_COLOR,
            font=tk.font.Font(family='Agency FB', size=30, weight='bold'),
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