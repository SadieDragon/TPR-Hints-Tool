# PEP8 Compliant note: These all throw E402.
# These, however, cannot be moved, as I *must* change
# the above first, to avoid spamming __pycache__.
# Or I could spam that across every file.

from hints.gui.MainTab import MainTab
from hints.gui.NotepadTab import NotepadTab
from hints.gui.Program import Program
from hints.gui.utils import create_notebook_tab
from tkinter import Tk
from tkinter.ttk import Notebook
from hints.gui.shopping.AgithaTab import AgithaTab
from hints.gui.shopping.JovaniTab import JovaniTab


class ProgramInstance(Program):
    root = None
    notebook = None

    main_tab = None
    notepad_tab = None
    agitha_tab = None
    jovani_tab = None

    def __init__(self) -> None:
        # Set up the window ---------------
        self.root = Tk()
        self.root.title('Please pick a seed.')
        self.root.geometry('500x500')
        self.root.config(bg='#2f3136')
        self.root.minsize(350, 350)
        # ---------------------------------

        # Set up the notebook ------------------------------------------------
        self.notebook = Notebook(self.root, width=495, height=475)
        self.notebook.pack(padx=5, pady=5, expand=True, fill='both', anchor='nw')
        # --------------------------------------------------------------------

        # Make the default tab ---------------------------------------
        main_page_frame = create_notebook_tab(self.notebook, "Main Page")
        # ------------------------------------------------------------

        # Make the default notebook page --
        self.notepad_tab = NotepadTab(self.notebook)
        # ---------------------------------

        # Make Agitha and Jovani --
        self.agitha_tab = AgithaTab(self.notebook)
        self.jovani_tab = JovaniTab(self.notebook)
        # -------------------------

        # Make the spoiler and reset buttons -------------------
        self.main_tab = MainTab(self, main_page_frame)
        # ------------------------------------------------------

        # Run the window
        self.root.mainloop()

    def reset(self, race_mode=False) -> None:
        '''A compiled method that does the resetting.'''
        # Completely empty out the tabs
        self.notepad_tab.reset()

        if race_mode:
            # For race mode
            if self.agitha_tab is not None:
                self.agitha_tab.destroy()
                self.agitha_tab = None
            if self.jovani_tab is not None:
                self.jovani_tab.destroy()
                self.jovani_tab = None
        else:
            # For normal mode:
            if self.agitha_tab is None:
                self.agitha_tab = AgithaTab(self.notebook)
            else:
                self.agitha_tab.reset()

            if self.jovani_tab is None:
                self.jovani_tab = JovaniTab(self.notebook)
            else:
                self.jovani_tab.reset()

    def set_agithas_spoiler_log(self, data):
        self.agitha_tab.set_spoiler_log(data)

    def set_jovani_spoiler_log(self, data):
        self.jovani_tab.set_spoiler_log(data)

    def has_unsaved_data(self) -> bool:
        return self.notepad_tab.has_unsaved_data() \
            or self.agitha_tab is not None and self.agitha_tab.has_unsaved_data() \
            or self.jovani_tab is not None and self.jovani_tab.has_unsaved_data()
