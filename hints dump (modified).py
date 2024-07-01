

from tkinter import Tk
from tkinter.ttk import Notebook

from hints.Globals import return_logs_list
from hints.gui.Globals import return_default_bg
from hints.gui.MainPage import create_main_reset_button, main_page_button
from hints.gui.PickSpoiler import spoiler_pop_up
from hints.gui.Utils import create_notebook_tab
from hints.gui.shopping.Agitha import AgithaTab
from hints.gui.shopping.Jovani import JovaniTab

# Script Execution ============================================================

# There should always be a main guard for things that are
# not run locally by me, because things could be different.
if __name__ == '__main__':
    # This will be updated and set later on
    seed_name = 'Please pick a seed.'

    # Set up the window -------------
    root = Tk()
    root.title(seed_name)
    root.geometry('500x500')
    root.config(bg='#2f3136')
    # -------------------------------

    # Set up the notebook ------------------------------------
    notebook = Notebook(root, width=495, height=475)
    notebook.pack(padx=5, pady=5, expand=False, anchor='nw')
    # --------------------------------------------------------

    # Intro Page ------------------------------------------------------
    main_page_frame = create_notebook_tab(notebook, "Main Page")
    # -----------------------------------------------------------------

    # Pick a spoiler log ---------------------------------------------------
    # PEP8 compliance and readability
    command = lambda: spoiler_pop_up(return_logs_list(), notebook)
    # Create the button
    main_page_button(main_page_frame, 'Pick Spoiler Log', [0, 0], command)
    # ----------------------------------------------------------------------

    # Make Agitha and Jovani -----
    agitha = AgithaTab(notebook)
    jovani = JovaniTab(notebook)
    # ----------------------------

    # Reset Button ------------------------------------------------------
    create_main_reset_button(notebook, main_page_frame)
    # -------------------------------------------------------------------

    # And run the window plz.
    root.mainloop()
