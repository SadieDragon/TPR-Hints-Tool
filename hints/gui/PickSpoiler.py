
# Hosts the creation function for the spoiler log pop up

from hints.data.Globals import return_logs_list
from hints.data.parse.SpoilerLog import dump_and_autofill
from hints.gui.Globals import return_default_bg

from tkinter import Button, StringVar, Tk, Toplevel
from tkinter.ttk import Notebook, OptionMenu

def spoiler_pop_up(notebook: Notebook, root: Tk) -> None:
    '''Creates the popup for the user to pick a spoiler log from.'''
    # Grab the list of available files
    spoiler_logs = return_logs_list()

    # The pop up window specifically
    pop_up = Toplevel(root, bg=return_default_bg())
    pop_up.title('Pick a spoiler log')
    pop_up.geometry('500x90')

    # The var that will hold the spoiler log choice
    spoiler_log = StringVar()

    # Grab the longest file name
    longest_spoiler_name = max(spoiler_logs, key=len)
    # And then the length of it, +5 for a buffer
    longest = len(longest_spoiler_name) + 5

    # The drop down to actually pick the spoiler log
    spoiler_log_dropdown = OptionMenu(pop_up,
                                      spoiler_log,
                                      spoiler_logs[0],
                                      *spoiler_logs)
    spoiler_log_dropdown.config(width=longest)
    spoiler_log_dropdown.pack(padx=5, pady=10)

    # PEP8 compliant command
    c = lambda: dump_and_autofill(spoiler_log,
                                  notebook,
                                  pop_up,
                                  root)
    # Confirmation button
    confirm_spoiler_log = Button(pop_up,
                                 text = 'Confirm',
                                 command = c)
    confirm_spoiler_log.pack(padx=5, pady=5)
