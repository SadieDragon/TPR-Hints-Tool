
# Home to the base functions based on the main page.

from hints.gui.PickSpoiler import spoiler_pop_up
from hints.gui.ResetTracker import verify_reset
from tkinter import Button, Frame
from tkinter.ttk import Notebook

def create_pop_up_buttons(notebook: Notebook, main_page: Frame) -> None:
    '''Creates the buttons responsible for the different pop ups.'''
    # Where I want things placed
    button_placement = {
        'Pick Spoiler Log': 0,
        'Reset Tracker': 1
    }

    for text, column in button_placement.items():
        # Pick the pop up based on the button being created
        command = None
        match text:
            case 'Pick Spoiler Log':
                command = lambda: spoiler_pop_up(notebook)
            case 'Reset Tracker':
                command = lambda: verify_reset(notebook)

        # Create then place the new button
        new_button = Button(main_page, text=text, command=command)
        new_button.grid(padx=5, pady=5, row=0, column=column)
