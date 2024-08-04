
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

    # Placeholder variables
    tab_name: str                                # Current tab name
    tab_contents: list | None                    # Widgets in the tab
    target_widget: CTkFrame | CTkTextbox | None  # Widget to be parsed

    def __init__(self, notebook_frame: NotebookFrame) -> None:
        '''Store the notebook instance,
           and initialize saving functions.'''
        # Store the notebook
        self.notebook = notebook_frame.notebook

        # Go through the list of data tabs
        for tab_name in data_tab_names:
            # Store the tab name for later updates
            self.tab_name = tab_name

            # Try to grab the contents of the tab
            self.grab_tab_contents()

            # If the tab does not exist,
            # we do not save any information on it
            if self.tab_contents is None:
                continue

            # Save data from a notepad tab
            if self.contains_widget(CTkTextbox):
                self.save_notepad()

            # Save data from a checklist tab
            elif self.contains_widget(CTkFrame):
                self.save_checklist()

            # If we come across a case that is not A or B,
            # then it is something I need to address but have not.
            # (This includes BUGS.)
            else:
                raise NotImplementedError

        # DEBUG
        print(self.tab_data)

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

    def grab_tab_contents(self) -> list | None:
        '''Attempt to grab the tab contents.'''
        # Try grabbing the tab, and its frame information
        try:
            # Grab the tab
            tab = self.notebook.tab(self.tab_name)

            # Then return the list of widgets on that tab
            self.tab_contents = self.return_children_widgets(tab)
        # If it fails, the tab doesn't exist, so return None.
        except ValueError:
            self.tab_contents = None

    def return_children_widgets(self, widget) -> list:
        '''A wrapper for the winfo_children function
           in tkinter and customtkinter, which returns
           a list of widgets within the parent widget.'''
        return widget.winfo_children()

    def return_first_child(self, widget):
        '''A wrapper function to return the first child widget.'''
        return self.return_children_widgets(widget)[0]

    def save_checklist(self) -> None:
        '''Grab the states of the checkbox.'''
        # Ok. The checklist is where things get tricky.
        # Read log.md for more information as to why
        # I chose to write this function like this.

        # The canvas
        canvas = self.return_first_child(self.target_widget)
        # The scrollable frame
        scrollable_frame = self.return_first_child(canvas)

        # The checklist of checkboxes
        checkboxes = self.return_children_widgets(scrollable_frame)

        # Go through each and get their state,
        # and the item that is being marked
        checkboxes_data = []  # Placeholder variable for the data
        for checkbox in checkboxes:
            # Grab the item the checkbox is for
            item = checkbox.cget('text')

            # Grab the on / off value
            collected = checkbox.get()

            # Store that as a list
            checkboxes_data.append([item, collected])

        self.tab_data[self.tab_name] = checkboxes_data

    def save_notepad(self) -> None:
        '''Store the information from the textbox.'''
        # Grab the contents and remove trailing whitespace
        textbox_contents = self.target_widget.get('1.0', END).strip()

        # Store those contents
        self.tab_data[self.tab_name] = textbox_contents
