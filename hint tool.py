
# The main file.

import sys

# Don't write __pycache__
sys.dont_write_bytecode = True

from hints.gui.main_page import create_default_notebook, create_pop_up_buttons
from hints.gui.Utils import create_notebook_tab
from hints.gui.shopping.agitha import AgithaTab
from hints.gui.shopping.jovani import JovaniTab
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
    create_default_notebook(notebook)
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
