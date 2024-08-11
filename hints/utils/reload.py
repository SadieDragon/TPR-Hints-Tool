
# Holds all of the utility for reloading saved information

from customtkinter import CTkTabview
from os import listdir
from pathlib import Path
from shutil import unpack_archive, rmtree

from hints.gui_management.notebook_frame import NotebookFrame
from hints.utils.constants.directories import saves_dir


class Reload:
    '''The utility class for reloading save file information.'''
    # The notebook from the notebook instance
    notebook: CTkTabview

    # Placeholder vars
    current_save_path: Path  # Placeholder var for the latest save
    notebook_data = {}       # Placeholder var for the save data to go in

    def __init__(self, notebook_frame: NotebookFrame) -> None:
        # Store the notebook
        self.notebook = notebook_frame.notebook

        # Grab the latest save
        self.grab_last_save()

        # Unzip that folder
        self.unzip_save_dir()

        # Grab the data from each tab file (ignoring master save file)
        # Delete the folder that was unpacked
        self.unpack_data()
        print(self.notebook_data)

        # Load it onto the notebook

    def grab_last_save(self) -> None:
        '''Grab the latest save's path from the save folder.'''
        # Grab the list of save files
        saves_dir_contents = listdir(saves_dir)

        # Store the last zip folder in that list's name
        current_save_name = saves_dir_contents[-1]

        # Create the path to it
        self.current_save_path = saves_dir / current_save_name

    def unpack_data(self) -> None:
        '''Grab the save data for each tab and store it to be reloaded.'''
        # Grab the list of files within the directory
        save_files = listdir(self.current_save_path)

        # Grab the contents of each file and dump them into storage
        for save_file in save_files:
            # Skip master.txt
            if 'master' in save_file:
                continue

            # Append the current save's path to the file name
            save_file_path = self.current_save_path / save_file

            # Open it, and grab the contents
            file_contents = []
            with open(save_file_path, 'r') as f:
                file_contents = f.readlines()

            # Grab the first line, and pop off the tab type indicator
            tab_type = file_contents[0]
            tab_type = tab_type.split(': ')[1].strip()

            # Store the rest as the tab contents
            tab_contents = file_contents[2:]

            # The tab name is the file name, without '.txt'
            tab_name = str(Path(save_file).with_suffix(''))

            # Shove those into the notebook data storage as a tuple list
            self.notebook_data[tab_name] = [tab_type, tab_contents]

        # Delete the folder we unpacked
        rmtree(self.current_save_path)

    def unzip_save_dir(self) -> None:
        '''Unzip the save archive.'''
        # Grab the name of the zip folder, without the .zip
        dir_name = self.current_save_path.with_suffix('')

        # Unzip the folder
        unpack_archive(extract_dir=dir_name, filename=self.current_save_path)

        # Update the local var with the new path (without the suffix)
        self.current_save_path = dir_name
