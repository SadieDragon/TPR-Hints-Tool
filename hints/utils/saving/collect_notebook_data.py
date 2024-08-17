
from customtkinter import (CTkCheckBox,
                           CTkFrame,
                           CTkScrollableFrame,
                           CTkTabview,
                           CTkTextbox,
                           END)

from hints.gui_management.notebook_frame import NotebookFrame
from hints.utils.constants.tab_names import data_tab_names


class CollectNotebookData:
    '''Gather all of the data for actually writing to the file.'''
    # The notebook from the notebook instance
    notebook: CTkTabview

    # The stored information from each tab
    notebook_data = {}

    # Placeholder variables
    tab_name: str                                # Current tab name
    tab_contents: str | list | None              # The contents of the tab
    tab_widgets: list | None                     # Widgets in the tab
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

            # Try grabbing the tab, and its frame contents
            try:
                # Grab the tab
                tab = self.notebook.tab(self.tab_name)

                # Return the list of widgets on that tab
                self.tab_widgets = self.return_children_widgets(tab)
            # If it fails, the tab doesn't exist, so continue to the next.
            except ValueError:
                continue

            # Collect data from a notepad tab
            if self.contains_widget(CTkTextbox):
                self.parse_notepad()
            # Collect data from a checklist tab
            elif self.contains_widget(CTkFrame):
                self.parse_checklist()
            # If we come across a case that is not A or B,
            # then it is something I need to address but have not.
            # (This includes BUGS.)
            else:
                raise NotImplementedError

    def contains_widget(self, target: CTkTextbox | CTkFrame) -> bool:
        '''Tests if a widget of the desired type is within the tab.'''
        for widget in self.tab_widgets:
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

    def get_checklist(self) -> list[CTkCheckBox]:
        '''Grab the checklist out of the frame it is in.'''
        # Architecture notes of the ScrollableFrame are in the log file.
        # This is complicated only because of that.

        # Grab the canvas out of the frame
        canvas = self.return_first_widget(self.target_widget)

        # Grab the scrollable frame out of the canvas
        scrollable_frame = self.return_first_widget(canvas)

        # Return the checklist
        return self.return_children_widgets(scrollable_frame)

    def parse_checklist(self) -> None:
        '''Grab the collection states of the checkbox.'''
        # Get the list of checkboxes
        checkboxes = self.get_checklist()

        # If that checklist is empty, something has gone wrong
        if not checkboxes:
            raise NotImplementedError

        # Update the placeholder variable for the tab contents
        # to be an empty list
        self.tab_contents = []

        # Go through each and get their collection state,
        # and the item that is being marked as collected or not
        for checkbox in checkboxes:
            # Grab the item the checkbox is for
            item = checkbox.cget('text')

            # Grab the on / off value
            collection_status = checkbox.get()

            # Store that as a list
            self.tab_contents.append([item, collection_status])

        # Update the dict
        self.store_data('checklist')

    def parse_notepad(self) -> None:
        '''Store the information from the textbox.'''
        # Grab the contents and remove trailing whitespace
        self.tab_contents = self.target_widget.get('1.0', END).strip()

        # Update the dict
        self.store_data('notepad')

    def return_children_widgets(self,
                                widget: CTkFrame | CTkScrollableFrame) -> list:
        '''A wrapper for the winfo_children function
           in tkinter and customtkinter, which returns
           a list of widgets within the parent widget.'''
        return widget.winfo_children()

    def return_first_widget(self, widget):
        '''A wrapper function to return the first child widget.'''
        return self.return_children_widgets(widget)[0]

    def store_data(self, tab_type: str) -> None:
        '''Store the tab data wrapper function.'''
        self.notebook_data[self.tab_name] = [tab_type, self.tab_contents]
