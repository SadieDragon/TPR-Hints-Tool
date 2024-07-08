
from TestCommand import read_tab

from tkinter import Button, Frame, StringVar, Text, Tk
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import Notebook

def create_tab(master: Tk) -> None:
    '''Create a test notebook tab.'''
    notebook = Notebook(master, width=500, height=500)
    notebook.pack(padx=5, pady=5, expand=True, fill='both', anchor='nw')

    test_tab = Frame(notebook)
    test_tab.pack(padx=5, expand=True, fill='both')
    notebook.add(test_tab, text='Test')

    # test_tab.

    command = lambda: read_tab(master)
    test_button = Button(test_tab, text='Read Tab', command=command)
    test_button.pack(padx=5, pady=5)

    textbox_host = ScrolledText(test_tab)
    textbox_host.pack(padx=5, pady=5)
