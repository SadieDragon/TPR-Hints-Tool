
from hints.gui.Globals import return_default_bg
from hints.gui.Utils import create_notebook_tab
from tkinter import Checkbutton, Label, IntVar, StringVar
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import Notebook

class ShoppingListTab():
    '''The parent class for Agitha and Jovani's tabs.'''
    def __init__(self, notebook: Notebook, name: str) -> None:
        '''Initialize all local vars, then create the tab.'''
        # Set the local constants of notebook and name
        self.notebook = notebook
        self.name = name

        # The default background color
        self.default_bg = return_default_bg()

        # Create the dict to be populated (the IntVar states)
        self.checkboxes = []

        # The notebook frame
        self.notebook_tab = None

        # And prepare the Frame and Label to be populated
        self.frame = None
        self.label = None
        self.label_var = StringVar()

        # Also the textbox for the checkbox to go into
        self.textbox = None

        # Specifically holds the default txts
        self.default_text = ''
        self.good = ''
        self.bad = ''

        # And holds the rewards
        self.rewards = []

        # Create the tab
        self.create_tab()

    def populate_tab(self) -> None:
        '''Populate the tab with provided information.'''
        # Create the new label in that tab, with the var
        self.label = Label(self.notebook_tab,
                           bg = self.default_bg,
                           textvariable = self.label_var,
                           justify = 'left')
        self.label.pack(padx=5, pady=5, anchor='nw')

        # Set up the textbox for scrollableness
        self.textbox = ScrolledText(self.notebook_tab,
                                    bg = self.default_bg,
                                    relief = 'flat',
                                    selectbackground = self.default_bg,
                                    cursor = 'arrow')
        self.textbox.pack()

        # Set the default to bad
        self.default_text = self.bad
        # Update if good
        if self.rewards:
            self.create_checklist()

            self.default_text = self.good

        # And update the label_var
        self.label_var.set(self.default_text)

    def create_tab(self) -> None:
        '''Sets the local notebook tab.'''
        # Create the notebook tab
        self.notebook_tab = create_notebook_tab(self.notebook, self.name)

    def create_checklist(self, bad=False) -> None:
        '''Create the checklist of items provided.'''
        # Go through the item list
        for reward in self.rewards:
            # Create the IntVar for the state
            checkbox_var = IntVar()

            # Create the checkbox itself
            checkbox = Checkbutton(self.textbox,
                                   text = reward,
                                   variable = checkbox_var,
                                   bg = self.default_bg,
                                   activebackground = self.default_bg,
                                   command = self.collect_item)

            # If this is a bad jovani item, disable it
            if bad:
                checkbox.config(state='disabled')
                checkbox_var.set(1)

            # Store it
            self.textbox.window_create('end', window=checkbox)
            self.textbox.insert('end', '\n')

            # And store the reward and new intvar
            self.checkboxes.append(checkbox_var)

    def collect_item(self) -> None:
        '''Update the labels if all items are collected.'''
        # Go through and check the states of the checkboxes
        checked = []
        for int_var in self.checkboxes:
            checked.append(int_var.get())

        # If all are true, update the text
        if all(checked):
            # (which is so long I create a new var)
            new_text = ('Congratulations!'
                        ' There is nothing left to collect here.\n'
                        'You have collected the following items from'
                        f' {self.name}:')
            self.label_var.set(new_text)
        # Set it to the default text, to be safe
        else:
            self.label_var.set(self.default_text)