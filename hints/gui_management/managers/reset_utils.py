
# Holds all of the reset utilities for the tracker

from CTkMessagebox import CTkMessagebox
from customtkinter import CTkFrame
from hints.control.program import Program
from hints.utils.constants import tab_names
from hints.utils.title import return_title

from hints.gui_management.managers.creation_utils import CreationUtils
from hints.gui_management.notebook_frame import NotebookFrame


class ResetUtils:
    '''A class for all of the reset utilities.'''
    # Instances
    program = Program                 # The program instance
    creator = CreationUtils           # The creation utilities instance
    notebook_manager = NotebookFrame  # The notebook manager

    def __init__(self, program: Program) -> None:
        '''Update the instances.'''
        self.program = program
        self.creation = self.program.creator
        self.notebook_manager = self.program.notebook_manager

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
            self.creator.create_notepad_tab(tab_name)

        # Return the tab
        return self.program.notebook.tab(tab_name)

    def reset_tracker(self, tab_back: bool = True) -> None:
        '''Completely reset the tracker.'''
        # Revert the title to default
        self.program.root.title(return_title())

        # Reset the tracker
        for tab_name in tab_names.data_tab_names:
            self.reset_tab(tab_name)

        # Tab back if requested
        if tab_back:
            self.notebook_manager.set_to_notes_tab()

    def show_warning(self) -> bool:
        '''Create a warning to ask them are ya sure?'''
        warning_box = CTkMessagebox(icon='warning',
                                    option_1='Cancel',
                                    option_2='Yes',
                                    master=self.program.root,
                                    message='This will reset everything.',
                                    title='Are you sure?')

        to_reset = False
        if warning_box.get() == 'Yes':
            to_reset = True

        return to_reset
