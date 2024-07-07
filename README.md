If you see this, it ain't packaged yet. Sorry.

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
- Move your downloaded seed's spoiler log to the folder named SpoilerLog
    - Remove spoiler logs as you complete them.
- Open command prompt
    - click the search icon on your task bar and type in "command", it should pop up
    - Windows (10), copy the path from the FileExplorer window
        - You see that bar above ``Name``, ``Date Modified``, etc? Click, then ctrl+C
- Nav to the directory the folder is in
    - Windows, type in ``cd`` then press ctrl+v to paste the path.
- ``python3 hint tool.py`` - tab complete will be your friend

__How to use this program:__
- lazy dragon mode- I will update later.

__To-Do:__
In no particular order:
- Improvizations to the shopping list tabs
  - Improve handling for the varying hint strengths - if you use anything but strong, feel free to dm me any issues that arise!
  - Combine jovani with the other minor shopping lists (Fishing Hole Bottle, COO, maybe etc?)
  - Improve the default pages for them to be a dropdown based checklist instead of a notepad
- Fix the reset button (it is admittedly broken)
- Saving
- A key tool that helps you figure out what an unrequired key makes barren
- A tool to help you mark down where the big key is for a dungeon, if your hint signs include it, and any small keys that you get hints for.
- Dark mode!
- Pre-package this into a .exe file
    - I do not know how to do this, currently.

Next planned release as of writing: July 27 at the latest for release 0.2
Betas / alphas might pop up beforehand for major bugfixes and improvements that were meant to be in this release.
