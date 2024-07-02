
# All of the functionality to create the basic notepad

from tkinter import Frame
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import Notebook

DEFAULT_BG = '#f9f9f9'

def create_notebook_tab(notebook: Notebook, title: str) -> Frame:
    '''Adds a new notebook tab'''
    new_frame = Frame(notebook, width=450, height=450, bg=DEFAULT_BG)
    new_frame.pack(padx=5, expand=True, fill='both')
    notebook.add(new_frame, text=title)

    return new_frame


def create_textbox(notebook_tab: Frame) -> ScrolledText:
    '''More readable "creating the textbox"'''
    textbox = ScrolledText(notebook_tab,
                           bg = DEFAULT_BG,
                           selectbackground = DEFAULT_BG)
    textbox.pack(padx=5, pady=5, expand=True, fill='both')

    return textbox