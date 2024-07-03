
# Home to the parent class of the shopping list tabs

from hints.gui.Globals import return_default_bg
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

        # Prepare the other widgets to be populated
        self.textbox = None
        self.frame = None
        self.label = None

        # Set the local vars which hold the label texts
        self.label_var = StringVar()
        self.default_text = ''
        self.good = ''
        self.bad = ''

        # Set the local list vars to be populated
        self.rewards = []     # The reward lists provided by the subclasses
        self.checkboxes = []  # The IntVars which are the states of the checks

    def populate_tab(self, jovani=False) -> None:
        '''Populate the tab with provided information.'''
        # Create the new label in the tab
        self.label = Label(self.notebook_tab,
                           bg = self.default_bg,
                           justify = 'left',
                           textvariable = self.label_var)
        self.label.pack(padx=5, pady=5, anchor='nw')

        # Set up the scrollbar
        # (a textbox because not all widgets can have ScrollBar)
        self.textbox = create_scrollable(self.notebook_tab)
        self.textbox.config(cursor='arrow', relief='flat', state='disabled')

        # Create the checklist frame itself
        self.frame = Frame(self.textbox,
                           bg = self.default_bg)

        # Store the frame in the scrollable textbox
        self.textbox.window_create('end', window=self.frame)

        # Rewards handling
        if self.rewards:
            # Create the checklist
            self.create_checklist(jovani)

    def create_checklist(self, jovani=False) -> None:
        '''Create the checklist of items provided.'''
        was_disabled = []  # Temp var storing the flags
        for reward in self.rewards:
            # Figure out if need to disable
            to_disable = False
            if jovani:
                # Unpack the list provided
                reward, to_disable = reward

            # Create the IntVar for the state
            checkbox_var = IntVar()

            # Create the checkbox itself
            checkbox = Checkbutton(self.frame,
                                   activebackground = self.default_bg,
                                   bg = self.default_bg,
                                   command = self.collect_item,
                                   text = reward,
                                   variable = checkbox_var)

            # If this is a bad Jovani item, disable it
            if to_disable:
                checkbox.config(state='disabled')
                checkbox_var.set(1)

            # Pack the checkbox
            checkbox.pack(anchor='w')

            # Store the IntVar representing the state
            self.checkboxes.append(checkbox_var)

            # Store whether we disabled the checklist
            was_disabled.append(to_disable)

        # If all of the checks were disabled, then bad
        self.default_text = self.bad
        # If any of the checks were not disabled, good text
        if not all(was_disabled):
            self.default_text = self.good

        # Update the label var
        self.label_var.set(self.default_text)

    def collect_item(self) -> None:
        '''Update the labels if all items are collected.'''
        # Go through and check the states of the checkboxes
        checked = []
        for int_var in self.checkboxes:
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
