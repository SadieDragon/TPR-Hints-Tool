
# Holds all of the utility for saving information on the tracker.

from os import listdir, makedirs, remove
from pathlib import Path
from shutil import make_archive, rmtree
from time import strftime

from hints.utils.constants.directories import saves_dir


class CreateSaveDir:
    '''A class that hosts the utilities for saving your progress.'''
    # The stored information from each tab
    tab_data = {}

    def __init__(self, tab_data: dict) -> None:
        '''Initialize saving functions.'''
        # Store the tab data
        self.tab_data = tab_data

        # Write the data to the file
        self.save_to_file()

    def checklist_to_str(self, contents: list) -> str:
        '''Write the checklist formatting.'''
        # The placeholder variable for the output
        to_return = 'tab_type: checklist\n\n'

        # Convert each to 'item_name': bool
        for item_state in contents:
            # Unpack the item and state (readability)
            item, state = item_state

            # Write 'item': bool(state)
            to_return = to_return + f"'{item}': {bool(state)}\n"

        return to_return

    def create_archive(self, dir_path: Path) -> None:
        '''Transform the save folder into a zip archive.'''
        # Create the zip archive
        make_archive(
            base_name=str(dir_path),  # shutil needs that to be a str
            format='zip',             # Will be a zip folder
            root_dir=dir_path,        # The directory to zip
            base_dir='.'              # Do not include the folder itself
        )

        # Remove the folder
        rmtree(dir_path)

    def make_txt_path(self, file_name: str) -> Path:
        '''Returns a Path with the file ending .txt'''
        return Path(file_name).with_suffix('.txt')

    def remove_old_files(self) -> None:
        '''Remove old folders, to avoid flooding the user's storage.'''
        # Grab the list of save files
        saves_dir_contents = listdir(saves_dir)

        # Ignore directories, in case the user extracted a save
        # (Trust them to remove the folders themselves if they care.)
        save_files = []
        for file in saves_dir_contents:
            if file.endswith('.zip'):
                save_files.append(file)

        # Leave if there are less than 5
        if len(save_files) < 5:
            return

        # Grab all but the last 4 files from the list
        files_to_remove = save_files[:-4]

        for file in files_to_remove:
            # Add the save folder to the path
            file_path = saves_dir / file

            # Remove it from the folder
            remove(file_path)

    def save_to_file(self) -> None:
        '''Writes the gathered data to the output file.'''
        # Remove old files before creating a new one.
        self.remove_old_files()

        # NOTE / TODO: The default title will be the save time,
        # but I do want to allow the user to pick a name in the future.

        # Grab the time of the save
        # month-day-year (hour-minute)
        # Hours are 24 hour style
        time = strftime('%m-%d-%y (%H-%M)')

        # Making the sub-directory =================================
        # This will be zipped up later. See the log file for info.

        # Create the path
        path_to_current_save_dir = saves_dir / time

        # Make the directory
        # (If it exists, that would be weird but I'm allowing it)
        makedirs(path_to_current_save_dir, exist_ok=True)
        # ==========================================================

        # Create the path to the master file
        path_to_save_file = path_to_current_save_dir / self.make_txt_path(time)

        # Write the file ====================================================
        with open(path_to_save_file, 'w+') as master_file:
            for tab_name, contents in self.tab_data.items():
                # If there is an instance of neither format, something's
                # gone wrong, and I need to write error handling for it.
                if not isinstance(contents, (str, list)):
                    raise NotImplementedError

                # If it is a checklist, then convert it to a str to
                # more easily dump into the files
                section_text = contents
                if isinstance(contents, list):
                    section_text = self.checklist_to_str(contents)
                # If it is a notepad, dump the whole contents into the file
                # as they are already. (plus a newline, and the indicator)
                else:
                    section_text = f'tab_type: notepad\n\n{contents}\n'

                # MASTER FILE ------------------------------------
                # Add a space to the tab name
                padded_tab_name = f'{tab_name} '
                # Pad it out to 80 characters with =
                master_file.write(f'\n{padded_tab_name:=<80}\n')

                # Write the contents of the section
                master_file.write(section_text)
                # ------------------------------------------------

                # TAB FILE -----------------------------------------------
                # Make the text file name using the tab name
                tab_file_name = self.make_txt_path(tab_name)

                # Make the path to the file
                tab_file_path = path_to_current_save_dir / tab_file_name

                # Open the file, and write to it the contents
                with open(tab_file_path, 'w+') as tab_file:
                    tab_file.write(section_text)
                # --------------------------------------------------------
        # ===================================================================

        # Zip the folder up
        self.create_archive(path_to_current_save_dir)
