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
from pathlib import Path

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

        self._primary_window.geometry("900x800")
        #self._primary_window.configure(bg = "#212020")

        self._upper_frame = tk.Frame(
            self._primary_window,
            height = 200,
            width = 900,
            bg = "#212020",
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        self._upper_frame.pack(side=tk.TOP, fill=tk.BOTH)

        self._lower_frame = tk.Frame(
            self._primary_window,
            height = 700,
            width = 900,
            bg = "#F0F0F3",
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        self._lower_frame.pack(side=tk.TOP, fill=tk.BOTH)
        self._button_frame = tk.Frame(
            self._lower_frame,
            height = 500,
            width = 500,
            bg = "#F0F0F3",
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        
        for i in range(4):
            self._lower_frame.columnconfigure(i, weight=1)
            self._lower_frame.rowconfigure(i, weight=1)

        button = tk.Button(self._lower_frame, text="aa", bg="#212020", borderwidth=0, highlightthickness=0, command=lambda: print("button_1 clicked"))
        # button = tk.Button(
        #     master=self._lower_frame,
        #     image=self._get_asset_file("button.png"),
        #     borderwidth=0,
        #     highlightthickness=0,
        #     command=lambda: print("button_1 clicked"),
        #     relief="flat"
        # )
        button.grid(row=0, column=0, sticky=tk.NSEW, padx=10, pady=10)
        button2 = tk.Button(self._lower_frame, text="ba", bg="#212020", borderwidth=0, highlightthickness=0, command=lambda: print("button_2 clicked"))
        button2.grid(row=0, column=1, sticky=tk.NSEW, padx=10, pady=10)
        #button.pack(side=tk.LEFT)

        # self._primary_canvas = tk.Canvas(
        #     self._primary_window,
        #     bg = "#212020",
        #     height = 200,
        #     width = 900,
        #     bd = 0,
        #     highlightthickness = 0,
        #     relief = "ridge")

        # self._primary_canvas.place(x=0, y=0)
        # self._primary_canvas.create_rectangle(
        #     0,
        #     190,
        #     900,
        #     800,
        #     fill="#F0F0F3",
        #     outline="")
            

        # self._primary_canvas.create_rectangle(
        #     630.0,
        #     250.0,
        #     880.0,
        #     750.0,
        #     fill="#D9D9D9",
        #     outline="")

        self._primary_window.resizable(False, False)


    def start(self):
        """
        """
        self._primary_window.mainloop()

    def _add_letter_button(self, letter: str) -> None:
        """
        """
        button = tk.Button(master=self._primary_window,
            image=self._get_asset_file("button.png"),
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        button.place(
            x=50.0,
            y=250.0,
            width=115.0,
            height=110.0
        )

        return button
    
    def _get_asset_file(self, name: str) -> tk.PhotoImage:
        """
        """
        img = tk.PhotoImage(file=self._assets_path / name)
        return img

gui = BoggleGUI("build\\assets\\frame0")
gui.start()
