
# The main file.

import sys

# Don't write __pycache__
sys.dont_write_bytecode = True

from hints.gui.MainPage import create_pop_up_buttons
from hints.gui.Utils import create_notebook_tab
from hints.gui.shopping.CreateTabs import create_shopping_tabs
from tkinter import Tk
from tkinter.ttk import Notebook

if __name__ == '__main__':
    # Set up the window -------
    root = Tk()
    root.title('Please pick a seed.')
    root.geometry('500x500')
    root.config(bg='#2f3136')
    # -------------------------

    # Set up the notebook ------------------------------------------------
    notebook = Notebook(root, width=495, height=475)
    notebook.pack(padx=5, pady=5, expand=True, fill='both', anchor='nw')
    # --------------------------------------------------------------------

    # Intro Page -------------------------------------------------
    main_page_frame = create_notebook_tab(notebook, "Main Page")
    # ------------------------------------------------------------

    # Make Agitha and Jovani -----
    create_shopping_tabs(notebook)
    # ----------------------------

    # Make the spoiler and reset buttons -------------------
    create_pop_up_buttons(notebook, main_page_frame, root)
    # ------------------------------------------------------

    # And run the window plz.
    root.mainloop()
