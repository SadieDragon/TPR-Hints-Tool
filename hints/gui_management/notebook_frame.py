
# Holds all of the window management utilities for the tracker

from customtkinter import CTk, CTkTabview
from hints.utils.constants import tab_names


class NotebookFrame:
    '''A class for managing the CTkTabview,
       which is the heart of this program.'''
    # The data tabs, and their contents
    data_tabs = {}

    # The main notebook
    notebook = CTkTabview

    def __init__(self, root: CTk) -> None:
        '''Create the notebook.'''
        # Create the main notebook. ------------------
        self.notebook = CTkTabview(master=root)
        self.notebook.pack(anchor='nw',
                           expand=True,
                           fill='both',
                           padx=5,
                           pady=5)
        # --------------------------------------------

    def set_to_notes_tab(self) -> None:
        '''Change the tab to the notes tab.'''
        self.notebook.set(tab_names.notes_tab_name)
