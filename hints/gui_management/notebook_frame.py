
# Holds all of the window management utilities for the tracker

from customtkinter import CTk, CTkTabview
from hints.utils.return_title import return_title


class NotebookFrame:
    '''A class for managing the CTkTabview,
       which is the heart of this program.'''
    # The main window and notebook
    root: CTk
    notebook: CTkTabview

    # The title of the window
    title: str

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
        # Store the seed name
        self.title = seed_name

        # Update the title
        self.root.title(return_title(seed_name))
