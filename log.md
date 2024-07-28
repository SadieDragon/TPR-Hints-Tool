
# This is a log file for the things that I have done.

It is written for my memory purposes when writing changelogs.  
It is provided for clarity when I ask for help.

Please note that I will reset this between releases, to keep it organized.

**July 28, 2024**
- Restructured ``.gitignore`` to be a bit smarter when it comes to me muting files for testing purposes.
- Created ``log.md`` to help scan through my often poorly named commits, to aide in future requests for help.
    - I hope that it will make it easier to scan the commits, and understand what I was trying to achieve in a commit.
- Created the folder ``hints/utils/gui_management`` to handle all of the utility functions in relation to handling gui elements.
    - moved ``reset_utils.py`` into the folder (and all of the import renames), meant to host only resetting functions
    - created ``creation_utils.py``, meant to host only creation functions.
        - All of its functions are wrapped within ``reset_utils.py``,
        until I get to my idea for fixing the circular dependency issue.
        This also means it's not as abstract as I intend, as it will be a folder,
        but I just need to get the prototype going.
        - Moved ``show_warning`` from ``reset_utils.py`` here.
        - Added the function ``create_window`` for creating ``program.root``.
            - this will be part of a different file.
            I want to abstract out the window management to make customization in the future easer.
        - More things will be uncoupled from ``hints_notebook.py`` after the circular dependency is addressed.
- 
