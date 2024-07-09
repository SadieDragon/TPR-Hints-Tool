
# The main file.

import sys

# Don't write __pycache__
sys.dont_write_bytecode = True

from hints.gui.MainPage import create_pop_up_buttons
from hints.gui.Utils import create_notebook_tab, create_scrollable
from hints.gui.shopping.Agitha import AgithaTab
from hints.gui.shopping.Jovani import JovaniTab
from tkinter import Tk
from tkinter.ttk import Notebook

if __name__ == '__main__':
    # Set up the window -------
    root = Tk()
    root.title('Please pick a seed.')
    root.geometry('500x500')
    root.config(bg='#2f3136')
    root.minsize(350, 350)
    # -------------------------

    # Set up the notebook ------------------------------------------------
    notebook = Notebook(root, width=495, height=475)
    notebook.pack(padx=5, pady=5, expand=True, fill='both', anchor='nw')
    # --------------------------------------------------------------------

    # Intro Page -------------------------------------------------
    main_page_frame = create_notebook_tab(notebook, "Main Page")
    # ------------------------------------------------------------

    # Make the default notebook page ----------------------
    default_page = create_notebook_tab(notebook, 'Notes')

    default_textbox = create_scrollable(default_page)
    # -----------------------------------------------------

    # Make Agitha and Jovani -----
    AgithaTab(notebook)
    JovaniTab(notebook)
    # ----------------------------

    # Make the spoiler and reset buttons -------------------
    create_pop_up_buttons(notebook, main_page_frame, root)
    # ------------------------------------------------------

    # And run the window plz.
    root.mainloop()
