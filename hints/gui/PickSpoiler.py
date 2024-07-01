
# Hosts the creation function for the spoiler log pop up

from hints.Globals import return_logs_list
from hints.gui.Globals import return_default_bg
from hints.gui.shopping.Agitha import AgithaTab
from hints.gui.shopping.Jovani import JovaniTab
from hints.parse.SpoilerLog import dump_spoiler_log

from tkinter import Button, StringVar, Tk, Toplevel
from tkinter.ttk import Notebook, OptionMenu

# NOTE: https://github.com/SadieDragon/TPR-Hints-Tool/issues/52

def spoiler_pop_up(files: list,
                   notebook: Notebook,
                   agitha: AgithaTab,
                   jovani: JovaniTab,
                   seed_name: str,
                   root: Tk) -> None:
    '''Creates the popup for the user to pick a spoiler log from.'''
    # The pop up window specifically
    pop_up = Toplevel(root, bg=return_default_bg())
    pop_up.title('Pick a spoiler log')
    pop_up.geometry('500x90')

    # The var that will hold the spoiler log choice
    spoiler_log = StringVar()

    # Grab the longest file name
    longest_spoiler_name = max(files, key=len)
    # And then the length of it, +5 for a buffer
    longest = len(longest_spoiler_name) + 5

    spoiler_logs = return_logs_list()

    # The drop down to actually pick the spoiler log
    spoiler_log_dropdown = OptionMenu(pop_up,
                                      spoiler_log,
                                      files[0],
                                      *spoiler_logs)
    spoiler_log_dropdown.config(width=longest)
    spoiler_log_dropdown.pack(padx=5, pady=10)

    # PEP8 compliant command
    c = lambda: dump_spoiler_log(spoiler_log,
                                 notebook,
                                 pop_up,
                                 agitha,
                                 jovani,
                                 seed_name,
                                 root)
    # Confirmation button
    confirm_spoiler_log = Button(pop_up,
                                 text = 'Confirm',
                                 command = c)
    confirm_spoiler_log.pack(padx=5, pady=5)
