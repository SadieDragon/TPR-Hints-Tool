
# Home to the global variables and functions of all components.

from os import getcwd, listdir
from pathlib import Path


def return_default_bg() -> str:
    '''Returns the default notebook background.'''
    return '#f9f9f9'


def return_logs_list() -> list:
    '''Returns a list of spoiler logs.'''
    # Get the target folder for the spoiler logs
    spoiler_log_folder = return_spoiler_folder()

    # Get the list of logs within that folder
    spoiler_logs = listdir(spoiler_log_folder)

    return spoiler_logs


def return_spoiler_folder() -> Path:
    '''Returns the spoiler log folder path.'''
    # Get the path of the logs, and return it
    return Path(getcwd()) / 'SpoilerLog'
