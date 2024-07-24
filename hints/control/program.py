
# Avoids the risk of circular imports. Somehow.
from customtkinter import CTkFrame, CTkTextbox
from os import getcwd
from pathlib import Path


class Program:
    # The root folder
    root_dir = Path(getcwd())

    # The root window
    root = None

    # The global variable of the notepad to add to
    notebook = None

    # The global variable of the data tabs.
    data_tabs = {}

    # The tabs that are to be created.
    # Easily expandable later.
    data_tab_names = [
        'Notes',
        'Bugs'
    ]

    # The holder of all things reset
    resetter = None

    # Functions that are required elsewhere. --------------------------
    def add_tab(self, tab_name: str) -> None:
        '''Create a tab in the notebook.'''
        pass

    def change_title(self) -> None:
        '''Change the title of the window.'''
        pass

    def create_notepad(self, tab_name: str) -> CTkTextbox:
        '''Creates a notepad under the target tab.'''
        pass

    def set_to_notes_tab(self) -> None:
        '''Change the tab to the notes tab.'''
        pass

    def update_data_tabs(self,
                         tab_name: str,
                         tab_content: CTkTextbox | CTkFrame | None) -> None:
        '''Update the storage of data tab info'''
        pass
    # -----------------------------------------------------------------
