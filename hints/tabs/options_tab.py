
# For easy expansion in the future: A class hosting all of the options
# (well. Most of them. Spoiler is probs its own thing.)

from customtkinter import CTkButton
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

        # Race mode -------------------------------------------------
        race_button = CTkButton(command=self.race_mode,
                                master=options_tab,
                                text='Race Mode')
        race_button.grid(column=0, padx=5, pady=5, row=0)
        # -----------------------------------------------------------

    def race_mode(self) -> None:
        '''The command for race mode.'''
        # - Close all the data tabs except for the first
        # - Reset the notepad to empty

        # Could just close *every* tab, then create the notepad.
        self.program.close_all_tabs()

        # Recreate the notes page
        self.program.create_notepad_tab()

        # Reset Tracker
        #   - Clears the notepad, and sets the Agitha's and Jovani's tabs
        #     to notepads.
        #     - If they do not exist, recreate them (though this is a bug
        #       that is currently in the app)
        # - Race Mode
        #   - Deletes the Agitha and Jovani Tabs, and resets the notepad
        #     to empty
