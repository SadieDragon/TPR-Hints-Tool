
# Houses all functions related to the resetting of the tracker.

from tkinter import messagebox, Frame
from tkinter.ttk import Notebook

def reset(master: Notebook | Frame) -> None:
    '''Reset the target.'''
    print(master)
    # Get the widgets of the target master
    children = master.winfo_children()

    # If this is passed a Notebook, it's the tracker,
    # so we need to remove the first tab from the list
    if type(master) == Notebook:
        del children[0]

    print(children)

    # Remove the widgets.
    [child.destroy() for child in children]


def verify_reset(notebook: Notebook) -> None:
    '''Have the user verify they want to reset.'''
    # A warning of "are you sure, mate?" PEP8 compliance
    warning = 'Are you sure? This will wipe everything.'
    if messagebox.askokcancel('Verify Reset', warning):
        reset(notebook)
