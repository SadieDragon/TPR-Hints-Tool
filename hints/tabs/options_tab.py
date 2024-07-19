
# For easy expansion in the future: A class hosting all of the options
# (well. Most of them. Spoiler is probs its own thing.)

from customtkinter import CTkButton, CTkFrame
from hints.control.program import Program


class OptionsTab:
    # Store the program passed in
    program = None

    def __init__(self, program: Program) -> None:
        '''Create the tab with the options, flexibly.'''
        # Set the program locally
        self.program = program

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
        reset_tracker = CTkButton(command=self.program.reset_tracker,
                                  master=buttons_frame,
                                  text='Reset Tracker')
        reset_tracker.grid(column=1, padx=5, pady=5, row=0)
        # -------------------------------------------------------------

    def race_mode(self) -> None:
        '''The command for race mode.'''
        # Close every tab
        self.program.close_all_tabs()

        # Recreate the notes page
        self.program.create_notepad_tab()
