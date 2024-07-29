
# Holds all of the creation utilities for the tracker

from customtkinter import CTkFrame, CTkTextbox
from hints.gui_management.notebook_frame import NotebookFrame
from hints.utils.constants import tab_names


class CreationUtils:
    '''A class for all of the creation utilities.'''
    # The notebook instance
    notebook_frame = NotebookFrame

    def __init__(self, notebook_frame: NotebookFrame) -> None:
        '''Set the notebook instance.'''
        self.notebook_frame = notebook_frame

    def add_tab(self, tab_name: str) -> None | CTkFrame:
        '''Create a tab in the notebook.'''
        # If it already exists, don't bother
        if tab_name in self.notebook_frame.data_tabs.keys():
            return

        # Update the data tabs dict
        self.notebook_frame.data_tabs[tab_name] = None

        # Find the index
        tab_index = tab_names.data_tab_names.index(tab_name)

        # Create the tab, and return it
        return self.notebook_frame.notebook.insert(tab_index, tab_name)

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
        self.notebook_frame.data_tabs[tab_name] = notepad

        # Return the notepad
        return notepad
