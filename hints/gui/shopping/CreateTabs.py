
from hints.gui.shopping.Agitha import AgithaTab
from hints.gui.shopping.Jovani import JovaniTab
from tkinter.ttk import Notebook

def create_shopping_tabs(notebook: Notebook) -> list:
    '''A DRY method to create the subtabs.'''
    return [AgithaTab(notebook), JovaniTab(notebook)]
