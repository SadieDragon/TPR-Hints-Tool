
# This is a log file for the things that I have done.

It is written for my memory purposes when writing changelogs.  
It is provided for clarity when I ask for help.

Please note that I will reset this between releases, to keep it organized.

# To-Do

**Tasks which I recognize I need to do- I will forget to add things here, and I am sorry in advance.**

- I have a lot of random newlines in the markdowns.
It's either that, or super long lines.
Make that uniform.
- Uncouple as much as I can from ``hints_notebook.py`` to reduce circular imports and dependencies.
    - Flesh out the constants system

# Log

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
- Create the folder ``utils/constants``- and save the minor work done separately this time! :D
    - I had to revert this change,
    because ``program.py`` remains a thorn in my side.
    Tackling it like that will not yet work. Woops.
    - This is a prototype and is very likely written poorly.
    - This is only the start of the uncoupling process,
    as I need to take baby bites to prevent straight up bricking the app again.
    - I also added a to-do list to this file for things that aren't in my notes file.
    - This was also suggested by @Ecconia when reviewing the work done on the previous hotfix, due to a couple vars I repeatedly set.
    - The file ``constants.py`` is a control file, creating the constants that have dependencies to avoid future dependency circles (i.e. the reason ``program.py`` exists.)
    - Checklist of what I got out this time around:
        - ``tab_name = 'Notes'`` is now in ``constants/tab_names.py`` as ``notes_tab_name``
        - ``tab_name = 'Bugs'`` is now in ``constants/tab_names.py`` as ``agitha_tab_name``
        - The options tab and spoiler log tab names have now been defined in ``constants/tab_names.py``
        - ``data_tab_names`` is now in ``constants/tab_names.py`` under the same name
- 
