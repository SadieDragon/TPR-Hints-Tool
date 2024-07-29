
# Somehow avoids the risk of circular imports and dependencies.
# This idea came from Ecconia during his prototyping.
# https://stackoverflow.com/q/7336802
# https://stackoverflow.com/q/9252543 < Much better answers
# This will hopefully be better addressed in the future.

from customtkinter import CTk, CTkFrame, CTkTabview, CTkTextbox


class Program:
    # Root information
    root = CTk              # The root window
    notebook = CTkTabview   # The global variable of the notepad

    # The global data tab vars
    data_tabs = {}          # The storage var of all data tabs

    # The instances
    creator = None          # from hints.utils.gui_management.creation_utils
    deleter = None          # from hints.utils.gui_management.deletion_utils
    resetter = None         # from hints.utils.gui_management.reset_utils
    window_manager = None   # from hints.utils.gui_management.window_management

    # Functions that are required elsewhere. ----------------------------------

    def update_data_tabs(self,
                         tab_name: str,
                         tab_content: CTkTextbox | CTkFrame | None) -> None:
        '''Update the storage of data tab info'''
        pass

    # -------------------------------------------------------------------------
