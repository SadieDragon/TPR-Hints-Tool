
# The control file for this folder.

from hints.control.program import Program
from hints.utils.constants import tab_names


class Constants:
    '''Create all of the constants and store them.'''
    # Constants found in tab_names
    notes_tab_name = tab_names.notes_tab_name
    data_tab_names = tab_names.data_tab_names

    # The program instance that is passed around
    # Temporary!
    program: Program

    def set_program(self, program: Program) -> None:
        '''Set the program instance constant.'''
        self.program = program
