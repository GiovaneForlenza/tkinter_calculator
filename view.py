from tkinter import *
from tkinter import ttk
from tkinter import simpledialog, messagebox
import tkinter as tk


class View(tk.Tk):
    PADDING = 10
    MAX_BUTTON_PER_ROW = 4
    button_captions = [
        'C', '+/-', '%', '/',
        7, 8, 9, '*',
        4, 5, 6, '-',
        1, 2, 3, '+',
        0, '.', '='
    ]

    def __init__(self, controller):
        self.controller = controller
        super().__init__()
        self.title('Calculator')

        self.value_var = tk.StringVar()

        self._make_main_frame()
        self._make_entry()
        self._make_buttons()
        self._center_window()

    def main(self):
        self.mainloop()

    def _make_main_frame(self):
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(padx=self.PADDING, pady=self.PADDING)

    def _make_entry(self):
        entry = ttk.Entry(self.main_frame, justify='right', textvariable=self.value_var)
        entry.pack(fill='x')

    def _make_buttons(self):
        outer_frame = ttk.Frame(self.main_frame)
        outer_frame.pack()

        inner_frame = ttk.Frame(outer_frame)
        inner_frame.pack()

        btns_in_row = 0
        for caption in self.button_captions:
            if btns_in_row == self.MAX_BUTTON_PER_ROW:
                inner_frame = ttk.Frame(outer_frame)
                inner_frame.pack()
                btns_in_row = 0
            btn = ttk.Button(inner_frame, text=caption, command=
            lambda button=caption: self.controller.on_btn_click(button))
            btn.pack(side='left', padx=self.PADDING / 2, pady=self.PADDING)
            btns_in_row += 1

    def _center_window(self):
        self.update()
        width = self.winfo_width()
        height = self.winfo_height()
        x_offset = int((self.winfo_screenwidth() - width *3))
        y_offset = int((self.winfo_screenheight() - height *6))
        self.geometry(f'{width}x{height}+{x_offset}+{y_offset}')
