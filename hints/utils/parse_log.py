
# The complex utility functions for the spoiler log parsing

from hints.gui_management.managers import ResetUtils
from hints.gui_management.notebook_frame import NotebookFrame

from hints.tabs.shopping.agitha_tab import AgithaTab
from hints.utils.constants import folders
from json import load
from pathlib import Path
from re import findall, sub


class ParseLog:
    '''It just, parses the spoiler log data.'''
    # The notebook instance
    notebook_frame: NotebookFrame

    # The provided spoiler log
    spoiler_log_file: Path

    def __init__(self, notebook_frame: NotebookFrame) -> None:
        '''Set the notebook instance.'''
        self.notebook_frame = notebook_frame

    def dump_and_fill(self,
                      spoiler_log_file: str,
                      resetter: ResetUtils) -> None:
        '''Take the provided path, and dump the log then fill the tabs.'''
        # Set the local var of the log
        self.spoiler_log_file = Path(spoiler_log_file)

        # Change the window title to include the seed name
        seed_name = findall(r'\-\-(.*?)\-\-', spoiler_log_file)[0]
        self.notebook_frame.update_title(seed_name)

        # Parse the provided data
        self.parse_spoiler_log(resetter)

    def dump_log(self) -> dict:
        '''Take the provided file name, and dump the log.'''
        # Re-affix '.json' to the spoiler log's file name
        self.spoiler_log_file = self.spoiler_log_file.with_suffix('.json')

        # Make the path to the log
        spoiler_log_path = (folders.spoiler_log_dir / self.spoiler_log_file)

        # Dump the spoiler log data
        # Ecconia provided the fix for reading the file, encoded in 'UTF-8'
        with open(spoiler_log_path, 'r', encoding='utf-8') as f:
            return load(f)

    def parse_spoiler_log(self, resetter: ResetUtils) -> None:
        '''Parse the spoiler log data.'''
        # NOTE: This does require some arbitrary knowledge of the
        # spoiler log's structure. Sorry in advance.
        # Please refer to the examples in hints/documentation for
        # a rough explanation of the structure.

        # Grab the data from the spoiler log
        spoiler_log_data = self.dump_log()

        # Grab the hints specifically out of the spoiler log
        hints = spoiler_log_data['hints']

        # Go through each hint, grabbing the sign and its data
        for sign, hint_datas in hints.items():
            # Cycle through each piece of hint data
            for hint_data in hint_datas:
                # Grab the hint text itself
                hint_text = hint_data['text']

                # Remove excess spacing from the hint text
                hint_text = sub(r' +', ' ', hint_text)

                # Special handling for Agitha
                if sign == 'Agithas_Castle_Sign':
                    # Go to her parsing
                    AgithaTab(hint_text, resetter)
