
from tkinter import Frame, Tk
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


def read_root(root: Tk) -> None:
    '''Simply reading the root window.'''
    notebook = root.winfo_children()[0]
    # => [<tkinter.ttk.Notebook object .!notebook>]

    test_reset(notebook)

    # tabs = notebook.winfo_children()
    # # => [<tkinter.Frame object .!notebook.!frame>,
    # #     <tkinter.Frame object .!notebook.!frame2>,
    # #     <tkinter.Frame object .!notebook.!frame3>,
    # #     <tkinter.Frame object .!notebook.!frame4>]
    # # (Main, Notes, Agitha, Jovani)

    # for index, tab in [*enumerate(tabs)]:
    #     if index == 1:
    #         test_reset(tab)

    # # print(notebook.winfo_children())


def test_reset(tab) -> None:
    '''Destroy the frame, as a test.'''
    print(type(tab))