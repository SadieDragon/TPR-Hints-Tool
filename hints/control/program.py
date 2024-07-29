
# Somehow avoids the risk of circular imports and dependencies.
# This idea came from Ecconia during his prototyping.
# https://stackoverflow.com/q/7336802
# https://stackoverflow.com/q/9252543 < Much better answers
# This will hopefully be better addressed in the future.

from customtkinter import CTk, CTkTabview


class Program:
    # Root information
    root = CTk              # The root window
    notebook = CTkTabview   # The global variable of the notepad

    # The global data tab vars
    data_tabs = {}          # The storage var of all data tabs

    # The instances
    creator = None           # from hints.gui_management.creation_utils
    resetter = None          # from hints.gui_management.reset_utils
    notebook_manager = None  # from hints.gui_management.window_management
