
# Hosts the main window stuffs

from customtkinter import CTk, CTkTabview, CTkTextbox
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

        # Notes, Agitha's Castle, and Jovani's Redemption
        # (Default state for the latter)
        self.create_data_tabs()

        # Options Tab

        # Run the window
        root.mainloop()

    def create_data_tabs(self) -> None:
        '''Creates the tabs that have data in their default state.'''
        # The tabs that are to be created.
        # Easily expandable later.
        tab_list = [
            'Notes',
            "Agitha's Castle",
            "Jovani's Redemption"
        ]

        # Go through and create each tab with a blank notepad, then store.
        for tab_name in tab_list:
            # Add the tab
            new_tab = self.notebook.add(tab_name)

            # Create the notepad that goes in it
            notepad = CTkTextbox(corner_radius=0, master=new_tab)
            notepad.pack(padx=5, pady=5, expand=True, fill='both')

            # Store the tab and the notepad under the tab name
            self.data_tabs[tab_name] = [new_tab, notepad]

        print(self.data_tabs)
