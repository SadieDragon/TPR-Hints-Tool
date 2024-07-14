
from tkinter import Tk
from tkinter.ttk import Notebook


def get_main_notebook(root: Tk) -> Notebook:
    '''Return simply the notebook.'''
    return root.winfo_children()[0]


def get_main_tabs(master: Tk | Notebook) -> list:
    '''Read the root window's notebook for the tabs.'''
    # Get the notebook, if not supplied
    notebook = master
    if not isinstance(master, Notebook):
        notebook = get_main_notebook(master)

    # Get the tabs
    tabs = notebook.winfo_children()

    # Remove the main tab from the list
    del tabs[0]

    # Return the tabs
    return tabs
