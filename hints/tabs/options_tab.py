
# A class hosting all of the basic options,
# for more flexible and future-proof code

from customtkinter import CTkButton, CTkFrame
from hints.control.program import Program
from hints.utils.reset_utils import ResetUtils


class OptionsTab:
    '''Hosts all of the Option Tab setup.'''
    # Instances
    program = Program      # The program passed in
    resetter = ResetUtils  # The reset instance, set by the program

    def __init__(self, program: Program) -> None:
        '''Create the tab with the options, flexibly.'''
        # Set the program locally
        self.program = program

        # Update the resetter to be the program's instance
        self.resetter = program.resetter

        # Create the tab itself
        options_tab = program.notebook.add('Options')

        # And a sub frame for the buttons
        buttons_frame = CTkFrame(master=options_tab)
        buttons_frame.pack(padx=5, pady=5)

        # Race Mode ---------------------------------------
        race_button = CTkButton(command=self.race_mode,
                                master=buttons_frame,
                                text='Race Mode')
        race_button.grid(column=0, padx=5, pady=5, row=0)
        # -------------------------------------------------

        # Reset Tracker -----------------------------------------------
        reset_button = CTkButton(command=self.resetter.reset_tracker,
                                  master=buttons_frame,
                                  text='Reset Tracker')
        reset_button.grid(column=1, padx=5, pady=5, row=0)
        # -------------------------------------------------------------

    def race_mode(self) -> None:
        '''The command for race mode.'''
        # Close every tab
        self.resetter.close_all_tabs()

        # Recreate the notes page
        self.resetter.create_notepad_tab()

        # Tab back to it
        self.program.set_to_notes_tab()
