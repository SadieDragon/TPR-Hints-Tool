
# Home to the base functions based on the main page.

from hints.gui.PickSpoiler import spoiler_pop_up
from hints.gui.Utils import create_notebook_tab, create_scrollable
from tkinter import Button, Frame, Tk
from tkinter.ttk import Notebook

def create_default_notebook(notebook: Notebook) -> None:
    '''Create the default notebook tab.'''
    default_page = create_notebook_tab(notebook, 'Notes')
    create_scrollable(default_page)

def create_pop_up_buttons(notebook: Notebook, main_page: Frame, root: Tk) -> None:
    '''Creates the buttons responsible for the different pop ups.'''
    # Where I want things placed
    button_placement = {
        'Pick Spoiler Log': [0, 0],
        'Reset Tracker': [0, 1],
        'Race Mode': [1, 0]
    }

    for text, (row, column) in button_placement.items():
        # Pick the pop up based on the button being created
        command = None
        match text:
            case 'Pick Spoiler Log':
                command = lambda: spoiler_pop_up(notebook, root)
            case 'Reset Tracker':
                from hints.gui.ResetTracker import verify_reset
                command = lambda: verify_reset(notebook)
            case 'Race Mode':
                from hints.gui.ResetTracker import reset
                command = lambda: reset(notebook, True)

        # Create then place the new button
        new_button = Button(main_page, text=text, command=command)
        new_button.grid(padx=5, pady=5, row=row, column=column)
