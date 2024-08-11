
# Holds all of the utility for reloading saved information

from customtkinter import CTkTabview

from hints.gui_management.notebook_frame import NotebookFrame


class Reload:
    '''The utility class for reloading save file information.'''
    # The notebook from the notebook instance
    notebook: CTkTabview

    def __init__(self, notebook_frame: NotebookFrame) -> None:
        # Store the notebook
        self.notebook = notebook_frame.notebook

        # Grab the latest save

        # Unzip that folder

        # Grab the data from each tab file (ignoring master save file)
        # Load it onto the notebook

        # Zip back up the folder, and remove the unpacked version.
        # (may not need to do this, we shall see.)
