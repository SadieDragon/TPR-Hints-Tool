
# Holds all of the utility for saving information on the tracker.

from customtkinter import CTkFrame, CTkTabview, CTkTextbox, END

from hints.gui_management.notebook_frame import NotebookFrame
from hints.utils.constants.tab_names import data_tab_names


class SaveNotes:
    '''A class that hosts the utilities for saving your progress.'''
    # The notebook from the notebook instance
    notebook: CTkTabview

    # The stored information from each tab
    tab_data = {}

    # A placeholder variable for the tab contents
    tab_contents: list | None

    def __init__(self, notebook_frame: NotebookFrame) -> None:
        '''Store the notebook instance,
           and initialize saving functions.'''
        # Store the notebook
        self.notebook = notebook_frame.notebook

        # Go through the list of data tabs
        for tab_name in data_tab_names:
            # Try to grab the contents of the tab
            self.grab_tab_contents(tab_name)

            # If the tab does not exist,
            # we do not save any information on it
            if self.tab_contents is None:
                continue

            # DEBUG
            print(self.tab_contents)
            print(self.contains_widget(CTkFrame))

            # if isinstance(tab_contents, CTkFrame):
            #     # TODO: Actually implement the checklist handling.
            #     read_checklist(tab_contents)
            # elif isinstance(tab_contents, CTkTextbox):
            #     # Read the textbox contants and store the info
            #     tab_information[tab_name] = read_textbox(tab_contents)
            # else:
            #     # ... er, that was not expected.
            #     raise NotImplementedError

    def contains_widget(self, target: CTkTextbox | CTkFrame) -> bool:
        '''Tests if a widget of the desired type is within the tab.'''
        # A placeholder var that stores test results,
        # for PEP8 compliance (80 character limits)
        test_outputs = []
        for widget in self.tab_contents:
            test_outputs.append(isinstance(widget, target))

        # Return if any were the target type
        return any(test_outputs)

    def grab_tab_contents(self, tab_name: str) -> list | None:
        '''Attempt to grab the tab contents.'''
        # Try grabbing the tab, and its frame information
        try:
            # Grab the tab
            tab = self.notebook.tab(tab_name)

            # Then return the list of widgets on that tab
            self.tab_contents = tab.winfo_children()
        # If it fails, the tab doesn't exist, so return None.
        except ValueError:
            self.tab_contents = None

    def read_checklist(self) -> None:
        '''Grab the states of the checkbox.'''
        # Ok. The checklist is where things get tricky.
        pass

    def read_textbox(self) -> str:
        '''Grab the information from the textbox.'''
        # Grab the contents and remove trailing whitespace
        # return tab_contents.get('1.0', END).strip()
        pass
