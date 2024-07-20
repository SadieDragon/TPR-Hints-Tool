
# Rather than keep spaghetti'ng the spoiler log handling,
# take the data and handle it elsewhere.
from hints.control.program import Program
from hints.tabs.shopping.agitha_tab import AgithaTab
from json import load
from pathlib import Path
from re import findall, sub


# Can I just class this?
class ParseLog:
    '''It just, parses the spoiler log data.'''
    # The root program
    program = None

    # The spoiler log folder
    spoiler_log_folder = None

    # The provided spoiler log
    spoiler_log_file = None

    def __init__(self, program: Program) -> None:
        '''Set the global var here.'''
        # Set the global program var
        self.program = program

        self.spoiler_log_folder = program.root_dir / 'SpoilerLog'

    def dump_and_fill(self, spoiler_log_file: str) -> None:
        '''Take the provided path, and dump the log then fill the tabs.'''
        # Set the local var of the log
        self.spoiler_log_file = spoiler_log_file

        # Change the window title
        seed_name = findall(r'\-\-(.*?)\-\-', spoiler_log_file)[0]
        self.program.change_title(seed_name)

        # Parse the provided data
        self.parse_spoiler_log()

    def dump_log(self) -> dict:
        '''Take the provided file name, and dump the log.'''
        # Re-affix '.json' to the log
        self.spoiler_log_file = Path(self.spoiler_log_file).with_suffix('.json')

        # Make the path to the log
        spoiler_log_path = (self.spoiler_log_folder / self.spoiler_log_file)

        # Dump the spoiler log data.
        # The file is encoded in UTF-8, and Ecconia provided this fix.
        with open(spoiler_log_path, 'r', encoding='utf-8') as f:
            return load(f)

    def parse_spoiler_log(self) -> None:
        '''Parse the spoiler log data.'''
        # NOTE: This does require some arbitrary knowledge of the
        # spoiler log's structure. Sorry in advance.

        # Grab the data from the spoiler log
        spoiler_log_data = self.dump_log()

        # Grab the hints specifically out of the spoiler log
        hints = spoiler_log_data['hints']

        # Go through each hint, grabbing the sign and data
        for sign, hint_datas in hints.items():
            # Cycle through each hint data
            for hint_data in hint_datas:
                # Grab the hint text itself
                hint_text = hint_data['text']

                # Remove excess spacing from the hint text
                hint_text = sub(r' +', ' ', hint_text)

                # Special handling for Agitha
                if sign == 'Agithas_Castle_Sign':
                    # Go to her parsing
                    AgithaTab(self.program, hint_text)
                # Special handling for Jovani
                elif sign == 'Jovani_House_Sign':
                    # Go to his parsing
                    print(hint_text)
