
# Houses all functions related to the resetting of the tracker.

from tkinter import messagebox
from tkinter.ttk import Notebook

def reset_tracker(notebook: Notebook) -> None:
    '''Reset the tracker.'''
    # Get the widgets.
    current_tabs = notebook.winfo_children()

    # If there's only 1 tab, we do not need to reset
    if len(current_tabs) > 1:
        print(current_tabs[1].winfo_children())
        # Remove all but the first tab's contents
        for widget in current_tabs[1:]:
            for child in widget.winfo_children():
                child.destroy()


def verify_reset(notebook: Notebook) -> None:
    '''Have the user verify they want to reset.'''
    # A warning of "are you sure, mate?" PEP8 compliance
    warning = 'Are you sure? This will wipe everything.'
    if messagebox.askokcancel('Verify Reset', warning):
        reset_tracker(notebook)
