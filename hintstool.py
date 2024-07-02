
# Don't write the __pycache__ plz
import sys

sys.dont_write_bytecode = True

# Actual start
from ht.gui.Notepad import create_notebook_tab, create_textbox
from ht.data.Load import load
from ht.data.Save import save

from tkinter import Button, Label, Tk
from tkinter.ttk import Notebook

# Root window, basic settings
root = Tk()
root.geometry('500x500')
root.minsize(425, 425)

# The notebook parent
notebook = Notebook(root, width=495, height=475)
notebook.pack(padx=5, pady=5, expand=True, fill='both', anchor='nw')

# The main page to add buttons to
main_page = create_notebook_tab(notebook, 'Main Page')

# The 3 tabs
tabs = ['Notes', "Agitha's Castle"]
# Where we'll store the vars
tab_notepad = {}
for tab in tabs:
    # Create the tab
    new_tab = create_notebook_tab(notebook, tab)

    # Create the notepad
    new_notepad = create_textbox(new_tab)

    # Store the tab with its notepad
    tab_notepad[tab] = new_notepad

# A warning label
text = ('Warning: Do not click LOAD when you have notes already. This'
        ' is not a foolproof rigid program, just a "get it done" if I'
        ' failed to meet the deadline.')
warning_label = Label(main_page, text=text, wraplength=400)
warning_label.grid(row=0, column=1, padx=5, pady=5)

# The save button
save_button = Button(main_page, text='Save', command=lambda: save(tab_notepad))
save_button.grid(row=1, column=0, padx=5, pady=5)

# The load button
load_button = Button(main_page, text='Load', command=lambda: load(tab_notepad))
load_button.grid(row=2, column=0, padx=5, pady=5)

root.mainloop()