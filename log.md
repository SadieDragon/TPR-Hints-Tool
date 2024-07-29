
# This is a log file for the things that I have done.

It is written for my memory purposes when writing changelogs.  
It is provided for clarity when I ask for help.

Please note that I will reset this between releases, to keep it organized.

# To-Do

**Tasks which I recognize I need to do- I will forget to add things here, and I am sorry in advance.**

- I have a lot of random newlines in the markdowns.
It's either that, or super long lines.
Make that uniform.
    - When I do, make sure to go back through and update every python file reference to have the full path.
- Uncouple as much as I can from ``hints_notebook.py`` to reduce circular imports and dependencies.
    - Flesh out the constants system
- Break ``hints/gui_management/creation_utils.py`` into a folder
    - ``utils/gui_management/creation/widgets.py``
    - ``utils/gui_management/creation/window.py``
- Try ``__init__.py`` again.
- ``self.spoiler_tab``'s defintion line in ``spoiler_log.py`` is 81 characters long due to var names.
    - this might get patched by the removal of program

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
- Remove ``constants.py`` and convert everything over to ``tab_names.py``
    - Feel like I'm not going to be able to hold the global constants like I expected.
        - I might be able to convert the "instances" constants into such in ``hint_notebook.py`` once I uncouple everything and can globally import it and only it.
- Move the folder calls out to a constants file ``folders.py``
    - There is no reason this should really be stuck in the program file.
    - It is not very used right now, but when I get around to saving, it will hopefully be used a lot more.
- Start pulling functions out of the program to try to weasel out of the need for it, or at least start untangling things from its web.
    - Remember, ``reset_utils.py`` is acting like a wrapper for now,
    and ``creation_utils.py`` is a condensed version of the folder it will become,
    until I figure out how to set those up without the use of passing the utils around.
    - There was a minor formatting fix in ``hints/tabs/shopping/shopping.py`` where a ``.pack()`` call was not properly aligned
    - moved ``add_tab()`` to ``creation_utils.py``
    - Created ``window_management.py``
    - wrapped ``window_management.py`` in ``reset_utils.py`` for the same reasons as ``creation_utils.py``
        - I *will* uncouple it later.
    - start moving ``change_title()`` to ``window_management.py``
    - realize that ResetUtils is now a circular dependency child, and push this commit so I can unbreak things in the next
        - I rushed at the end to fix the last two calls. woops.
- Set up the ``gui_management`` folder, properly this time.
    - I wanted to use ``__init__.py`` to save some hassle,
    but it was a struggle to understand how to set it up.
        - I will address this later.
    - Please note that this commit is a broken code commit.
    - Create a wrapper function in ``hints_notebook.py`` to create the 3 instances
    - Prepare for the ensuing pain by analyzing the code and taking a very deep breath
        - (I wish I had more than 1 monitor for this)
    - Remove the wrapper functions from ``hints/utils/gui_management/reset_utils.py``
    - Fix the window creator not knowing where to call ``change_title()`` from
    - Update the instances in ``reset_utils.py`` to use the program ones.
    - Realize there's also a deletion function, and create ``deletion_utils.py``
        - and its instance. Yay. :/
        - move ``close_tab()`` from ``reset_utils.py`` to ``deletion_utils.py``
    - Update ``reset_utils.py`` to use the other managers' functions
        - ``add_tab`` in line 28 is from ``creator``
        - ``change_title`` in line 45 is from ``window_manager``
    - Update ``creation_utils.py`` to use the other managers' functions
        - ``change_title`` in line 48 is from ``window_manager``
    - move ``create_notepad()`` to ``creation_utils.py``
    - rename ``create_notepad()`` to ``create_notepad_tab()``
    - Update ``reset_utils.py``
        - line 36 uses the new function
    - Update ``hints_notebook.py`` to use the manager functions
        - ``create_window`` in line 28 is from ``creator``
        - ``add_tab`` in line 58 is from ``creator``
        - ``create_notepad`` in line 61 is now ``create_notepad_tab``, from ``creator``
    - Update ``shopping.py`` to use the manager functions
        - Import the deleter instance
        - ``close_tab`` in line 132 is from ``deleter``
    - Update ``options_tab.py`` to use the manager functions
        - Import the creator and deleter instance
        - ``show_warning`` in lines 55 and 73 are from ``creator``
        - ``close_tab`` in line 67 is from ``deleter``
    - Update ``spoiler_log.py`` - it needed more than the managers
        - in line 45, the spoiler log folder var is now a constant
        - Import the creator instance
        - ``show_warning`` in line 81 is from ``creator``
    - update ``parse_log.py`` to use the manager functions
        - Import the window manager instance
        - Remove the resetter instance
        - ``change_title`` in line 38 is from ``window_manager``
- ...
