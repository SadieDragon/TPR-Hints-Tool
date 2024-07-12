# Hosts the creation function for the spoiler log pop up

from hints.data.globals import (return_default_bg,
                                return_logs_list,
                                return_spoiler_folder)
from hints.data.parse.spoiler_log import dump_and_autofill
from tkinter import Button, Label, StringVar, Toplevel
from tkinter.ttk import OptionMenu

from hints.gui.Program import Program


def spoiler_pop_up(program: Program) -> None:
    '''Creates the popup for the user to pick a spoiler log from.'''
    # Grab the list of available files
    spoiler_logs = return_logs_list()

    # Validate which files can actually be used
    valid_spoilers = []
    for spoiler_log_file in spoiler_logs:
        if spoiler_log_file.endswith('.json'):
            valid_spoilers.append(spoiler_log_file)

    # The default background color
    default_bg = return_default_bg()

    # The pop up window specifically
    pop_up = Toplevel(program.root, bg=default_bg)
    pop_up.title('Pick a spoiler log')
    pop_up.geometry('500x90')

    # If there are spoiler logs, let them pick one
    if valid_spoilers:
        # Grab the longest file name
        longest_spoiler_name = max(valid_spoilers, key=len)
        # And then the length of it, +5 for a buffer
        longest = len(longest_spoiler_name) + 5

        # The var that will hold the spoiler log choice
        spoiler_log = StringVar()

        # The drop down to actually pick the spoiler log
        spoiler_log_dropdown = OptionMenu(pop_up,
                                          spoiler_log,
                                          valid_spoilers[0],
                                          *valid_spoilers)
        spoiler_log_dropdown.config(width=longest)
        spoiler_log_dropdown.pack(padx=5, pady=10)

        # Confirmation button
        confirm_log = Button(pop_up, text='Confirm')
        confirm_log.pack(padx=5, pady=5)
        # PEP8 compliant command
        confirm_log.config(command=lambda: dump_and_autofill(spoiler_log,
                                                             program,
                                                             pop_up))
    # Otherwise, inform them to please put the file
    # in the folder.
    else:
        # PEP8 compliant and readable text
        spoiler_label_text = ('Please provide a spoiler log in this folder:\n'
                              f'{return_spoiler_folder()}')

        # Create the warning label
        spoiler_label = Label(pop_up,
                              bg=default_bg,
                              justify='left',
                              text=spoiler_label_text,
                              wraplength=600)
        spoiler_label.pack(padx=5, pady=5)

        # Confirmation button
        spoiler_confirm = Button(pop_up, text='Ok', command=pop_up.destroy)
        spoiler_confirm.pack(padx=5, pady=5)


# See main_page.py for why this stupid area exists.
def set_confirmation_command(button: Button,
                             spoiler_log: StringVar,
                             program: Program,
                             pop_up: Toplevel) -> None:
    '''PEP8 compliant: set the command for the confirmation button.'''
    button.config(command=lambda: dump_and_autofill(spoiler_log,
                                                    program,
                                                    pop_up))
