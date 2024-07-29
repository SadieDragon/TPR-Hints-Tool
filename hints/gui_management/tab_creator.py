
# Creates the many different tabs.

from customtkinter import CTk
from hints.gui_management.managers import ResetUtils
from hints.gui_management.notebook_frame import NotebookFrame
from hints.tabs.options_tab import OptionsTab
from hints.tabs.spoiler_log import SpoilerLog


class TabCreator:
    '''Creates all of the tabs within the program.'''
    def __init__(self, notebook_frame: NotebookFrame, root: CTk) -> None:
        '''Initialize the reset utility instance, and create the tabs.'''
        # Initialize the reset utilities
        resetter = ResetUtils(notebook_frame, root)

        # Create the data tabs
        resetter.create_data_tabs()

        # Create the options tab
        OptionsTab(notebook_frame, root)

        # Create the spoiler log dump tab
        SpoilerLog(notebook_frame, resetter)
