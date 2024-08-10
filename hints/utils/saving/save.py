
# Holds all of the utility for saving information on the tracker.

from customtkinter import CTkFrame, CTkTabview, CTkTextbox, END
from os import listdir, remove
from pathlib import Path
from time import strftime

from hints.gui_management.notebook_frame import NotebookFrame
from hints.utils.constants.tab_names import data_tab_names
from hints.utils.constants.folders import saves_folder


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

        # Grab the data to write to saving
        self.gather_data()

        # Write the data to the file
        self.save_to_file()

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

    def gather_data(self) -> None:
        '''A wrapper function for the overall functionality
           of gathering data from the different widget types.'''
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

    def remove_old_files(self) -> None:
        '''Remove old folders, to avoid flooding the user's storage.'''
        # Grab the list of save files
        save_files = listdir(saves_folder)

        # Leave if there are less than 5
        if len(save_files) < 5:
            return

        # Grab all but the last 4 files from the list
        files_to_remove = save_files[:-4]

        for file in files_to_remove:
            # Add the save folder to the path
            file_path = saves_folder / file

            # Remove it from the folder
            remove(file_path)

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

        # Store the acquired data
        self.tab_data[self.tab_name] = checkboxes_data

    def save_notepad(self) -> None:
        '''Store the information from the textbox.'''
        # Grab the contents and remove trailing whitespace
        textbox_contents = self.target_widget.get('1.0', END).strip()

        # Store those contents
        self.tab_data[self.tab_name] = textbox_contents

    def save_to_file(self) -> None:
        '''Writes the gathered data to the output file.'''
        # Remove old files before creating a new one.
        self.remove_old_files()

        # Grab the time of the save
        # month-day-year (hour-minute)
        # Hours are 24 hour style
        time = strftime('%m-%d-%y (%H-%M)')

        # The default file name will be '{time}.txt'
        save_file = Path(time).with_suffix('.txt')

        # Create the path
        path_to_save_file = saves_folder / save_file

        # Write the file ====================================================
        with open(path_to_save_file, 'w+') as f:
            for tab_name, contents in self.tab_data.items():
                # Add a space to the tab name
                tab_name = f'{tab_name} '
                # Pad it out to 80 characters with =
                f.write(f'\n{tab_name:=<80}\n')

                # Just dump notepad contents into the file verbatim
                if isinstance(contents, str):
                    f.write(f'{contents}\n')
                # Format the checklist to be human readable
                elif isinstance(contents, list):
                    for item_state in contents:
                        # Unpack the item and state (readability)
                        item, state = item_state

                        # Write 'item': bool(state)
                        f.write(f"'{item}': {bool(state)}\n")
                # If there is something else here, then something has
                # gone wrong somewhere, and I need to write error handling.
                else:
                    raise NotImplementedError
        # ===================================================================
