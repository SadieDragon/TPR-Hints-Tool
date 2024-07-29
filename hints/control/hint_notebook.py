
# Hosts the main window creation, running,
# and also some basic utitlies acting upon it.

from customtkinter import CTk, CTkTabview

from hints.control.program import Program

from hints.tabs.options_tab import OptionsTab
from hints.tabs.spoiler_log import SpoilerLog

from hints.gui_management.window_manager import create_window
from hints.gui_management.notebook_frame import NotebookFrame

from hints.gui_management.managers.creation_utils import CreationUtils
from hints.gui_management.managers.reset_utils import ResetUtils



class HintNotebook(Program):
    '''The main window.'''
    # The root window
    root = CTk

    # The notebook that is the heart of this program
    notebook = NotebookFrame

    # The management utilities
    creator = CreationUtils  # Manages the creation of widgets (and tabs)
    resetter = ResetUtils    # Manages the reset functions

    def __init__(self) -> None:
        '''Initialize the program window.'''
        # Create the window
        self.root = create_window()

        # Create the main notebook
        self.notebook = NotebookFrame(self.root)

        # Initialize the gui management instances --------------------------
        self.creator = CreationUtils(self.notebook)
        self.resetter = ResetUtils(self.creator, self.notebook, self.root)
        # ------------------------------------------------------------------

        # Create the data tabs
        self.creator.create_data_tabs()

        # Options Tab
        OptionsTab(self)

        # Spoiler Log Tab
        SpoilerLog(self)

        # Run the window
        self.root.mainloop()
