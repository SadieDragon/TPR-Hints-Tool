
# Holds all of the utility for reloading saved information

from customtkinter import CTkTabview
from os import listdir
from pathlib import Path
from shutil import unpack_archive

from hints.gui_management.notebook_frame import NotebookFrame
from hints.utils.constants.directories import saves_dir


class Reload:
    '''The utility class for reloading save file information.'''
    # The notebook from the notebook instance
    notebook: CTkTabview

    # Placeholder var for the latest save
    current_save_path: Path

    def __init__(self, notebook_frame: NotebookFrame) -> None:
        # Store the notebook
        self.notebook = notebook_frame.notebook

        # Grab the latest save
        self.grab_last_save()

        # Unzip that folder
        self.unzip_save_dir()

        # Grab the data from each tab file (ignoring master save file)
        # Load it onto the notebook

        # Delete the unzipped save folder

    def grab_last_save(self) -> None:
        '''Grab the latest save's path from the save folder.'''
        # Grab the list of save files
        saves_dir_contents = listdir(saves_dir)

        # Store the last zip folder in that list's name
        current_save_name = saves_dir_contents[-1]

        # Create the path to it
        self.current_save_path = saves_dir / current_save_name

    def unzip_save_dir(self) -> None:
        '''Unzip the save archive.'''
        # Grab the name of the zip folder, without the .zip
        dir_name = self.current_save_path.with_suffix('')

        # Unzip the folder
        unpack_archive(extract_dir=dir_name, filename=self.current_save_path)

        # Update the local var with the new path (without the suffix)
        self.current_save_path = dir_name
