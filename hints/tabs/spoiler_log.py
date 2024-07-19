
# Does the spoiler log handling, which is super complex.
# This goes under hints/tabs/optionstab/options_tab.py.

from customtkinter import CTkButton, CTkComboBox, CTkFrame, CTkLabel, StringVar
from hints.control.program import Program
from hints.data.parse_log import define_spoilers_folder, dump_and_fill
from os import listdir
from pathlib import Path


class SpoilerLog:
    '''The class to handle all spoiler log things.'''
    # The program that was passed in
    program = None

    # The spoiler log folder and available logs
    spoiler_logs_folder = None
    spoiler_logs = None

    # The tab that we're working in
    spoiler_tab = None

    # The main button
    spoiler_log_button = None

    # The frame hosting the user-input fields
    interface_frame = None

    # The var for picking the spoiler log
    spoiler_log_var = None

    def __init__(self, program: Program) -> None:
        '''Create the host frames, and the main button.'''
        # Store the program
        self.program = program

        # Grab the spoiler log folder
        self.spoiler_logs_folder = define_spoilers_folder()

        # Get the spoiler logs available
        self.spoiler_logs = listdir(self.spoiler_logs_folder)

        # Create the spoiler log tab
        self.spoiler_tab = self.program.notebook.add('Spoiler Log')

        # The main button that affects the frame ------------------------------
        self.spoiler_log_button = CTkButton(command=self.present_logs,
                                            master=self.spoiler_tab,
                                            text='Pick Log')
        self.show_button()
        # ---------------------------------------------------------------------

    def create_frame(self) -> None:
        '''Create the frame for the interface.'''
        # Create the frame
        self.interface_frame = CTkFrame(master=self.spoiler_tab)
        self.interface_frame.grid(column=0, padx=5, pady=5, row=1)

        # Hide the button
        self.spoiler_log_button.grid_forget()

    def create_spoiler_dropdown(self, spoilers: list) -> None:
        '''Create a dropdwon with valid spoiler logs.'''
        # Make the stringvar to store which was chosen
        self.spoiler_log_var = StringVar(value=spoilers[0])

        # Grab the longest file name, the length of it, then adjust to fit.
        # Idk why *8 worked. I fiddled around with the number until you could
        # read the full file name, and *8 worked.
        longest = len(max(spoilers, key=len)) * 8

        # Create the dropdown
        spoiler_log_dropdown = CTkComboBox(master=self.interface_frame,
                                           values=spoilers,
                                           variable=self.spoiler_log_var,
                                           width=longest)
        spoiler_log_dropdown.pack(padx=5, pady=5)

        # Create confirmation button
        spoiler_log_confirmation = CTkButton(command=self.dump_spoiler_log,
                                             master=self.interface_frame,
                                             text='Confirm')
        spoiler_log_confirmation.pack(padx=5, pady=5)

    def destroy_frame(self) -> None:
        '''Destroys the interface frame when it's no longer in use.'''
        # Destroy the frame
        self.interface_frame.destroy()
        self.interface_frame = None

        # Show the button again
        self.show_button()

    def dump_spoiler_log(self) -> None:
        '''Dumps the spoiler log and passes it on to the parser'''
        # Get the chosen log
        spoiler_log = self.spoiler_log_var.get()

        # Destroy the interface frame
        self.destroy_frame()

        # Dump and fill the tabs
        dump_and_fill(self.program, spoiler_log)

    def present_logs(self) -> None:
        '''Presents a list of the spoiler logs available.'''
        # Validate which files can actually be used
        valid_spoilers = []
        for spoiler_log_file in self.spoiler_logs:
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
            # Create a label telling them hey, uhm, we don't have any?
            print()

    def show_button(self) -> None:
        '''Pack the button so the user can see it again.'''
        self.spoiler_log_button.grid(column=0, padx=5, pady=5, row=0)
