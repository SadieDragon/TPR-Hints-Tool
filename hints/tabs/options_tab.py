
# A class hosting all of the basic options,
# for more flexible and future-proof code

from customtkinter import CTkButton, CTkFrame
from hints.utils.constants.constants import Constants
from hints.utils.gui_management.reset_utils import ResetUtils


class OptionsTab:
    '''Hosts all of the Option Tab setup.'''
    # Instances
    program = Constants.program  # The program instance
    resetter = ResetUtils        # The reset instance, set by the program

    def __init__(self) -> None:
        '''Create the tab with the options, flexibly.'''
        # Update the resetter to be the program's instance
        self.resetter = self.program.resetter

        # Create the tab itself
        options_tab = self.program.notebook.add('Options')

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
        if not self.resetter.show_warning():
            return

        # Go through the data tabs
        for index, tab_name in [*enumerate(Constants.data_tab_names)]:
            # Reset the notes tab
            if index == 0:
                self.resetter.reset_tab(tab_name)
                continue

            # Close everything else
            self.resetter.close_tab(tab_name)

        self.program.set_to_notes_tab()

    def reset(self) -> None:
        '''A wrapper for the tracker reset.'''
        # Get permission to reset the tracker
        if not self.resetter.show_warning():
            return

        # Reset the tracker
        self.resetter.reset_tracker()
