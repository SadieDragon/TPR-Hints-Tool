
# Hosts the main window stuffs

from CTkMessagebox import CTkMessagebox
from customtkinter import CTk, CTkButton, CTkFrame, CTkTabview, CTkTextbox
from hints.control.program import Program


class HintNotebook(Program):
    '''The main window.'''
    # The root window
    root = None

    # The tabs that are to be created.
    # Easily expandable later.
    data_tab_names = [
        'Notes',
        "Agitha's Castle",
        "Jovani's Redemption"
    ]

    def __init__(self) -> None:
        '''Initialize the program window.'''
        # Create the main window --------
        self.root = CTk()
        self.root.geometry('500x500')
        self.root.minsize(250, 250)
        self.root.title('TPR Hint Notebook')
        # -------------------------------

        # Create the main notebook. -------------
        self.notebook = CTkTabview(master=self.root)
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

        # DEBUG - remove for updates
        # debug_tab = self.notebook.add('DEBUG')

        # debug_button = CTkButton(command=lambda: self.close_tab('Options'),
        #                          master=debug_tab,
        #                          text='DEBUG')
        # debug_button.pack(padx=5, pady=5)

        # Run the window
        self.root.mainloop()

    def add_tab(self, tab_name: str) -> None:
        '''Create a tab in the notebook.'''
        if not self.tab_exists(tab_name):
            self.notebook.add(tab_name)

    def close_tab(self, tab_name: str) -> None:
        '''Close a tab in the notebook.'''
        if self.tab_exists(tab_name):
            self.notebook.delete(tab_name)

    def create_data_tabs(self) -> None:
        '''Creates the tabs that have data in their default state.'''
        # Go through and create each tab with a blank notepad, then store.
        for tab_name in self.data_tab_names:
            # Add the tab
            self.add_tab(tab_name)

            # Create the notepad that goes in it
            notepad = self.create_notepad(tab_name)

            # Store the notepad under the tab name
            self.update_data_tabs(tab_name, notepad)

    def create_notepad(self, tab_name: str) -> CTkTextbox:
        '''Creates a notepad under the target tab.'''
        # Get the tab at the tab name
        tab = self.notebook.tab(tab_name)

        # Create the notepad
        notepad = CTkTextbox(corner_radius=0, master=tab)
        notepad.pack(padx=5, pady=5, expand=True, fill='both')

        # Return the notepad
        return notepad

    def reset_tracker(self) -> None:
        '''Completely reset the tracker.'''
        # Create a warning to ask them are ya sure?
        warning_box = CTkMessagebox(icon='warning',
                                    option_1='Cancel',
                                    option_2='Yes',
                                    master=self.root,
                                    message='This will reset everything.',
                                    title='Are you sure?')

        # Reset all of the tabs only if they explicitly click yes.
        if warning_box.get() == 'Yes':
            [self.reset_tab(tab_name) for tab_name in self.data_tab_names]

    def reset_tab(self, tab_name: str) -> None:
        '''Reset the contents of the tab.'''
        self.data_tabs[tab_name].destroy()

        self.update_data_tabs(tab_name, None)

    def tab_exists(self, tab_name: str) -> bool:
        '''A simple test for if the tab even exists.'''
        try:
            exists = True
        except ValueError:
            exists = False

        return exists

    def update_data_tabs(self,
                         tab_name: str,
                         tab_content: CTkTextbox | CTkFrame | None) -> None:
        '''Update the storage of data tab info'''
        self.data_tabs[tab_name] = tab_content
