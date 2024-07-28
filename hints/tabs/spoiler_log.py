
# The spoiler log tab main creation and basic utilites
# Complex utils are found under hints/utils/parse_log.py

from customtkinter import CTkButton, CTkComboBox, CTkFrame, CTkLabel, StringVar
from hints.control.program import Program
from hints.utils.parse_log import ParseLog
from hints.utils.gui_management.reset_utils import ResetUtils
from os import listdir
from pathlib import Path
from subprocess import check_call


class SpoilerLog:
    '''The class to handle all spoiler log things.'''
    # Instances
    program = Program               # Provided program instance
    parser = ParseLog               # The parser instance
    resetter = ResetUtils           # The reset instance, set by the program

    # The spoiler log folder
    spoiler_logs_folder = Path

    # Local interface vars
    spoiler_tab = CTkFrame          # The tab that we're working in
    spoiler_log_button = CTkButton  # The main button
    interface_frame = None          # The frame hosting the interface elements
    spoiler_log_var = StringVar     # The var for picking the spoiler log

    def __init__(self, program: Program) -> None:
        '''Create the host frames, and the main button.'''
        # Store the program
        self.program = program

        # Init the spoiler log parser
        self.parser = ParseLog(self.program)

        # Update the reset instance
        self.resetter = program.resetter

        # Grab the spoiler log folder
        self.spoiler_logs_folder = self.parser.spoiler_log_folder

        # Create the spoiler log tab
        self.spoiler_tab = self.program.notebook.add('Spoiler Log')

        # The main button that affects the frame -----------------------
        self.spoiler_log_button = CTkButton(command=self.present_logs,
                                            master=self.spoiler_tab,
                                            text='Pick Log')
        self.show_button()
        # --------------------------------------------------------------

    def clipboard_path(self) -> None:
        '''Copies the path to clipboard.'''
        # https://stackoverflow.com/a/41029935
        command = f'echo {self.spoiler_logs_folder}|clip'

        check_call(command, shell=True)

    def create_frame(self) -> None:
        '''Create the frame for the interface.'''
        # Create the frame -----------------------------------------
        self.interface_frame = CTkFrame(master=self.spoiler_tab)
        self.interface_frame.grid(column=0, padx=5, pady=5, row=1)
        # ----------------------------------------------------------

        # Hide the button
        self.spoiler_log_button.grid_forget()

    def create_spoiler_dropdown(self, spoilers: list) -> None:
        '''Create a dropdwon with valid spoiler logs.'''
        # Get permission to reset the tracker
        if not self.resetter.show_warning():
            # Destroy the frame if denied, before returning
            self.destroy_frame()
            return

        # Reset the tracker, but do not tab back
        self.resetter.reset_tracker(False)

        # Make the stringvar to store which was chosen
        self.spoiler_log_var = StringVar(value=spoilers[0])

        # Grab the longest file name and the length of that name,
        # then adjust it so the information fits.
        # It is unknown why (x * 8) was the magic formula for this.
        longest = len(max(spoilers, key=len)) * 8

        # Create the dropdown ---------------------------------------------
        spoiler_log_dropdown = CTkComboBox(master=self.interface_frame,
                                           values=spoilers,
                                           variable=self.spoiler_log_var,
                                           width=longest)
        spoiler_log_dropdown.pack(padx=5, pady=5)
        # -----------------------------------------------------------------

        # Create the confirmation button ------------------------------------
        spoiler_log_confirmation = CTkButton(command=self.dump_spoiler_log,
                                             master=self.interface_frame,
                                             text='Confirm')
        spoiler_log_confirmation.pack(padx=5, pady=5)
        # -------------------------------------------------------------------

    def destroy_frame(self) -> None:
        '''Destroys the interface frame when it's no longer in use.'''
        # If the interface frame was created, destroy it
        if self.interface_frame is not None:
            self.interface_frame.destroy()
            self.interface_frame = None

        # Show the button again
        self.show_button()

    def display_no_logs(self) -> None:
        '''If there are no spoiler logs, ask them to please
        put one in the folder.'''
        # The error label -----------------------------------------------------
        # The error text (for PEP8 compliance, and readability)
        error_text = ('There are no available spoiler logs. Please provide one'
                      ' in the following folder:\n\n'
                      f'{self.spoiler_logs_folder}\n\nClick below to copy'
                      ' the path to your clipboard.')
        # The error label itself
        error_label = CTkLabel(justify='left',
                               master=self.interface_frame,
                               text=error_text,
                               wraplength=450)
        error_label.pack(padx=5, pady=5)
        # ---------------------------------------------------------------------

        # Button Land -----------------------------------------
        # Frame for gridding
        button_frame = CTkFrame(master=self.interface_frame)
        button_frame.pack(padx=5, pady=5)

        # Copy to clipboard button
        copy_button = CTkButton(command=self.clipboard_path,
                                master=button_frame,
                                text='Copy')
        copy_button.grid(column=0, padx=5, pady=5, row=0)

        # Return to the default spoiler tab button
        return_button = CTkButton(command=self.destroy_frame,
                                  master=button_frame,
                                  text='Try Again')
        return_button.grid(column=1, padx=5, pady=5, row=0)
        # -----------------------------------------------------

    def dump_spoiler_log(self) -> None:
        '''Dumps the spoiler log and passes it on to the parser'''
        # Tab back to the notes
        self.program.set_to_notes_tab()

        # Get the chosen log
        spoiler_log = self.spoiler_log_var.get()

        # Destroy the interface frame if necessary
        self.destroy_frame()

        # Dump and fill the tabs
        self.parser.dump_and_fill(spoiler_log)

    def present_logs(self) -> None:
        '''Presents a list of the spoiler logs available.'''
        # Destroy any frame which might be leftover
        self.destroy_frame()

        # Get the spoiler logs available
        spoiler_logs = listdir(self.spoiler_logs_folder)

        # Validate which files can actually be used
        valid_spoilers = []
        for spoiler_log_file in spoiler_logs:
            if spoiler_log_file.endswith('.json'):
                # Append only the file name, without the .json
                # While .replace works, jaq suggests this for cross-platform.
                file_name = str(Path(spoiler_log_file).with_suffix(''))
                valid_spoilers.append(file_name)

        # Create the frame for the upcoming interfaces
        self.create_frame()

        if valid_spoilers:
            # Create a dropdown list for the user to pick from
            self.create_spoiler_dropdown(valid_spoilers)
        else:
            # Create the error page for no available spoiler logs
            self.display_no_logs()

    def show_button(self) -> None:
        '''Pack the button so the user can see it again.'''
        self.spoiler_log_button.grid(column=0, padx=5, pady=5, row=0)
