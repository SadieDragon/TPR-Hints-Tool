
# Holds all of the window management utilities for the tracker

from customtkinter import CTk, CTkTabview
from hints.utils.constants import tab_names
from hints.utils.title import return_title


class NotebookFrame:
    '''A class for managing the CTkTabview,
       which is the heart of this program.'''
    # The data tabs, and their contents
    data_tabs = {}

    # The main window and notebook
    root = CTk
    notebook = CTkTabview

    def __init__(self, root: CTk) -> None:
        '''Create the notebook.'''
        # Store root
        self.root = root

        # Create the notebook ------------------------
        self.notebook = CTkTabview(master=self.root)
        self.notebook.pack(anchor='nw',
                           expand=True,
                           fill='both',
                           padx=5,
                           pady=5)
        # --------------------------------------------

    def update_title(self, seed_name: str = '') -> None:
        '''Update the title of the window.'''
        self.root.title(return_title(seed_name))

    def set_to_notes_tab(self) -> None:
        '''Change the tab to the notes tab.'''
        self.notebook.set(tab_names.notes_tab_name)
