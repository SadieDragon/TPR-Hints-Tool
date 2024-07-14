
# Home to the base functions based on the main page.

from hints.gui.pick_spoiler import spoiler_pop_up
from hints.gui.utils import create_notebook_tab, create_scrollable
from tkinter import Button, Frame, Tk
from tkinter.ttk import Notebook


def create_default_notebook(master: Notebook | Frame) -> None:
    '''Create the default notebook tab.'''
    # If we are not given a frame, make a frame
    default_page = master
    if not isinstance(master, Frame):
        default_page = create_notebook_tab(master, 'Notes')

    # Create a scrolled text notepad
    create_scrollable(default_page)


def create_pop_up_buttons(notebook: Notebook,
                          main_page: Frame,
                          root: Tk) -> None:
    '''Creates the buttons responsible for the different pop ups.'''
    # Where I want things placed
    button_placement = {
        'Pick Spoiler Log': [0, 0],
        'Reset Tracker': [0, 1],
        'Race Mode': [1, 0],
        'Test': [2, 0]
    }

    for text, (row, column) in button_placement.items():
        # Create then place the new button
        new_button = Button(main_page, text=text)
        new_button.grid(padx=5, pady=5, row=row, column=column)

        # Configure the button commands
        match text:
            case 'Pick Spoiler Log':
                new_button.config(command=lambda: spoiler_pop_up(notebook, root))
            case 'Race Mode':
                # Avoid a circular import by importing here.
                from hints.gui.reset_tracker import reset
                new_button.config(command=lambda: reset(notebook, True))
            case 'Reset Tracker':
                # Avoid a circular import by importing here.
                from hints.gui.reset_tracker import empty_main_tabs
                new_button.config(command=lambda: empty_main_tabs(root))
