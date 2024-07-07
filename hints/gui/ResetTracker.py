
# Houses all functions related to the resetting of the tracker.

from os import abort
from tkinter import messagebox, Frame
from tkinter.ttk import Notebook

def reset(master: Notebook | Frame) -> None:
    '''Reset the target.'''
    # Stramge errors are afoot: DEBUG
    if not master.winfo_exists():
        print("Master does not exist!")
        print("Reset called on:", master)
        abort()

    # Get the widgets of the target master
    children = master.winfo_children()

    # If this is passed a Notebook, it's the tracker,
    # so we need to remove the first 2 tabs from the list
    if isinstance(master, Notebook) and children:
        for _ in range(2):
            del children[0]

    # Remove the widgets.
    [child.destroy() for child in children]


def verify_reset(notebook: Notebook) -> None:
    '''Have the user verify they want to reset.'''
    # A warning of "are you sure, mate?" PEP8 compliance
    warning = 'Are you sure? This will wipe everything.'
    if messagebox.askokcancel('Verify Reset', warning):
        reset(notebook)
