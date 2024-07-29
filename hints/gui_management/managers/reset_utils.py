
# Holds all of the reset utilities for the tracker

from CTkMessagebox import CTkMessagebox
from customtkinter import CTk, CTkFrame
from hints.utils.constants import tab_names
from hints.utils.title import return_title

from hints.gui_management.managers.creation_utils import CreationUtils
from hints.gui_management.notebook_frame import NotebookFrame


class ResetUtils:
    '''A class for all of the reset utilities.'''
    # Instances
    creator = CreationUtils         # The creation utilities instance
    notebook_frame = NotebookFrame  # The notebook manager

    # The root window
    root = CTk

    def __init__(self,
                 creator: CreationUtils,
                 notebook_frame: NotebookFrame,
                 root: CTk) -> None:
        '''Store the provided information.'''
        self.creation = creator
        self.notebook_frame = notebook_frame
        self.root = root

    def close_tab(self, tab_name: str) -> None:
        '''Close a tab in the notebook.'''
        try:
            # Close the tab
            self.notebook_frame.notebook.delete(tab_name)

            # Remove the key, it no longer exists
            del self.notebook_frame.data_tabs[tab_name]
        except ValueError:
            pass

    def reset_tab(self, tab_name: str, default: bool = True) -> CTkFrame:
        '''Reset the contents of the tab.'''
        # If the tab does not already exist, create it
        if not tab_name in self.notebook_frame.data_tabs.keys():
            self.creator.add_tab(tab_name)

        # Destroy the frame contents
        if self.notebook_frame.data_tabs[tab_name] is not None:
            self.notebook_frame.data_tabs[tab_name].destroy()

        # If requested, place a blank notepad in the tab
        if default:
            self.creator.create_notepad_tab(tab_name)

        # Return the tab
        return self.notebook_frame.notebook.tab(tab_name)

    def reset_tracker(self, tab_back: bool = True) -> None:
        '''Completely reset the tracker.'''
        # Revert the title to default
        self.root.title(return_title())

        # Reset the tracker
        for tab_name in tab_names.data_tab_names:
            self.reset_tab(tab_name)

        # Tab back if requested
        if tab_back:
            self.notebook_frame.set_to_notes_tab()

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
