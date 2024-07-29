
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
- Try ``__init__.py`` again.
- ``self.spoiler_tab``'s defintion line in ``spoiler_log.py`` is 81 characters long due to var names.
    - this might get patched by the removal of program
- Give ``title.py`` a better name (I was struggling)
- update all ``x = Class`` to ``x: Class`` (thanks @Ecconia for pointing this out)

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
- Arguably, ``set_to_notes_tab()`` is window management.
    - Move ``set_to_notes_tab()`` to ``window_management.py``
    - Update ``options_tab.py``
        - Import the window manager instance
        - ``set_to_notes_tab`` in line 72 is from ``window_manager``
    - Update ``spoiler_log.py``
        - Import the window manager instance
        - ``set_to_notes_tab`` in line 163 is from ``window_manager``
    - Update ``reset_utils.py``
        - ``set_to_notes_tab`` in line 53 is from ``window_manager``
- The function ``update_data_tabs`` doesn't really need to be a function.
    - It is simply updating ``data_tabs``, the dict that holds the data tabs and their contents.
    - "Replace the function call" will mean turning ``udpate_data_tabs(tab_name, [content])`` to ``data_tabs[tab_name] = content``
    - Replace the function call in line 91 of ``shopping.py``
    - Realize that it was used both times ``create_notepad_tab`` was called, and moved the call into that function
    - Replace the function call in lines 29 and 48 of ``creation_utils.py``
    - Remove the function call from ``reset_utils.py``
    - Remove the function call from ``hint_notebook.py``
- Time to try the ``__init__.py`` again. See if I can uncouple the managers from the hint notebook and avoid circles...
    - After this I will finally test the code to make sure nothing is broken
    - I was gonna create the init file...
    - I then realized that ``create_data_tabs()`` in ``hint_notebook.py`` is practically only using creator functions and moved it there...
    - Then realize that ``create_window()`` could go into its own file, ``utils/gui_management/creation/window.py``, and that would be the only function within- and it could return root instead of updating it- meaning no more circle dependency-
        - Actually it got named to ``window/create.py`` so i can mess with the window more in the future.
    - Rename the new file to ``window_manager.py``; moved to the base folder.
    - Renamed ``window_management.py`` to ``notebook_manager.py``
        - Updated every call
    - moved ``change_title()`` to ``window_manager.py``
        - Realized a funny mistake, where the title set was not in the correct scope, and fixed that.
        - Updated every call
    - Realize then that ``change_title()`` is basically doing the same thing, 2 times, and then 1 time, doing something special.
    - create a new util file, ``title.py``, with that function without setting the title
    - Delete the function ``change_title()`` and update all calls to it
    - Ok, I should push now. That's already a big change.
- Actually remove ``change_title()``
- I forgot to update the window_manager vars, so this is a quick formatting push
- "Ok, so what do the managers actually need from ``hint_notebook.py``, that would cause a circular dependency?"
    - ``CreationUtils``
        - Wait, ``NotebookManager`` is no longer used. *rips it out*
        - needs ``data_tabs`` for ``add_tab()`` and ``create_notepad_tab()``
        - needs the notebook for ``create_notepad_tab()``
            - Wait. I added a tab here. USE THE FUNCTION.
            - Mmh, that means I don't need that call in ``create_data_tabs()``...
        - needs the root window for ``show_warning()``.
            - Does that *actually* belong in ``ResetUtils``? I mean, it creates a pop-up, but... it returns whether or not permission was granted to reset.. Hm.
    - ``DeletionUtils``
        - Needs the notebook to delete tabs, and ``data_tabs`` to remove the tab, in ``close_tab()``
    - ``NotebookManager``
        - It needs the notebook for changing to the notes tab in ``set_to_notes_tab()``
        - Could this be where I create the notebook itself? prolly, then it would need the root window as well
        - This is also where ``data_tabs`` could go...
    - ``ResetUtils``
        - Needs ``data_tabs`` for ``reset_tab()``, and the notebook to return the tab
        - Needs root to update the title for ``reset_tracker()``
- Begin by making ``NotebookManager`` no longer rely on ``program.py`` (baby steps towards making it a sort of parent class for the utils)
    - Not the order of operations I should be doing this (you'll see why next push), but I had the changes stashed (you'll see why)
    - update the outdated doctstring (a byproduct of copy pasta from earlier)
    - move ``data_tabs`` to ``notebook_manager.py``
    - create the notebook within ``notebook_manager.py``'s ``__init__``
    - update ``hint_notebook.py``
        - Create the notebook manager instance during ``__init__``
        - Remove it from ``create_instances()``
- Move ``gui_management`` into the root folder (told you you'd see why)
    - Do the bulk move
    - Move the utils into ``hints/gui_management/managers``
- Rename ``NotebookManager`` to ``NotebookFrame`` because it fits a bit better into its new role
- Address the utility managers to try to figure out how to incorporate them with the new ``NotebookFrame`` changes: ``CreationUtils``
    - I know that the rest of the app is broken right now, and I will get to it,
    after I get the children settled.
    - moved ``show_warning()`` to ``ResetUtils``, because it fits better there
        - There was a lot of internal debate over this but yeah.
        It's meant for resetting, and only used by resetting.
        - update ``options_tab.py``
            - lines 56 and 74
            - remove the creator manager, no longer used
        - update ``spoiler_log.py``
            - line 81
            - remove the creator manager, no longer used
    - Make a local var for the notebook frame
        - Remove the call to ``program.py`` *WOO*
        - Update ``__init__`` accordingly
        - update ``add_tab`` and ``create_notepad_tab`` to use the new var
    - Update ``hint_notebook.py``
        - Make a var for it in the top of the class before ``__init__``
        - Move its creation up into ``__init__``
        - Update its initialization
- ...
