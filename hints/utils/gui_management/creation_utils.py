
# Holds all of the creation utilities for the tracker

from CTkMessagebox import CTkMessagebox
from customtkinter import CTk, CTkFrame, CTkTextbox
from hints.control.program import Program
from hints.utils.constants import tab_names
from hints.utils.gui_management.window_management import WindowManagement


class CreationUtils:
    '''A class for all of the creation utilities.'''
    # The instances
    program = Program                  # The program instance
    window_manager = WindowManagement  # The window manager instance

    def __init__(self, program: Program) -> None:
        '''Set the instances.'''
        self.program = program
        self.window_manager = self.program.window_manager

    def add_tab(self, tab_name: str) -> None | CTkFrame:
        '''Create a tab in the notebook.'''
        # If it already exists, don't bother
        if tab_name in self.program.data_tabs.keys():
            return

        # Update the data tabs dict
        self.program.update_data_tabs(tab_name, None)

        # Find the index
        tab_index = tab_names.data_tab_names.index(tab_name)

        # Create the tab, and return it
        return self.program.notebook.insert(tab_index, tab_name)

    def create_notepad_tab(self, tab_name: str) -> CTkTextbox:
        '''Creates a notepad under the target tab.'''
        # Create the tab at the tab name
        tab = self.program.notebook.tab(tab_name)

        # Create the notepad -----------------------------------
        notepad = CTkTextbox(corner_radius=0, master=tab)
        notepad.pack(padx=5, pady=5, expand=True, fill='both')
        # ------------------------------------------------------

        # Return the notepad
        return notepad

    def create_window(self) -> None:
        '''Create the main window'''
        # Create the window
        self.program.root = CTk()

        # Manage the window size --------------
        self.program.root.geometry('500x500')
        self.program.root.minsize(300, 300)
        # -------------------------------------

        # Set the title to default title
        self.window_manager.change_title()

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
