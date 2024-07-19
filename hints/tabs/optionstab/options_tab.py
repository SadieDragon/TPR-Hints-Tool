
# For easy expansion in the future: A class hosting all of the options
# (well. Most of them. Spoiler is probs its own thing.)

from customtkinter import CTkButton, CTkFrame
from hints.control.program import Program
from hints.tabs.optionstab.spoiler_log import SpoilerLog


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

        # Dump Spoiler Log ----------------------------------------------------
        # Have to create the frame here, otherwise it just...
        # breaks... and doesn't place it correctly...
        spoiler_log_main_frame = CTkFrame(master=options_tab)
        spoiler_log_main_frame.pack(
                                    expand=True,
                                    fill='both',
                                    padx=5,
                                    pady=5)

        spoiler_log_class = SpoilerLog(self.program,
                                       buttons_frame,
                                       spoiler_log_main_frame)

        # Grab the button to grid it here and correctly
        # (realized i don't technically need to do that here)
        test_button = spoiler_log_class.spoiler_log_button
        test_button.grid(column=0, padx=5, pady=5, row=1)
        # ---------------------------------------------------------------------

    def create_spoiler_frame(self, tab) -> None:
        '''Create the spoiler log frame?'''
        SpoilerLog(self.program, tab)

    def race_mode(self) -> None:
        '''The command for race mode.'''
        # Close every tab
        self.program.close_all_tabs()

        # Recreate the notes page
        self.program.create_notepad_tab()
