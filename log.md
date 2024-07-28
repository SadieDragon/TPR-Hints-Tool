
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
- Created the folder ``hints/utils/constants`` in an attempt to fix the circular dependency issues
    - This is only the start. I need to start untangling things, and this is the first steps.
    - This was also suggested by @Ecconia when reviewing the work done on the previous hotfix, due to a couple vars I repeatedly set.
    - The file ``constants.py`` is a control file, creating the constants that have dependencies to avoid future dependency circles (i.e. the reason ``program.py`` exists.)
    - Checklist of what I got out this time around:
        - ``tab_name = 'Notes'`` is now in ``constants/tab_names.py`` as ``notes_tab_name``
        - ``data_tab_names`` is now in ``constants/tab_names.py`` under the same name
        - The program instance was moved here as well, to stop needing to pass it around when creating classes
            - This is TEMPORARY. I hope to remove ``program.py`` by the time I am done untangling this mess.
            (In fact, this already does a very good job at removing why this was even a thing)
            - I should've done this as its own commit. That changed so many things.
- 
