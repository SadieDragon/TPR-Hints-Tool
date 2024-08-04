
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

    # A placeholder variable for the target widget
    target_widget: CTkFrame | CTkTextbox | None

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

            # Save data from a notepad tab
            if self.contains_widget(CTkTextbox):
                self.save_notepad()

            # elif self.contains_widget(CTkFrame):

            # If we come across a case that is not A or B,
            # then it is something I need to address but have not.
            # (This includes BUGS.)
            else:
                raise NotImplementedError

    def contains_widget(self, target: CTkTextbox | CTkFrame) -> bool:
        '''Tests if a widget of the desired type is within the tab.'''
        for widget in self.tab_contents:
            # If we find a widget of the target type,
            # store the index and return.
            if isinstance(widget, target):
                self.target_widget = widget
                return True

        # If it went through the entire list,
        # and made it here, then there was not
        # a widget of the type requested.
        self.target_widget = None
        return False

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

    def save_notepad(self) -> str:
        '''Grab the information from the textbox.'''
        # Grab the contents and remove trailing whitespace
        # return tab_contents.get('1.0', END).strip()
