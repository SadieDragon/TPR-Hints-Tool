
# Home to the base functions based on the main page.

from hints.data.read_root import read_root
from hints.gui.pick_spoiler import spoiler_pop_up
from hints.gui.utils import create_notebook_tab, create_scrollable
from os import abort
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
        if text == 'Pick Spoiler Log':
            set_spoiler_command(new_button, notebook, root)
        elif text == 'Race Mode':
            set_race_command(new_button, root)
        elif text in ['Race Mode', 'Reset Tracker']:
            set_reset_command(new_button, root)
        elif text == 'Test':
            set_test_command(new_button, root)
        else:
            print(f'There is no command for {text}, dev.')
            abort()


# PEP8 Compliancy- ... don't use lambdas like that?
# ... https://stackoverflow.com/a/37489941
# This will be greatly improved once I get the
# "hey, root, info plz" working :/
def set_race_command(button: Button, root: Tk) -> None:
    '''PEP8 compliant: set the command for the race button.'''
    # Avoid a circular import by importing here.
    from hints.gui.reset_tracker import empty_main_tabs
    button.config(command=lambda: empty_main_tabs(root, True))


def set_reset_command(button: Button, root: Tk) -> None:
    '''PEP8 compliant: set the command for the reset button.'''
    from hints.gui.reset_tracker import verify_reset
    button.config(command=lambda: verify_reset(root))


def set_spoiler_command(button: Button,
                        notebook: Notebook,
                        root: Tk) -> None:
    '''PEP8 compliant: set the command for the spoiler log button.'''
    button.config(command=lambda: spoiler_pop_up(notebook, root))


def set_test_command(button: Button, root: Tk) -> None:
    '''PEP8 compliant: set the command for the test button.'''
    button.config(command=lambda: read_root(root))