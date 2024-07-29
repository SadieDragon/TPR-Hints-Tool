
# Holds all of the deletion utilities for the tracker

from hints.control.program import Program


class DeletionUtils:
    '''A class for all of the reset utilities.'''
    # Instances
    program = Program  # The program instance

    def __init__(self, program: Program) -> None:
        '''Update the instances.'''
        self.program = program

    def close_tab(self, tab_name: str) -> None:
        '''Close a tab in the notebook.'''
        try:
            # Close the tab
            self.program.notebook.delete(tab_name)

            # Remove the key, it no longer exists
            del self.program.data_tabs[tab_name]
        except ValueError:
            pass
