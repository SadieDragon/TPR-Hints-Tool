
# Holds all of the reset utilities for the tracker

from customtkinter import CTkFrame
from hints.control.program import Program
from hints.utils.constants import tab_names
from hints.utils.gui_management.creation_utils import CreationUtils
from hints.utils.gui_management.window_management import WindowManagement


class ResetUtils:
    '''A class for all of the reset utilities.'''
    # Instances
    program = Program                  # The program instance
    creator = CreationUtils            # The creation utilities instance
    window_manager = WindowManagement  # The window manager

    def __init__(self, program: Program) -> None:
        '''Update the instances.'''
        self.program = program
        self.creation = self.program.creator
        self.window_manager = self.program.window_manager

    def reset_tab(self, tab_name: str, default: bool = True) -> CTkFrame:
        '''Reset the contents of the tab.'''
        # If the tab does not already exist, create it
        if not tab_name in self.program.data_tabs.keys():
            self.creator.add_tab(tab_name)

        # Destroy the frame contents
        if self.program.data_tabs[tab_name] is not None:
            self.program.data_tabs[tab_name].destroy()

        # If requested, place a blank notepad in the tab
        if default:
            new_contents = self.creator.create_notepad_tab(tab_name)
            self.program.update_data_tabs(tab_name, new_contents)

        # Return the tab
        return self.program.notebook.tab(tab_name)

    def reset_tracker(self, tab_back: bool = True) -> None:
        '''Completely reset the tracker.'''
        # Revert the title to default
        self.window_manager.change_title()

        # Reset the tracker
        for tab_name in tab_names.data_tab_names:
            self.reset_tab(tab_name)

        # Tab back if requested
        if tab_back:
            self.window_manager.set_to_notes_tab()
