
# Holds all of the reset utilities for the tracker

from customtkinter import CTkFrame
from hints.control.program import Program
from hints.utils.constants import tab_names
from hints.utils.gui_management.creation_utils import CreationUtils
from hints.utils.gui_management.window_management import WindowManagement


class ResetUtils:
    '''A class for all of the reset utilities.'''
    # Instances
    program = Program                  # The program provided
    creation = CreationUtils           # The creation util
    window_manager = WindowManagement  # The window manager

    def __init__(self, program: Program) -> None:
        '''Update the instances.'''
        self.program = program
        self.creation = CreationUtils(self.program)
        self.window_manager = WindowManagement(self.program)

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
            self.add_tab(tab_name)

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
        self.change_title()

        # Reset the tracker
        for tab_name in tab_names.data_tab_names:
            self.reset_tab(tab_name)

        # Tab back if requested
        if tab_back:
            self.program.set_to_notes_tab()

    # Wrapped functions: creation_utils.py ====================================

    # utils/gui_management/creation/widgets
    def add_tab(self, tab_name: str) -> None | CTkFrame:
        '''Wrapper function for creating a tab in the notebook.'''
        self.creation.add_tab(tab_name)

    # utils/gui_management/creation/window
    def create_window(self) -> None:
        '''Wrapper function for creating the window.'''
        self.creation.create_window()

    # utils/gui_management/creation/widgets
    def show_warning(self) -> bool:
        '''Wrapper function for the warning box.'''
        self.creation.show_warning()

    # =========================================================================

    # Wrapped functions: window_mgmt.py =======================================

    def change_title(self, seed_name: str = '') -> None:
        '''Wrapper function for changing the title of the window.'''
        self.window_manager.change_title(seed_name)

    # =========================================================================
