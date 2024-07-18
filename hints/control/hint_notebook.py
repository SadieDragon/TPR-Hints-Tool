
# Hosts the main window stuffs

from customtkinter import CTk, CTkTabview
from hints.control.program import Program


class HintNotebook(Program):
    '''The main window.'''
    def __init__(self) -> None:
        '''Initialize the program window.'''
        # Create the main window --------
        root = CTk()
        root.geometry('500x500')
        root.minsize(250, 250)
        root.title('TPR Hint Notebook')
        # -------------------------------

        # Create the main notebook. -------------
        self.notebook = CTkTabview(master=root)
        self.notebook.pack(anchor='nw',
                           expand=True,
                           fill='both',
                           padx=5,
                           pady=5)
        # ---------------------------------------

        # Run the window
        root.mainloop()
