
# Holds all of the creation utilities for the tracker

from CTkMessagebox import CTkMessagebox
from customtkinter import CTkFrame, CTkTextbox
from hints.control.program import Program
from hints.utils.constants import tab_names


class CreationUtils:
    '''A class for all of the creation utilities.'''
    # The instances
    program = Program  # The program instance

    def __init__(self, program: Program) -> None:
        '''Set the instances.'''
        self.program = program

    def add_tab(self, tab_name: str) -> None | CTkFrame:
        '''Create a tab in the notebook.'''
        # If it already exists, don't bother
        if tab_name in self.program.data_tabs.keys():
            return

        # Update the data tabs dict
        self.program.data_tabs[tab_name] = None

        # Find the index
        tab_index = tab_names.data_tab_names.index(tab_name)

        # Create the tab, and return it
        return self.program.notebook.insert(tab_index, tab_name)

    def create_data_tabs(self) -> None:
        '''Creates the tabs that have data in their default state.'''
        # Go through and create each tab with a blank notepad,
        # then store the notepad for later use.
        for tab_name in tab_names.data_tab_names:
            # Create the notepad that goes in it
            self.create_notepad_tab(tab_name)

    def create_notepad_tab(self, tab_name: str) -> CTkTextbox:
        '''Creates a notepad under the target tab.'''
        # Create the tab at the tab name
        tab = self.add_tab(tab_name)

        # Create the notepad -----------------------------------
        notepad = CTkTextbox(corner_radius=0, master=tab)
        notepad.pack(padx=5, pady=5, expand=True, fill='both')
        # ------------------------------------------------------

        # Store the notepad under the tab name
        self.program.data_tabs[tab_name] = notepad

        # Return the notepad
        return notepad

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
