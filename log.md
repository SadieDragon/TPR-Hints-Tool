
# This is a log file for the things that I have done.

It is written for my memory purposes when writing changelogs. It is provided for clarity when I ask for help.

Please note that I will reset this between releases, to keep it organized.

If you see a blank line between bullets on any given day, it means that I rolled over to the next day, and went to sleep somewhere in the region.

# To-Do

**Tasks which I recognize I need to do- I will forget to add things here, and I am sorry in advance.**

- I have a lot of random newlines in the markdowns. It's either that, or super long lines. Make that uniform.
- update all ``x = Class`` to ``x: Class`` (thanks @Ecconia for pointing this out)
- prettify the code and repository (later tasks, saving is priority)

# Bugs

**xxyy** where x is the version number and y is the bug number  
(.201 = version 0.2, bug 1)


- [ x ] .201: Resetting in any fashion destroys the textboxes (which is intended), but generates the textboxes on the main frame and never the tab frame.

# Log

**August 2 and 3, 2024**
- Reset ``log.md`` because I wrote it poorly

- Fix Bug .201
    - In great summary, the issue:
        - When ``reset_tab`` is called, it checks for the tab and calls ``add_tab`` if it does not exist.
        - When ``create_notepad_tab`` is called, it calls ``add_tab``. And then tries to store the return value.
        - If a notepad is requested for ``reset_tab``, it calls ``create_notepad_tab`` - oh wait a minute... *the tab was created... earlier in this function... so it gets None, and has no master*.
            - The fallback master is the root it can access, which is either the notebook or root. I don't know which, nor does it matter, because the end result is the same: Tab contents are deleted correctly but the frame is jammed onto the default master.
    - Solution:
        - Just run ``add_tab`` when calling ``reset_tab``, and store its output
        - Update ``add_tab`` to return the widget info if the tab does exist, instead of ``None``
            - Update the return type of ``add_tab`` to no longer inlcude ``None``, as it should never return ``None`` now
        - Update ``create_notepad_tab`` to have a new arg for a provided tab, defaulted to ``None``
            - If no tab is passed in, it still runs ``add_tab`` to get one.

- Update the return type for ``add_data_tab`` to not include ``None``
    - That was a remnant, and it should never return ``None``

- Remove unnecessary imports
    - ``from customtkinter import CTk`` in ``hints/control/hint_notebook.py``

- Correct comments

- Realize I have been foolish, and re-invented the wheel. Remove all of the ``data_tabs`` stuff.
    - I can just use ``.winfo_children()`` on the tabs to get the data about the tabs.
    - as for "Does it exist or not?"- ``try/except``
        - I was already doing this in ``hints/gui_management/managers/reset_utils.py`` at ``close_tab``...
        - Try to get the frame using ``.tab(tab_name)``
            - If it succeeds, return the frame info
            - If it fails, then do the creation stuffz. (we want the error.)

***Saving***

- It is in its own folder "saving" so I can brute force a prototype and fix it later.
    - It is within ``hints/utils`` because they are technically utils, if ``parse_log.py`` is something to refer to for that defintion.
    - (It will, in the future, be combined into a single class. THIS IS A PROTOTYPE.)
    - ``save.py`` is meant for everything to do with saving
    - ``reload.py`` is meant for getting the save data and reloading it.

- Create a function to more easily modify and add buttons in the future (also DRY the code) - ``create_buttons`` in ``hints/tabs/options_tab.py``
    - This could be in ``__init__`` but I put it here for easier modifications.

- ...
