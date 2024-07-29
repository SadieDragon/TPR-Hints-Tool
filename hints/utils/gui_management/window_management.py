
# Holds all of the window management utilities for the tracker

from hints.control.program import Program
from hints.utils.constants import tab_names


class WindowManagement:
    '''A class for all of the creation utilities.'''
    # The program passed in
    program = Program

    def __init__(self, program: Program) -> None:
        '''Set the program to be locally global.'''
        self.program = program

    def change_title(self, seed_name: str = '') -> None:
        '''Change the title of the window.'''
        # The default without the seed name
        title = 'TPR Hint Notebook'
        # If there was a seed name, append it
        if seed_name:
            title = f'{title} ({seed_name})'

        self.program.root.title(title)

    def set_to_notes_tab(self) -> None:
        '''Change the tab to the notes tab.'''
        self.program.notebook.set(tab_names.notes_tab_name)
