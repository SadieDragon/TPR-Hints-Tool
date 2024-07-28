
# Holds all of the creation utilities for the tracker

from CTkMessagebox import CTkMessagebox
from customtkinter import CTk
from hints.control.program import Program

class CreationUtils:
    '''A class for all of the creation utilities.'''
    # The program passed in
    program = Program

    def __init__(self, program: Program) -> None:
        '''Set the program to be locally global.'''
        self.program = program

    def create_window(self) -> None:
        '''Create the main window'''
        # Create the window
        self.program.root = CTk()

        # Manage the window size --------------
        self.program.root.geometry('500x500')
        self.program.root.minsize(300, 300)
        # -------------------------------------

        # Set the title to default title
        self.program.change_title()

    def show_warning(self) -> bool:
        '''Create a warning to ask them are ya sure?'''
        warning_box = CTkMessagebox(icon='warning',
                                    option_1='Cancel',
                                    option_2='Yes',
                                    master=self.program.root,
                                    message='This will reset everything.',
                                    title='Are you sure?')

        to_reset = False
        if warning_box.get() == 'Yes':
            to_reset = True

        return to_reset
