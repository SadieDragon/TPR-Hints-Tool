
# Holds all of the creation utilities for the tracker

from customtkinter import CTkFrame, CTkTextbox
from hints.gui_management.notebook_frame import NotebookFrame
from hints.utils.constants import tab_names


class CreationUtils:
    '''A class for all of the creation utilities.'''
    # The notebook instance
    notebook_frame: NotebookFrame

    def __init__(self, notebook_frame: NotebookFrame) -> None:
        '''Set the notebook instance.'''
        self.notebook_frame = notebook_frame

    def add_data_tab(self, tab_name: str) -> CTkFrame:
        '''Create specifically a data tab in the notebook.'''
        # Find the index
        tab_index = tab_names.data_tab_names.index(tab_name)

        # Create the tab, and return it
        return self.notebook_frame.notebook.insert(tab_index, tab_name)

    def add_tab(self, tab_name: str) -> CTkFrame:
        '''Create a tab in the notebook.'''
        # Try to return an existing tab
        try:
            return self.notebook_frame.notebook.tab(tab_name)
        # If it fails, create the tab as intended
        # (This function wants this error to occur.)
        except ValueError:
            # If the tab name is in the data tabs list, then create a data tab
            if tab_name in tab_names.data_tab_names:
                return self.add_data_tab(tab_name)

            # Otherwise, just add the tab
            return self.notebook_frame.notebook.add(tab_name)

    def create_data_tabs(self) -> None:
        '''Creates the tabs that have data in their default state.'''
        # Go through and create each tab with a blank notepad,
        # then store the notepad for later use.
        for tab_name in tab_names.data_tab_names:
            self.create_notepad_tab(tab_name)

    def create_notepad_tab(self,
                           tab_name: str,
                           tab: CTkFrame | None = None) -> CTkTextbox:
        '''Creates a notepad under the target tab.'''
        # Create the tab with the provided the tab name
        # if a tab is not provided
        if tab is None:
            tab = self.add_tab(tab_name)

        # Create the notepad -------------------------------------------
        notepad = CTkTextbox(corner_radius=0, master=tab, wrap='word')
        notepad.pack(padx=5, pady=5, expand=True, fill='both')
        # --------------------------------------------------------------

        # Return the notepad
        return notepad
