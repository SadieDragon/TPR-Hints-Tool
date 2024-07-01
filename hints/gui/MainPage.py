
# Home to the base functions based on the main page.

from tkinter.ttk import Notebook
from tkinter import Button

def main_page_button(notebook: Notebook,
                     text: str,
                     row_column: list,
                     command=None) -> None:
    '''Create a button on the main page.'''
    row, column = row_column
    new_button = Button(notebook, text=text, command=command)
    new_button.grid(padx=5, pady=5, row=row, column=column)