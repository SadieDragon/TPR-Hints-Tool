
# Houses all functions related to the resetting of the tracker.

from hints.data.read_root import get_main_notebook, get_main_tabs
from hints.gui.shopping.agitha import AgithaTab
from hints.gui.shopping.jovani import JovaniTab
from os import abort
from tkinter import messagebox, Tk


def empty_main_tabs(root: Tk, clear_tabs=False) -> None:
    '''Delete the contents of the tabs.'''
    # Error Handling: If this does not exist, break
    if not root.winfo_exists():
        print('The provided window does not exist.')
        abort()

    # Grab the tabs
    tabs = get_main_tabs(root)

    # Clear the tabs- and if requested, destroy them.
    for index, tab in [*enumerate(tabs)]:
        # Always leave the first information tab,
        # but destroy tabs if requested
        if clear_tabs and (index != 0):
            tab.destroy()
        # Otherwise, just empty them
        else:
            [widget.destroy() for widget in tab.winfo_children()]

    # Refill the tabs
    refill_main_tabs(root, clear_tabs)


def refill_main_tabs(root: Tk, clear_tabs: bool) -> None:
    '''Refill the main tabs after emptying them.'''
    # This is a separate function to make editing and understanding
    # easier in future patches.

    # Avoid a circular import by importing here
    from hints.gui.main_page import create_default_notebook

    # Get the main notebook
    notebook = get_main_notebook(root)

    # Get a list of tabs to work with
    tabs = get_main_tabs(notebook)

    # Recreate the default notepad
    create_default_notebook(tabs[0])

    # If we weren't asked to delete these, refill them
    if not clear_tabs:
        # Grab which tab was specifically theirs
        agitha, jovani = tabs[1:3]

        # Recreate the default pages
        AgithaTab(notebook, tab=agitha)
        JovaniTab(notebook, tab=jovani)


def verify_reset(root: Tk) -> None:
    '''Have the user verify they want to reset.'''
    # A warning of "are you sure, mate?" PEP8 compliance
    warning = 'Are you sure? This will wipe everything.'
    if messagebox.askokcancel('Verify Reset', warning):
        empty_main_tabs(root)
