
# Home to the global variables of all components.

from os import abort, getcwd, listdir
from pathlib import Path

# TODO: https://github.com/SadieDragon/TPR-Hints-Tool/issues/48

def return_logs_list() -> list:
    '''Returns a list of spoiler logs.'''
    # Get the target folder for the spoiler logs
    spoiler_log_folder = return_spoiler_folder()

    # Get the list of logs within that folder
    spoiler_logs = listdir(spoiler_log_folder)

    # If there are no logs and this was called, report error
    if not spoiler_logs:
        print('Please supply at least one spoiler log in the folder below:')
        print(spoiler_log_folder)
        abort()

    return spoiler_logs


def return_spoiler_folder() -> Path:
    '''Returns the spoiler log folder path.'''
    # Get the root folder
    root_folder = Path(getcwd())

    # Get the data folder's path
    data_folder = root_folder / 'hints/data'

    # Get the path of the logs, and return it
    return data_folder / 'SpoilerLog'
