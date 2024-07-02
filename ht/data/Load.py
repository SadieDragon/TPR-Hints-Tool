
# Loads the data

from re import findall
from tkinter import INSERT
from tkinter.filedialog import askopenfilename

def load(tab_notepad: dict) -> None:
    '''Loads previous information.'''
    # Ask them to pick the file to open
    path = askopenfilename()

    if path:
        with open(path, 'r') as f:
            for notepad in tab_notepad.values():
                # Grab the current line
                line = f.readline()

                # Remove the tab itself
                line = findall('^(.*?): (.*)', line)[0][1]

                # And then shove that into the notepad
                notepad.insert(INSERT, line)
