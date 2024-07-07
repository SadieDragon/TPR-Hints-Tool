
# Home to the "basic" utility functions of the GUI components

from hints.data.Globals import return_default_bg
from tkinter import Frame
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import Notebook

def create_notebook_tab(master: Notebook, current_category: str) -> Frame:
    '''Create a frame, and turn it into a notebook tab.'''
    new_frame = new_frame = Frame(master,
                                  width = 450,
                                  height = 450,
                                  bg = return_default_bg())
    new_frame.pack(padx=5, expand=True, fill='both')
    master.add(new_frame, text=current_category)

    return new_frame


def create_scrollable(master: Frame, shopping=False) -> ScrolledText:
    '''Creates the scrollable textbox, by default one you can edit.'''
    default_bg = return_default_bg()
    new_textbox = ScrolledText(master,
                               bg = default_bg,
                               font = 37,
                               selectbackground = 'light gray',
                               selectforeground='black')
    if shopping:
        new_textbox.grid(row=1, column=0, padx=5, pady=5)
    else:
        new_textbox.pack(padx=5, pady=5, expand=True, fill='both')

    return new_textbox
