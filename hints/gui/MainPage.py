
# Home to the base functions based on the main page.

from hints.gui.PickSpoiler import spoiler_pop_up
from hints.gui.ResetTracker import verify_reset
from tkinter import Button, Frame
from tkinter.ttk import Notebook

def create_main_reset_button(notebook: Notebook, main_page: Frame) -> None:
    '''Creates the main page reset button.'''
    command = lambda: verify_reset(notebook)
    main_page_button(main_page, 'Reset Tracker', [0, 1], command)


def create_choose_button(notebook: Notebook, main_page: Frame) -> None:
    '''Creates the button that allows the user to pick a spoiler.'''
    command = lambda: spoiler_pop_up(notebook)
    main_page_button(main_page, 'Pick Spoiler Log', [0, 0], command)


def main_page_button(notebook: Notebook,
                     text: str,
                     row_column: list,
                     command=None) -> None:
    '''Create a button on the main page.'''
    row, column = row_column
    new_button = Button(notebook, text=text, command=command)
    new_button.grid(padx=5, pady=5, row=row, column=column)
