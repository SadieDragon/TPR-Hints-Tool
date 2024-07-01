
# Hosts the base spoiler log parsing

from hints.Globals import return_spoiler_folder
from hints.gui.ResetTracker import reset_tracker
from hints.parse.Hints import parse_hints
from hints.gui.shopping.Agitha import AgithaTab
from hints.gui.shopping.Jovani import JovaniTab

from json import load
from re import findall
from tkinter import StringVar, Tk, Toplevel
from tkinter.ttk import Notebook

# NOTE: https://github.com/SadieDragon/TPR-Hints-Tool/issues/52

# TODO: https://github.com/SadieDragon/TPR-Hints-Tool/issues/53

# Run when the spoiler log is picked.
def dump_spoiler_log(spoiler_log: StringVar,
                     notebook: Notebook,
                     pop_up: Toplevel,
                     agitha: AgithaTab,
                     jovani: JovaniTab,
                     seed_name: str,
                     root: Tk) -> None:
    '''Dumps the information from the chosen spoiler log.'''
    # Let go of the window
    pop_up.destroy()

    # Reset the tracker
    reset_tracker(notebook)

    # Figure out which log was chosen
    chosen_log = spoiler_log.get()

    # Set the seed name, which is encased in -- --
    seed_name = findall(r'\-\-(.*?)\-\-', chosen_log)[0]

    # Set the title of the window
    root.title(f'Hint Tracker Tool: {seed_name}')

    # Get the path
    spoiler_log_folder = return_spoiler_folder()
    spoiler_log_path = spoiler_log_folder / chosen_log

    # Dump the data
    with open(spoiler_log_path, 'r') as f:
        spoiler_log_data = load(f)

    # Move on to parse the hints
    parse_hints(spoiler_log_data, agitha, jovani)