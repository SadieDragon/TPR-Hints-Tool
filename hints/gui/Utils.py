
# Home to the "basic" utility functions of the GUI components

from hints.gui.Globals import return_default_bg
from tkinter import Frame
from tkinter.ttk import Notebook

def create_notebook_tab(master: Notebook, current_category: str) -> Frame:
    '''Create a frame, and turn it into a notebook tab.'''
    new_frame = new_frame = Frame(master,
                                  width = 450,
                                  height = 450,
                                  bg = return_default_bg())
    new_frame.pack(padx=5, expand=True)
    master.add(new_frame, text=current_category)

    return new_frame
