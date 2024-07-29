
# Holds all of the window management utilities for the tracker

from hints.control.program import Program
from hints.utils.constants import tab_names


class NotebookManager:
    '''A class for all of the creation utilities.'''
    # The program passed in
    program = Program

    def __init__(self, program: Program) -> None:
        '''Set the program to be locally global.'''
        self.program = program

    def set_to_notes_tab(self) -> None:
        '''Change the tab to the notes tab.'''
        self.program.notebook.set(tab_names.notes_tab_name)
