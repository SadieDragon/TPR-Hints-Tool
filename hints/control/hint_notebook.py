
# Hosts the main window stuffs

from customtkinter import CTk, CTkFrame, CTkTabview, CTkTextbox
from hints.control.program import Program
from hints.tabs.options_tab import OptionsTab
from hints.tabs.spoiler_log import SpoilerLog
from hints.utils.reset_utils import ResetUtils


class HintNotebook(Program):
    '''The main window.'''
    def __init__(self) -> None:
        '''Initialize the program window.'''
        # Create the main window --------
        self.root = CTk()
        self.root.geometry('500x500')
        self.root.minsize(300, 300)

        # Set the title to default title.
        self.change_title()

        # Create the main notebook. -------------
        self.notebook = CTkTabview(master=self.root)
        self.notebook.pack(anchor='nw',
                           expand=True,
                           fill='both',
                           padx=5,
                           pady=5)
        # ---------------------------------------

        # Initialize the resetter
        self.resetter = ResetUtils(self)

        # Notes, Agitha's Castle
        # (Default state for the latter)
        self.create_data_tabs()

        # Options Tab
        OptionsTab(self)

        # Spoiler Log Tab
        SpoilerLog(self)

        # Run the window
        self.root.mainloop()

    def add_tab(self, tab_name: str) -> None:
        '''Create a tab in the notebook.'''
        # If it already exists, don't bother.
        if tab_name in self.data_tabs.keys():
            return

        # Update the data tabs dict
        self.update_data_tabs(tab_name, None)

        # Find the index
        tab_index = self.data_tab_names.index(tab_name)

        # Create and return the tab
        return self.notebook.insert(tab_index, tab_name)

    def change_title(self, seed_name: str = '') -> None:
        '''Change the title of the window.'''
        # The default without the seed name
        title = 'TPR Hint Notebook'
        # If there was a seed name, append it
        if seed_name:
            title = f'{title} ({seed_name})'

        self.root.title(title)

    def create_data_tabs(self) -> None:
        '''Creates the tabs that have data in their default state.'''
        # Go through and create each tab with a blank notepad, then store.
        for tab_name in self.data_tab_names:
            # Create the notepad that goes in it
            notepad = self.create_notepad(tab_name)

            # Store the notepad under the tab name
            self.update_data_tabs(tab_name, notepad)

    def create_notepad(self, tab_name: str) -> CTkTextbox:
        '''Creates a notepad under the target tab.'''
        # Create the tab at the tab name
        tab = self.add_tab(tab_name)

        # Create the notepad
        notepad = CTkTextbox(corner_radius=0, master=tab)
        notepad.pack(padx=5, pady=5, expand=True, fill='both')

        # Return the notepad
        return notepad

    def set_to_notes_tab(self) -> None:
        '''Change the tab to the notes tab.'''
        self.notebook.set('Notes')

    def update_data_tabs(self,
                         tab_name: str,
                         tab_content: CTkTextbox | CTkFrame | None) -> None:
        '''Update the storage of data tab info'''
        self.data_tabs[tab_name] = tab_content
