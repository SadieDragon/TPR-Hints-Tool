
# Rather than keep spaghetti'ng the spoiler log handling,
# take the data and handle it elsewhere.
from hints.control.program import Program
from json import load
from pathlib import Path
from re import findall


def define_spoilers_folder() -> Path:
    '''Create the path to the spoiler log folder.'''
    return Program.root_dir / 'SpoilerLog'


def dump(spoiler_log_file: str) -> None:
    '''Take the provided file name, and dump the log.'''
    # Re-affix '.json' to the log, and hopefully make the file work again
    spoiler_log_file = Path(''.join(spoiler_log_file, '.json'))

    # Make the path to the log
    spoiler_log_path = (define_spoilers_folder() / spoiler_log_file)


def dump_and_fill(program: Program, spoiler_log_file: str) -> None:
    '''Take the provided path, and dump the log then fill the tabs.'''
    # Reset the tracker
    program.reset_tracker()

    seed_name = findall(r'\-\-(.*?)\-\-', spoiler_log_file)[0]
    program.change_title(seed_name)

    # # Dump the spoiler log data.
    # # The file is encoded in UTF-8, and Ecconia provided this fix.
    # with open(log_path, 'r', encoding='utf-8') as f:
    #     spoiler_log_data = load(f)