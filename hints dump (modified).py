

from tkinter import Tk
from tkinter.ttk import Notebook

from hints.gui.MainPage import create_pop_up_buttons
from hints.gui.Utils import create_notebook_tab
from hints.gui.shopping.Agitha import AgithaTab
from hints.gui.shopping.Jovani import JovaniTab

if __name__ == '__main__':
    # This will be updated and set later on
    seed_name = 'Please pick a seed.'

    # Set up the window -------
    root = Tk()
    root.title(seed_name)
    root.geometry('500x500')
    root.config(bg='#2f3136')
    # -------------------------

    # Set up the notebook ------------------------------------
    notebook = Notebook(root, width=495, height=475)
    notebook.pack(padx=5, pady=5, expand=False, anchor='nw')
    # --------------------------------------------------------

    # Make Agitha and Jovani -----
    agitha = AgithaTab(notebook)
    jovani = JovaniTab(notebook)
    # ----------------------------

    # Intro Page ------------------------------------------------------
    main_page_frame = create_notebook_tab(notebook, "Main Page")
    # -----------------------------------------------------------------

    # Make the spoiler and reset buttons -------------
    create_pop_up_buttons(notebook, main_page_frame)
    # ------------------------------------------------

    # And run the window plz.
    root.mainloop()
