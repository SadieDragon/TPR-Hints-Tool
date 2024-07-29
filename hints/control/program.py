
# Somehow avoids the risk of circular imports and dependencies.
# This idea came from Ecconia during his prototyping.
# https://stackoverflow.com/q/7336802
# https://stackoverflow.com/q/9252543 < Much better answers
# This will hopefully be better addressed in the future.

from customtkinter import CTk, CTkFrame, CTkTabview, CTkTextbox


class Program:
    # Root information
    root = CTk                          # The root window
    notebook = CTkTabview               # The global variable of the notepad

    # The global data tab vars
    data_tabs = {}                      # The storage var of all data tabs

    # The reset class instance
    resetter = None                     # from hints.utils.reset_utils

    # Functions that are required elsewhere. ----------------------------------
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
    # -------------------------------------------------------------------------
