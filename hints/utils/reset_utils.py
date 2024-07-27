
# Holds all of the reset utilities for the tracker

from CTkMessagebox import CTkMessagebox
from customtkinter import CTkFrame
from hints.control.program import Program


class ResetUtils:
    '''A class for all of the reset utilities.'''
    # The program passed in
    program = Program

    def __init__(self, program: Program) -> None:
        '''Set the program to be locally global.'''
        self.program = program

    def close_tab(self, tab_name: str) -> None:
        '''Close a tab in the notebook.'''
        try:
            # Close the tab
            self.program.notebook.delete(tab_name)

            # Remove the key, it no longer exists
            del self.program.data_tabs[tab_name]
        except ValueError:
            pass

    def create_notepad_tab(self) -> None:
        '''Recreate the primary tab.'''
        # The name of the tab
        tab_name = 'Notes'

        # Create the tab
        self.program.add_tab(tab_name)

        # Create the notepad and tab
        notepad = self.program.create_notepad(tab_name)

        # And store the new info
        self.program.update_data_tabs(tab_name, notepad)

    def reset_tab(self, tab_name: str, default: bool = True) -> CTkFrame:
        '''Reset the contents of the tab.'''
        # If the tab does not already exist, create it, and return
        if not tab_name in self.program.data_tabs.keys():
            self.program.add_tab(tab_name)
            return self.program.notebook.tab(tab_name)

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
        self.tracker_wide_reset('reset')

        # Set the notes tab to be the default tab if requested
        if tab_back:
            self.program.set_to_notes_tab()

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

    def tracker_wide_reset(self, type: str) -> None:
        '''A DRY location for a tracker-wide reset- closing or resetting.'''
        for tab_name in self.program.data_tab_names:
            if type == 'close':
                self.close_tab(tab_name)
            elif type == 'reset':
                self.reset_tab(tab_name)
            else:
                raise NotImplementedError
