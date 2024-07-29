
# A class hosting all of the basic options,
# for more flexible and future-proof code

from customtkinter import CTkButton, CTkFrame
from hints.control.program import Program
from hints.utils.constants import tab_names

from hints.gui_management.managers.creation_utils import CreationUtils
from hints.gui_management.managers.deletion_utils import DeletionUtils
from hints.gui_management.managers.reset_utils import ResetUtils
from hints.gui_management.notebook_manager import NotebookManager


class OptionsTab:
    '''Hosts all of the Option Tab setup.'''
    # Instances
    program = Program                   # The program instance
    creator = CreationUtils             # The creator, set by the program
    deleter = DeletionUtils             # The deleter, set by the program
    resetter = ResetUtils               # The reseter, set by the program
    notebook_manager = NotebookManager  # The notebook, set by the program

    def __init__(self, program: Program) -> None:
        '''Create the tab with the options, flexibly.'''
        # Set the program locally
        self.program = program

        # Grab the necessary instances from the program
        self.creator = self.program.creator
        self.deleter = self.program.deleter
        self.resetter = self.program.resetter
        self.notebook_manager = self.program.notebook_manager

        # Create the tab itself
        options_tab = program.notebook.add(tab_names.options_tab_name)

        # And a sub frame for the buttons
        buttons_frame = CTkFrame(master=options_tab)
        buttons_frame.pack(padx=5, pady=5)

        # Race Mode ---------------------------------------
        race_button = CTkButton(command=self.race_mode,
                                master=buttons_frame,
                                text='Race Mode')
        race_button.grid(column=0, padx=5, pady=5, row=0)
        # -------------------------------------------------

        # Reset Tracker ------------------------------------
        reset_button = CTkButton(command=self.reset,
                                  master=buttons_frame,
                                  text='Reset Tracker')
        reset_button.grid(column=1, padx=5, pady=5, row=0)
        # --------------------------------------------------

    def race_mode(self) -> None:
        '''The command for race mode.'''
        # Get permission to reset the tracker
        if not self.creator.show_warning():
            return

        # Go through the data tabs
        for index, tab_name in [*enumerate(tab_names.data_tab_names)]:
            # Reset the notes tab
            if index == 0:
                self.resetter.reset_tab(tab_name)
                continue

            # Close everything else
            self.deleter.close_tab(tab_name)

        self.notebook_manager.set_to_notes_tab()

    def reset(self) -> None:
        '''A wrapper for the tracker reset.'''
        # Get permission to reset the tracker
        if not self.creator.show_warning():
            return

        # Reset the tracker
        self.resetter.reset_tracker()
