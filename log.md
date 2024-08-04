
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

**General Focus Patches**
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

- Move ``set_to_notes_tab()`` to ``hints/gui_management/managers/reset_utils.py``, as it is only ever used for resetting purposes.

- Remove now unnecessary local notebook instances
    - ``hints/tabs/shopping/shopping.py`` no longer needs the notebook
        - This means ``hints/tabs/shopping/agitha.py`` no longer needs the notebook

    - ``hints/utils/parse_log.py`` only needs it to update the title now
    - ``hints/tabs/spoiler_log.py`` only needs it for ``parse_log``

- Update ``hints/tabs/shopping/shopping.py`` to not have an extra subframe.
    - I do not think this is needed, though I may well be very wrong, we shall see.
    - It was here to make checking for the checklist easier, but I want to more loosely code instead of hardcoding myself into a box

***Saving***

- It is in its own folder "saving" so I can brute force a prototype and fix it later.
    - It is within ``hints/utils`` because they are technically utils, if ``parse_log.py`` is something to refer to for that defintion.
    - ``save.py`` is meant for everything to do with saving
    - ``reload.py`` is meant for getting the save data and reloading it.

- Create a function to more easily modify and add buttons in the future (also DRY the code) - ``create_buttons`` in ``hints/tabs/options_tab.py``
    - This could be in ``__init__`` but I put it here for easier modifications.

- Saving Prototyping:
    - As much as I thought the flexibility was smart, this is still using pretty hardcoded expectances. If I change things in the future, this prototype will still be too hard-coded to take advantage of the flexibility.
        - Because of how the ``CTkScrollableFrame`` is actually packed, I need to look for a frame within the widget. But what if I create a frame myself, to store a different widget list? Stuff like this will make future expandability difficult.
    - Loop through the data tab names (the constant in ``hints/utils/constants/tab_names.py``)
        - All of this could be done in one sweep under a try-except, but I wanna reduce nesting, and clean up the flow a lil bit.
            - I may also handle "None" returns differently in the future, so I want to have that flexibility available to me.

        - Have the try-except to look for ``tab_contents`` in a function for readability
            - As this is strucutured into a class, I can set the contents of the tab into a local variable, instead of needing to pass it in and out of different functions.
                - This is being done for more flexible coding: Instead of assuming that the widget we're looking for is precisely at x index and is precisely y widget, look for the widget type (which can later be changed) in the list of widgets, then call the handling for that widget type separately.
            - Try to get the tab.
                - If success, set tab contents to the children of the frame that is the tab
                - If failure, set the tab contents to none

        - If tab has nothing (it was closed, or otherwise does not exist), move along for now.

        - Look for a ``CTkTextbox`` widget within the contents
            - If one exists, store the contents of the textbox
                - Get the contents using ``.get('1.0', END).strip()``
        - Look for a ``CTkFrame`` widget within the contents (the shopping list)
            - So, that scrollable frame is packed as a ``canvas``, ``scrollbar``, and ``label`` object into a singular frame.

- ...
