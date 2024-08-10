
# Holds the static folders

from os import getcwd
from pathlib import Path

# The root folder
root_dir = Path(getcwd())

# The spoiler log folder
spoiler_log_dir = root_dir / 'SpoilerLog'

# The save output folder
saves_dir = root_dir / 'Saves'
