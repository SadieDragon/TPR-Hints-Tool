
# Hosts the main window creation, running,
# and also some basic utitlies acting upon it.

from customtkinter import CTkFrame, CTkTabview, CTkTextbox

from hints.control.program import Program

from hints.tabs.options_tab import OptionsTab
from hints.tabs.spoiler_log import SpoilerLog

from hints.utils.constants import tab_names

from hints.utils.gui_management.creation_utils import CreationUtils
from hints.utils.gui_management.deletion_utils import DeletionUtils
from hints.utils.gui_management.reset_utils import ResetUtils
from hints.utils.gui_management.window_management import WindowManagement


class HintNotebook(Program):
    '''The main window.'''
    def __init__(self) -> None:
        '''Initialize the program window.'''
        # Initialize the gui management instances
        self.create_instances()

        # Create the window
        self.creator.create_window()

        # Create the main notebook. ------------------
        self.notebook = CTkTabview(master=self.root)
        self.notebook.pack(anchor='nw',
                           expand=True,
                           fill='both',
                           padx=5,
                           pady=5)
        # --------------------------------------------

        # Notes, Agitha's Castle
        # (Default state for the latter)
        self.create_data_tabs()

        # Options Tab
        OptionsTab(self)

        # Spoiler Log Tab
        SpoilerLog(self)

        # Run the window
        self.root.mainloop()

    def create_data_tabs(self) -> None:
        '''Creates the tabs that have data in their default state.'''
        # Go through and create each tab with a blank notepad,
        # then store the notepad for later use.
        for tab_name in tab_names.data_tab_names:
            # Create the tab
            self.creator.add_tab(tab_name)

            # Create the notepad that goes in it
            notepad = self.creator.create_notepad_tab(tab_name)

            # Store the notepad under the tab name
            self.update_data_tabs(tab_name, notepad)

    def create_instances(self) -> None:
        '''Creates the gui management instances.'''
        self.creator = CreationUtils(self)
        self.deleter = DeletionUtils(self)
        self.resetter = ResetUtils(self)
        self.window_manager = WindowManagement(self)

    def update_data_tabs(self,
                         tab_name: str,
                         tab_content: CTkTextbox | CTkFrame | None) -> None:
        '''Update the storage of data tab info'''
        self.data_tabs[tab_name] = tab_content
