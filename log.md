
# This is a log file for the things that I have done.

It is written for my memory purposes when writing changelogs. It is provided for clarity when I ask for help.

Please note that I will reset this between releases, to keep it organized.

If you see a blank line between bullets on any given day, it means that I rolled over to the next day, and went to sleep somewhere in the region.

# To-Do

**Tasks which I recognize I need to do- I will forget to add things here, and I am sorry in advance.**

- I have a lot of random newlines in the markdowns. It's either that, or super long lines. Make that uniform.
- prettify the code and repository (later tasks, saving is priority)

- Figure out how to implement an autosave upon resets, and inform the user of the autosave
- Proper errorhandling instead of ``raise NotImplementedError``


# Tasks to Complete for Release
It is finally time for a release. There are some things I need to get working first, and this is a subset of the to-do list which encompasses the targets for release.

- Update text wrapping in the textboxes to be word based
- Improve some code in ``create_save_dir.py`` (maybe even rename it)
    - Rename the user file / master save file to be ``master`` instead of ``time``, so the user knows what to look for
    - Update the ``state`` variable name for the checklist processing to instead be something more accurately referring to ``collection status``
- Reloading save data
- Figure out if ``add_data_tab`` necessary anymore


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
        - Update ``create_notepad_tab`` to have a new arg for a provided tab, defaulted to ``None``
            - If no tab is passed in, it still runs ``add_tab`` to get one.

- Remove all of the ``data_tabs`` stuff.
    - I can just use ``.winfo_children()`` on the tabs to get the data about the tabs.
    - For creating the tab: Try to get the frame using ``.tab(tab_name)``
        - If it succeeds, return the frame info
        - If it fails, then do the creation stuffz. (we want the error.)

- Move ``set_to_notes_tab()`` to ``hints/gui_management/managers/reset_utils.py``, as it is only ever used for resetting purposes.

- Update ``hints/tabs/shopping/shopping.py`` to not have an extra subframe.

***Saving***

- It is in its own folder "saving" so I can brute force a prototype and fix it later.
    - It is within ``hints/utils`` because they are technically utils, if ``parse_log.py`` is something to refer to for that defintion.
    - ``save.py`` is meant for everything to do with saving
    - ``reload.py`` is meant for getting the save data and reloading it.

- Create a function to more easily modify and add buttons in the future (also DRY the code) - ``create_buttons`` in ``hints/tabs/options_tab.py``

- Saving Prototyping (``save.py``):
    - As much as I thought the flexibility was smart, this is still using pretty hardcoded expectances. If I change things in the future, this prototype will still be too hard-coded to take advantage of the flexibility.
        - Because of how the ``CTkScrollableFrame`` is actually packed, I need to look for a frame within the widget. But what if I create a frame myself, to store a different widget list? Stuff like this will make future expandability difficult.
    - Gathering the data from the tabs (``gather_tab_data.py``)
        - I wrote a wrapper function for ``.winfo_children()`` because... it's not very clear what exactly that's doing....
            - I also wrote a wrapper function to return the first widget of that list.
            - Type defintions for these are a bit weird
        - All of this could be done in one sweep under a try-except, but I wanna reduce nesting, and clean up the flow a lil bit.
            - I may also handle "None" returns differently in the future, so I want to have that flexibility available to me.
        - Loop through the data tab names (the constant in ``hints/utils/constants/tab_names.py``)
            - Have the try-except to look for ``tab_widgets``
                - As this is strucutured into a class, I can set the contents of the tab into a local placeholder variable (``tab_widgets``), instead of needing to pass it in and out of different functions.
                    - This is being done for more flexible coding: Instead of assuming that the widget we're looking for is precisely at ``x`` index and is precisely ``y`` widget, look for the widget type (which can later be changed) in the list of widgets, so I can call the handling for that widget type separately.
                - Try to get the tab.
                    - If success, set ``tab_widgets`` to the children of the frame that is the tab
                    - If failure, the tab was closed, so move to the next tab.

            - The ``contains_widget`` function also saves the target widget when found, to reduce repeated searching.
                - In the future, it would not be that difficult to switch this to an indices storage, to cherry pick which specific widget is to be the target.

            - Notepad Handling
                - Look for a ``CTkTextbox`` widget within the contents
                - If one exists, store the contents of the textbox

            - Shopping List Handling
                - Look for a ``CTkFrame`` widget within the contents
                    - This has some major futureproofing issues, as mentioned above. But this is how the checklist frame is handled by ``customtkinter``.
                - If one exists, handle the checklist frame
                    - Checkbox Architecture notes
                        - The scrollable frame is packed into a frame as a ``canvas``, ``scrollbar``, and ``label``.
                        - within the ``canvas``, is the ``scrollableframe``
                        - Within the ``scrollableframe`` is the checklist.
                    - Checkbox parsing
                        - Use ``get_checklist`` to grab the checklist more clearly and also have the typing be correct
                        - Use ``.get()`` to get the state of the ``IntVar`` (the collection status)
                        - Use ``.cget('text')`` to get the text that was assigned to the checkbox, which was the item
                        - Future proofing note: For the minor lists which disable useless checkboxes, ``.cget('state')`` will tell whether the checkbox is enabled or not
                        - Store the item and the state in a tuple like list, ``['item', state]``
    - Saving the Data
        - For now, I am using a folder in the root directory to hold all of the saves. I will patch in "pick your own" later.
        - The default name of the zip folder will be a time stamp, but file name friendly.
            - ``mm-dd-yy (hh-mm)`` - ``month-day-year (hour-minute)``
            - uses 24hr clock; could use AM/PM but eh
        - Only 5 files will be saved, before old ones are deleted.

        - Formatting notes:
            - In a zip file to organize each save file
            - Contains the different tabs as different formats for the reloading to read easier, but also a master file for the user to read all of their notes at once.
                - Master Save File: the user can use this to read all of their notes at once, instead of having to parse the separate files.
                    - Pads the tab name with '=' to a length of 80 characters, to make it easier to find where each section is
                    - The formatting for each section is the same as in the individual tabs, as listed below.
                - Tab files: named after the tab itself, and the tab type is stored at the top of the file
                    - The notepad is literally just "dump notes in file verbatim"
                    - The checklist format: ``'item name': bool``, with the integer translated into a boolean
                        - would use yaml, but not built in, and honestly not worth at this time.
                        - Could use JSON- but again, not worth.
        - Further notes
            - There's an edge case, where if you create 2 saves within the same moment, the oldest save is overwritten. Oops.
            - jaq suggested using ``.anything-but-zip`` but i want the end user to be able to access the contents.

- ...
