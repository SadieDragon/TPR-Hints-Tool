
from pathlib import Path
from shutil import make_archive, rmtree


def create_archive(dir_path: Path) -> None:
    '''Zip up the folder at the provided path.'''
    # Create the zip archive
    make_archive(
        base_name=str(dir_path),  # shutil needs that to be a str
        format='zip',             # Will be a zip folder
        root_dir=dir_path,        # The directory to zip
        base_dir='.'              # Do not include the folder itself
    )

    # Remove the folder
    rmtree(dir_path)
