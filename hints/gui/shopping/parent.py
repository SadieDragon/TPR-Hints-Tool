
# Home to the parent class of the shopping list tabs

from hints.data.globals import return_default_bg
from hints.data.utils import remove_braces
from hints.gui.Utils import create_notebook_tab, create_scrollable
from tkinter import Checkbutton, Frame, IntVar, Label, StringVar
from tkinter.ttk import Notebook

class ShoppingListTab():
    '''The parent class for Agitha and Jovani's tabs.'''
    def __init__(self, notebook: Notebook, name: str) -> None:
        '''Initialize all local vars, then create the tab.'''
        # Set the default background color
        self.default_bg = return_default_bg()

        # Set the local constants that were provided
        self.notebook = notebook
        self.name = name

        # Create the tab for the subclass
        self.notebook_tab = create_notebook_tab(self.notebook, self.name)

        # Create the textbox
        self.textbox = create_scrollable(self.notebook_tab, True)

        # Prepare the other widgets to be populated
        self.frame = None
        self.label = None

        # Set the local vars which hold the label texts
        self.label_var = StringVar()
        self.default_text = ''
        self.text = ''

        # Set the local list vars to be populated
        self.rewards = []        # The reward lists provided by the subclasses
        self.checkboxes = []     # The actual checkboxes
        self.checkbox_vars = []  # The checkbox states

    def populate_tab(self) -> None:
        '''Populate the tab with provided information.'''
        # Create the new label in the tab
        self.label = Label(self.notebook_tab,
                           bg = self.default_bg,
                           justify = 'left',
                           textvariable = self.label_var)
        self.label.grid(row=0, column=0, padx=5, pady=5, sticky='nw')

        # And disable it, so the user can't mess it up
        self.textbox.config(cursor='arrow', relief='flat', state='disabled')

        # Create the checklist frame itself
        self.frame = Frame(self.textbox,
                           bg = self.default_bg)

        # Store the frame in the scrollable textbox
        self.textbox.window_create('end', window=self.frame)

    def create_checklist(self) -> None:
        '''Create the checklist of items provided.'''
        # Populate the tab first
        self.populate_tab()

        for reward in self.rewards:
            # Clean up the reward string
            reward = remove_braces(reward)

            # Create the IntVar for the state
            checkbox_var = IntVar()

            # Create the checkbox itself
            checkbox = Checkbutton(self.frame,
                                   activebackground = self.default_bg,
                                   bg = self.default_bg,
                                   command = self.collect_item,
                                   text = reward,
                                   variable = checkbox_var)
            checkbox.pack(anchor='w')

            # Store the checkbox for later config
            self.checkboxes.append(checkbox)

            # Store the IntVar representing the state
            self.checkbox_vars.append(checkbox_var)

    def set_default_label_text(self) -> None:
        '''Set the default text and the label text.'''
        self.default_text = self.text
        self.label_var.set(self.text)

    def collect_item(self) -> None:
        '''Update the labels if all items are collected.'''
        # Go through and check the states of the checkboxes
        checked = []
        for int_var in self.checkbox_vars:
            checked.append(int_var.get())

        # If all are true, update the text
        if all(checked):
            # PEP8 compliant and readable text
            new_text = ('Congratulations!'
                        ' There is nothing left to collect here.\n'
                        'You have collected the following items from'
                        f' {self.name}:')
            self.label_var.set(new_text)
        # Set it to the default text (safety measure)
        else:
            self.label_var.set(self.default_text)
