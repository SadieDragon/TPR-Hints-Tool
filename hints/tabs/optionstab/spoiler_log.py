
# Does the spoiler log handling, which is super complex.
# This goes under hints/tabs/optionstab/options_tab.py.

from customtkinter import CTkButton, CTkFrame, CTkLabel
from hints.control.program import Program


class SpoilerLog:
    '''The class to handle all spoiler log things.'''
    # The program that was passed in
    program = None

    # The main frame
    spoiler_log_main_frame = None

    # The main button
    spoiler_log_button = None

    def __init__(self, program: Program,
                 options_frame: CTkFrame,
                 master_frame: CTkFrame) -> None:
        '''Create the host frames, and the main button.'''
        # Store the program
        self.program = program

        self.spoiler_log_main_frame = master_frame

        # The main button that affects the frame ------------------------------
        self.spoiler_log_button = CTkButton(command=self.test,
                                            master=options_frame,
                                            text='Pick Log')
        # ---------------------------------------------------------------------

    def test(self) -> None:
        '''Test function'''
        test_label = CTkLabel(master=self.spoiler_log_main_frame, text='Hello')
        test_label.grid(column=0, padx=5, pady=5, row=1)
