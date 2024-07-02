
# All of the functions to rip the data, and save

from tkinter import END
from tkinter.filedialog import asksaveasfile

def save(tab_notepad: dict) -> None:
    '''Write the save file.'''
    # Ask them to pick the file to save to
    path = asksaveasfile()

    if path is not None:
        path = path.name

        # Write the file
        with open(path, 'w+') as f:
            for tab, notepad in tab_notepad.items():
                # Grab the info out of the notepad
                text = notepad.get('1.0', END)

                # Write the log
                f.write(f'{tab}: {text}')