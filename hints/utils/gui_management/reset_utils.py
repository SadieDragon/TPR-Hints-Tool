
# Holds all of the reset utilities for the tracker

from customtkinter import CTkFrame
from hints.utils.constants.constants import Constants
from hints.utils.gui_management.creation_utils import CreationUtils


class ResetUtils:
    '''A class for all of the reset utilities.'''
    # Instances
    program = Constants.program  # The program instance
    creation = CreationUtils     # The creation utility instance

    def __init__(self) -> None:
        '''Initialize the creation instance.'''
        self.creation = CreationUtils()

    def close_tab(self, tab_name: str) -> None:
        '''Close a tab in the notebook.'''
        try:
            # Close the tab
            self.program.notebook.delete(tab_name)

            # Remove the key, it no longer exists
            del self.program.data_tabs[tab_name]
        except ValueError:
            pass

    def reset_tab(self, tab_name: str, default: bool = True) -> CTkFrame:
        '''Reset the contents of the tab.'''
        # If the tab does not already exist, create it
        if not tab_name in self.program.data_tabs.keys():
            self.program.add_tab(tab_name)

        # Destroy the frame contents
        if self.program.data_tabs[tab_name] is not None:
            self.program.data_tabs[tab_name].destroy()

        # If requested, place a blank notepad in the tab
        if default:
            new_contents = self.program.create_notepad(tab_name)
            self.program.update_data_tabs(tab_name, new_contents)

        # Return the tab
        return self.program.notebook.tab(tab_name)

    def reset_tracker(self, tab_back: bool = True) -> None:
        '''Completely reset the tracker.'''
        # Revert the title to default
        self.program.change_title()

        # Reset the tracker
        for tab_name in Constants.data_tab_names:
            self.reset_tab(tab_name)

        # Tab back if requested
        if tab_back:
            self.program.set_to_notes_tab()

    # Wrapped functions =======================================================
    # utils/gui_management/creation/window
    def create_window(self) -> None:
        '''Wrapper function for creating the window.'''
        self.creation.create_window()

    # utils/gui_management/creation/widgets
    def show_warning(self) -> bool:
        '''Wrapper function for the warning box.'''
        self.creation.show_warning()
    # =========================================================================
