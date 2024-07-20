If you see this, it ain't packaged yet. Sorry.

__Contact me if you find bugs:__
- I would like to keep issues for things I have posted myself, given I have a lot of irons in the fire and have made a mess of them. There's a discussion page for bug reports, though, and this would be the preferred location for them.
    - https://github.com/SadieDragon/TPR-Hints-Tool/discussions/categories/bug-reports
- Discord is the best not-GitHub way to get my attention more directly. There is a discord server for this project now.
    - https://discord.gg/5M8VQFBYZs

__To 'install' this program (Unix/Mac):__
- Install Python. (https://www.python.org/downloads/)
- Install customtkinter, and CTkMessagebox.
    - ``pip install customtkinter``
    - ``pip install CTkMessagebox``
- Download the release.
    - https://github.com/SadieDragon/TPR-Hints-Tool/releases
- Extract the zip somewhere somehow, there are multiple ways.

__To 'install' this program (Windows):__
- Install python. (https://www.python.org/downloads/)
- Install customtkinter, and CTkMessagebox.
    - ``pip install customtkinter``
    - ``pip install CTkMessagebox``
- Download the release.
    - https://github.com/SadieDragon/TPR-Hints-Tool/releases
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
- In terminal/command prompt, if you navigate to this folder, you can use
``py main.py`` to run the program. I will be writing a file in the near future
to make running it a bit more straightforward, and also to enable easier
desktop shortcuts.

__To-Do:__
In no particular order:
- Improvizations to the shopping list tabs
  - Improve handling for the varying hint strengths
    - If you use stronger hints, and get a bug, please join the discord and
    report it under the #bug-reports channel.
  - Combine jovani with the other minor shopping lists (Fishing Hole Bottle,
  COO, maybe etc?)
  - Improve the default pages for them to be a dropdown based checklist
  instead of a notepad
- Saving
- A key tool that helps you figure out what an unrequired key makes barren
- A tool to help you mark down where the big key is for a dungeon, if your hint signs include it, and any small keys that you get hints for.
- Package better for end users
  - Write a temporary file that allows you to more easily create a desktop
  shortcut and run this program.
  - Pre-package this into a .exe file - I have done testing, and there are some
  issues that arise with the user input

Next planned release as of writing: July 19 at the latest for release 0.2
