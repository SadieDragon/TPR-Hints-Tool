
# Hosts the main window creation, running,
# and also some basic utitlies acting upon it.

from customtkinter import CTk, CTkTabview

from hints.control.program import Program

from hints.tabs.options_tab import OptionsTab
from hints.tabs.spoiler_log import SpoilerLog

from hints.utils.gui_management.window_manager import create_window
from hints.utils.gui_management.notebook_manager import NotebookManager

from hints.utils.gui_management.creation_utils import CreationUtils
from hints.utils.gui_management.deletion_utils import DeletionUtils
from hints.utils.gui_management.reset_utils import ResetUtils



class HintNotebook(Program):
    '''The main window.'''
    # The root window
    root = CTk

    # The notebook that is the heart of this program
    notebook = NotebookManager

    def __init__(self) -> None:
        '''Initialize the program window.'''
        # Create the window
        self.root = create_window()

        # Create the main notebook
        self.notebook = NotebookManager(self.root)

        # Initialize the gui management instances
        self.create_instances()

        # Create the data tabs
        self.creator.create_data_tabs()

        # Options Tab
        OptionsTab(self)

        # Spoiler Log Tab
        SpoilerLog(self)

        # Run the window
        self.root.mainloop()

    def create_instances(self) -> None:
        '''Creates the gui management instances.'''
        self.creator = CreationUtils(self)
        self.deleter = DeletionUtils(self)
        self.resetter = ResetUtils(self)
