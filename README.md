If you see this, I did not finish my lofty goals by July 6, 2024, and released a basic program. Therefore, it ain't packaged yet. Sorry.

(Or I made the repo public prior and thus have this on main so no one comes by and is confused.)

__Contact me if you find bugs:__
- I would like to keep issues for things I have posted myself, given I have a lot of irons in the fire and have made a mess of them. There's a discussion page for bug reports, though, and this would be the preferred location for them.
    - https://github.com/SadieDragon/TPR-Hints-Tool/discussions/categories/bug-reports
- If you do not have a GitHub account, and would like to report a bug, the next best option is Google Forms.
    - https://forms.gle/mzShNU1twirNS79P9
- Discord is the best not-GitHub way to get my attention more directly. ``sadie_dragon`` is my tag, or I can very easily be found in the TPR discord under the username ``DraconusLupa``.

__To 'install' this program (Unix/Mac):__
- Install Python. (https://www.python.org/downloads/)
- It is very likely that you did not get tkinter with your install. If you run the program, and get an error, then assume first that you did not get tkinter.
    - run ``pip3 install --upgrade pip`` because pip wants upgrades first
    - run ``pip3 install tk`` to install tkinter
- Use curl (``curl https://github.com/SadieDragon/TPR-Hints-Tool.git``)
- Extract the zip somewhere somehow, there are multiple ways.

__To 'install' this program (Windows):__
- Install python. (https://www.python.org/downloads/)
- Click on the ``<> Code`` button, and you'll see a dropdown. Click on the ``download zip`` option.
- Extract your zip somewhere.
    - Do not close File Explorer, it will help in the ``how to run``

__To run this program:__
- Windows (10), copy the path from the FileExplorer window
    - You see that bar above ``Name``, ``Date Modified``, etc? Click, then ctrl+C
    - open command prompt
        - click the search icon on your task bar and type in "command", it should pop up
- Nav to the directory the folder is in
    - Windows, type in ``cd`` then press ctrl+v to paste the path.
- ``python3 hintstool.py`` - tab complete will be your friend

__How to use this program:__
- This version is a glorified notepad. I have no real tips for how to use this.
- If you want tips, there's an extra tab for Agitha, because of the fact that she has a checklist of sorts, so you can keep her checklist separate and easier to read in your notes.
- Also, **DO NOT** click load, if you already have text in the boxes! Unless you want the scattered notes from previous saves to clutter!
- Save will save your notes, but I did not set a default output. Again, basic, not fighting with the cross-platform, just getting it out there.

__To-Do:__
- Agitha (and the other shopping lists) designed as a checkbox system
- A key tool that helps you figure out what an unrequired key makes barren
- A tool to help you mark down where the big key is for a dungeon, if your hint signs include it, and any small keys that you get hints for.
- Autofill based on the spoiler logs for the different shopping tabs that are not notepads
    - I would like some help understanding the different hint strengths, this expects balanced or strong hints
- Dark mode!
- Reset the tracker so you don't need to relaunch it every time you reset a seed for whatever reason
- Pre-package this into a .exe file
    - I do not know how to do this, currently.

If you want to play with those changes, a good majority of them are already implemented in the ``hint-tool-(not-mvc)`` branch, so you can follow the instructions to get that running.

Be warned: That is a live dev branch, and things may or may not be fully functional- if I have pushed changes to update or add issues, it's often with not currently working code.
