
# Hosts the base spoiler log parsing

from hints.data.Globals import return_spoiler_folder
from hints.gui.ResetTracker import reset
from hints.data.parse.Hints import parse_hints
from hints.gui.shopping.CreateTabs import create_shopping_tabs

from json import load
from re import findall
from tkinter import StringVar, Tk, Toplevel
from tkinter.ttk import Notebook

def dump_and_autofill(spoiler_log: StringVar,
                      notebook: Notebook,
                      pop_up: Toplevel,
                      root: Tk) -> None:
    '''Button press: Dump the spoiler and then autofill tabs.'''
    # Let go of the window
    pop_up.destroy()

    # Reset the tracker
    reset(notebook)

    # Recreate agitha and jovani, because they get deleted
    agitha, jovani = create_shopping_tabs(notebook)

    # Set the seed name, which is encased in -- --
    seed_name = findall(r'\-\-(.*?)\-\-', spoiler_log.get())[0]

    # Set the title of the window
    root.title(f'Hint Tracker Tool: {seed_name}')

    # Run the dump_spoiler_log
    data = dump_spoiler_log(spoiler_log)

    # And parse the hints
    parse_hints(data, agitha, jovani)


# Run when the spoiler log is picked.
def dump_spoiler_log(spoiler_log: StringVar) -> dict:
    '''Dumps the information from the chosen spoiler log.'''
    # Figure out which log was chosen
    chosen_log = spoiler_log.get()

    # Get the path
    spoiler_log_folder = return_spoiler_folder()
    spoiler_log_path = spoiler_log_folder / chosen_log

    # Dump the data
    with open(spoiler_log_path, 'r') as f:
        return load(f)
