
# Holds all of the utility for saving information on the tracker.

from os import listdir, makedirs, remove
from pathlib import Path
from time import strftime

from hints.utils.create_archive import create_archive
from hints.utils.constants.directories import saves_dir


# NOTE / TODO: The default title will be the save time,
# but I do want to allow the user to pick a name in the future.

class CreateSaveDir:
    '''A class that hosts the utilities for saving your progress.'''
    # The stored information from each tab
    notebook_data = {}

    # The paths to all the files
    path_to_current_save_dir: Path  # The path to the current save dir
    save_file_paths = []            # The paths to the save files

    def __init__(self, notebook_data: dict) -> None:
        '''Initialize saving functions.'''
        # Store the notebook data
        self.notebook_data = notebook_data

        # Remove old files before creating a new one,
        # if there are more than 4 already present
        self.remove_old_files()

        # Create the directory for the current save
        self.create_current_directory()

        # Write the file paths
        self.write_paths()

        # Write the data to the file
        self.save_to_files()

        # Zip up the folder
        create_archive(self.path_to_current_save_dir)

    def checklist_to_str(self, contents: list) -> str:
        '''Write the checklist formatting.'''
        # The placeholder variable for the output
        to_return = ''

        # Convert each to 'item_name': bool
        for item_state in contents:
            # Unpack the item and state (readability)
            item, collection_state = item_state

            # Write 'item': bool(state)
            to_return = to_return + f"{item}: {bool(collection_state)}\n"

        return to_return

    def create_current_directory(self) -> None:
        '''Create the directory for the current save files.'''
        # Get the time of the file writing starting
        # month-day-year (hour-minute) (24 hours)
        time = strftime('%m-%d-%y (%H-%M)')

        # Create the path to the directory for this save
        self.path_to_current_save_dir = saves_dir / time

        # Make the folder that the save files will go into
        # (If it exists, that would be weird but I'm allowing it)
        makedirs(self.path_to_current_save_dir, exist_ok=True)

    def remove_old_files(self) -> None:
        '''Remove old folders, to avoid flooding the user's storage.'''
        # Grab the list of save files
        saves_dir_contents = listdir(saves_dir)

        # Ignore directories, but grab the list
        # of old zip folders
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

    def save_to_files(self) -> None:
        '''Writes the gathered data to the output file.'''
        # Grab master off of the front of the list
        master_file_path = self.save_file_paths.pop(0)

        # Save ===============================================================
        # Open the main file, and begin saving
        with open(master_file_path, 'w+') as master_file:
            # Index the list (PEP8 Compliance: 80 characters)
            enumerated_data = list(enumerate(self.notebook_data.items()))
            for index, (tab_name, type_contents) in enumerated_data:
                # Unpack the type and contents from the list
                tab_type, tab_contents = type_contents

                # If there is an instance of neither format, something's
                # gone wrong, and I need to write error handling for it.
                if not isinstance(tab_contents, (str, list)):
                    raise NotImplementedError

                # If it is a notepad, dump the whole contents into the file
                # as they are already
                section_text = f'{tab_contents}\n'
                # If it is a checklist, then convert it to a str to
                # more easily dump into the files
                if isinstance(tab_contents, list):
                    section_text = self.checklist_to_str(tab_contents)

                # MASTER FILE ------------------------------------
                # Add a space to the tab name
                padded_tab_name = f'{tab_name} '
                # Pad it out to 80 characters with =
                master_file.write(f'\n{padded_tab_name:=<80}\n')

                # Write the contents of the section
                master_file.write(section_text)
                # ------------------------------------------------

                # TAB FILE ---------------------------------------------------
                # Grab the file path
                tab_file_path = self.save_file_paths[index]

                # Open the file, and write to it the contents
                with open(tab_file_path, 'w+') as tab_file:
                    # Append the tab type indicator to the top of
                    # the file
                    section_text = f'tab_type: {tab_type}\n\n{section_text}'

                    tab_file.write(section_text)
                # ------------------------------------------------------------
        # ====================================================================

    def write_paths(self) -> None:
        '''Write the local variables for the paths to the different files.'''
        # Create a list of file names, using the keys of
        # the notebook data (which are the tab names),
        # and prepend master to the list
        file_names = ['master'] + list(self.notebook_data.keys())

        # Append the file extension to each, and create a path object
        for file_name in file_names:
            # Append '.txt' extension to the file name
            tab_save_file_name = Path(file_name).with_suffix('.txt')

            # Create the path to the file
            tab_save_file_path = (self.path_to_current_save_dir /
                                  tab_save_file_name)

            # Store the path
            self.save_file_paths.append(tab_save_file_path)
