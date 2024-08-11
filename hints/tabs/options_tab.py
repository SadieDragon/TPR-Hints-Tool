
# A class hosting all of the basic options,
# for more flexible and future-proof code

from customtkinter import CTkButton, CTkFrame
from hints.gui_management.managers import ResetUtils
from hints.gui_management.notebook_frame import NotebookFrame
from hints.utils.constants import tab_names

from hints.utils.saving.save_notes import SaveNotes
from hints.utils.reload import Reload


class OptionsTab:
    '''Hosts all of the Option Tab setup.'''
    # The tab itself
    options_tab: CTkFrame

    # The reset utility instance
    resetter: ResetUtils

    # The notebook
    notebook_frame: NotebookFrame

    def __init__(self, resetter: ResetUtils) -> None:
        '''Create the tab with the options, flexibly.'''
        # Initialize the resetter
        self.resetter = resetter

        # Store the notebook frame, which the resetter has
        self.notebook_frame = self.resetter.notebook_frame

        # Create the tab itself
        self.options_tab = self.resetter.add_tab(tab_names.options_tab_name)

        # Create the buttons
        self.create_buttons()

    def create_buttons(self) -> None:
        '''Creates the different buttons that are displayed on this tab.'''
        # Create a sub frame for the buttons --------------
        buttons_frame = CTkFrame(master=self.options_tab)
        buttons_frame.pack(padx=5, pady=5)
        # -------------------------------------------------

        # A list of all the buttons and settings
        # button_text: [command, [row, column]]
        buttons = {
            'Race Mode':     [self.race_mode, [0, 0]],
            'Reset Tracker': [self.reset, [0, 1]],
            'Save':          [self.save, [1, 0]],
            'Reload Save':   [self.reload, [1, 1]]
        }

        # Go through those buttons and create them
        for text, command_coords in buttons.items():
            # Unpack the command and coords, for readability
            command, coords = command_coords

            # Further unpack the row and column, for readability
            row, column = coords

            # Create the new button ---------------------------------
            new_button = CTkButton(command=command,
                                   master=buttons_frame,
                                   text=text)
            new_button.grid(column=column, padx=5, pady=5, row=row)
            # -------------------------------------------------------

    def race_mode(self) -> None:
        '''The command for race mode.'''
        # Get permission to reset the tracker
        if not self.resetter.show_warning():
            return

        # Go through the data tabs
        for index, tab_name in [*enumerate(tab_names.data_tab_names)]:
            # Reset the notes tab
            if index == 0:
                self.resetter.reset_tab(tab_name)
                continue

            # Close everything else
            self.resetter.close_tab(tab_name)

        self.resetter.set_to_notes_tab()

    def reload(self) -> None:
        '''A wrapper for reloading a save.'''
        Reload(self.notebook_frame)

    def reset(self) -> None:
        '''A wrapper for the tracker reset.'''
        # Get permission to reset the tracker
        if not self.resetter.show_warning():
            return

        # Reset the tracker
        self.resetter.reset_tracker()

    def save(self) -> None:
        '''A wrapper for saving.'''
        SaveNotes(self.notebook_frame)
