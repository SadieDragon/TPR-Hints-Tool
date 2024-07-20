
# Rather than keep spaghetti'ng the spoiler log handling,
# take the data and handle it elsewhere.
from hints.control.program import Program
from json import load
from pathlib import Path
from re import findall


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
        # Re-affix '.json' to the log, and hopefully make the file work again
        self.spoiler_log_file = Path(''.join([self.spoiler_log_file, '.json']))

        # Make the path to the log
        spoiler_log_path = (self.spoiler_log_folder / self.spoiler_log_file)

        # Dump the spoiler log data.
        # The file is encoded in UTF-8, and Ecconia provided this fix.
        with open(spoiler_log_path, 'r', encoding='utf-8') as f:
            return load(f)

    def parse_spoiler_log(self) -> None:
        '''Parse the spoiler log data.'''
        # Grab the data from the spoiler log
        spoiler_log_data = self.dump_log()

        print(spoiler_log_data)
