
# Hosts the main window stuffs

from CTkMessagebox import CTkMessagebox
from customtkinter import CTk, CTkFrame, CTkTabview, CTkTextbox
from hints.control.program import Program
from hints.tabs.options_tab import OptionsTab
from hints.tabs.spoiler_log import SpoilerLog


class HintNotebook(Program):
    '''The main window.'''
    # The root window
    root = None

    # The tabs that are to be created.
    # Easily expandable later.
    data_tab_names = [
        'Notes',
        'Bugs'
    ]

    def __init__(self) -> None:
        '''Initialize the program window.'''
        # Create the main window --------
        self.root = CTk()
        self.root.geometry('500x500')
        self.root.minsize(300, 300)

        # Set the title to default title.
        self.change_title()
        # -------------------------------

        # Create the main notebook. -------------
        self.notebook = CTkTabview(master=self.root)
        self.notebook.pack(anchor='nw',
                           expand=True,
                           fill='both',
                           padx=5,
                           pady=5)
        # ---------------------------------------

        # Notes, Agitha's Castle, and Jovani's Redemption
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

    def close_all_tabs(self) -> None:
        '''Close all of the tabs.'''
        self.tracker_wide_reset('close')

    def close_tab(self, tab_name: str) -> None:
        '''Close a tab in the notebook.'''
        try:
            # Close the tab
            self.notebook.delete(tab_name)

            # Remove the key, it no longer exists
            del self.data_tabs[tab_name]
        except ValueError:
            pass

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

    def create_notepad_tab(self) -> None:
        '''Recreate the primary tab.'''
        # Makes plonking this in easier
        tab_name = 'Notes'

        # Create the notepad and tab
        notepad = self.create_notepad(tab_name)

        # And store the new info
        self.update_data_tabs(tab_name, notepad)

    def reset_tab(self, tab_name: str, default: bool = True) -> None:
        '''Reset the contents of the tab.'''
        # If the tab already exists, close the tab
        if tab_name in self.data_tabs.keys():
            self.close_tab(tab_name)

        if default:
            # Recreate the blank tab
            self.create_notepad(tab_name)
        else:
            # Just add a tab
            self.add_tab(tab_name)

        return self.notebook.tab(tab_name)

    def reset_tracker(self, tab_back: bool = True) -> bool:
        '''Completely reset the tracker.'''
        # Revert the title to default
        self.change_title()

        # Reset the tracker
        permission_granted = self.tracker_wide_reset('reset')

        # Set the notes tab to be the default tab if requested
        if tab_back:
            self.set_to_notes_tab()

        return permission_granted

    def set_to_notes_tab(self) -> None:
        '''Change the tab to the notes tab.'''
        self.notebook.set('Notes')

    def show_warning(self) -> bool:
        '''Create a warning to ask them are ya sure?'''
        warning_box = CTkMessagebox(icon='warning',
                                    option_1='Cancel',
                                    option_2='Yes',
                                    master=self.root,
                                    message='This will reset everything.',
                                    title='Are you sure?')

        to_reset = False
        if warning_box.get() == 'Yes':
            to_reset = True

        return to_reset

    def tracker_wide_reset(self, type: str) -> bool:
        '''A DRY location for a tracker-wide reset- closing or resetting.'''
        permission_granted = self.show_warning()

        if permission_granted:
            for tab_name in self.data_tab_names:
                if type == 'close':
                    self.close_tab(tab_name)
                elif type == 'reset':
                    self.reset_tab(tab_name)
                else:
                    raise NotImplementedError

        return permission_granted

    def update_data_tabs(self,
                         tab_name: str,
                         tab_content: CTkTextbox | CTkFrame | None) -> None:
        '''Update the storage of data tab info'''
        self.data_tabs[tab_name] = tab_content
