
# Avoids the risk of circular imports. Somehow.
from os import getcwd
from pathlib import Path


class Program:
    # The root folder
    root_dir = Path(getcwd())

    # The global variable of the notepad to add to
    notebook = None

    # The global variable of the data tabs.
    data_tabs = {}

    # Functions that are required elsewhere. --
    def change_title(self) -> None:
        '''Change the title of the window.'''
        pass

    def close_all_tabs(self) -> None:
        '''Close all of the tabs.'''
        pass

    def create_notepad_tab(self) -> None:
        '''Recreate the primary tab.'''
        pass

    def reset_tracker(self) -> None:
        '''Completely reset the tracker.'''
        pass
    # -----------------------------------------
