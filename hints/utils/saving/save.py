
# Holds all of the utility for saving information on the tracker.

from customtkinter import CTkFrame, CTkTextbox, END

from hints.gui_management.notebook_frame import NotebookFrame
from hints.utils.constants.tab_names import data_tab_names


def save(notebook: NotebookFrame) -> None:
    '''Debug / prototyping state'''
    print('I saved.')

    # The dict which will be passed to a text file
    # (Yes, json would make more sense, I don't care.)
    tab_information = {}

    # Go through the list of data tabs
    for tab_name in data_tab_names:
        # Try grabbing the tab, and its frame information
        try:
            # Grab the tab
            tab = notebook.notebook.tab(tab_name)
        # If it fails, the tab doesn't exist, so save as None.
        except ValueError:
            tab = None

        # If the tab does not exist, then we do not save,
        # so carry along.
        if tab is None:
            continue

        # Grab the children from the tab frame.
        tab_contents = tab.winfo_children()[0]

        if isinstance(tab_contents, CTkFrame):
            # TODO: Actually implement the checklist handling.
            read_checklist(tab_contents)
        elif isinstance(tab_contents, CTkTextbox):
            # Read the textbox contants and store the info
            tab_information[tab_name] = read_textbox(tab_contents)
        else:
            # ... er, that was not expected.
            raise NotImplementedError


def read_checklist(tab_contents: CTkFrame) -> None:
    '''Grab the states of the checkbox.'''
    # Ok. The checklist is where things get tricky.
    # Grab the checklist frame
    checklist_frame = tab_contents.winfo_children()[1]

    # Print that information?
    print(checklist_frame.winfo_children())


def read_textbox(tab_contents: CTkTextbox) -> str:
    '''Grab the information from the textbox.'''
    # Grab the contents and remove trailing whitespace
    return tab_contents.get('1.0', END).strip()
