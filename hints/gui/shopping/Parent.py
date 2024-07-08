
# Home to the parent class of the shopping list tabs

from hints.data.Globals import return_default_bg
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
        self.good = ''
        self.bad = ''

        # Set the local list vars to be populated
        self.rewards = []     # The reward lists provided by the subclasses
        self.checkboxes = []  # The IntVars which are the states of the checks

    def populate_tab(self) -> None:
        '''Populate the tab with provided information.'''
        # Create the dropdown list in the tab
        self.dropdown_var = StringVar(self.notebook_tab)
        self.dropdown = OptionMenu(self.notebook_tab, self.dropdown_var, "")
        self.dropdown.config(bg=self.default_bg)
        self.dropdown.grid(row=0, column=0, padx=5, pady=5, sticky='nw')

        # Configure and disable the textbox
        self.textbox.config(cursor='arrow', relief='flat', state='disabled')

        # Create the checklist frame itself
        self.frame = Frame(self.textbox, bg=self.default_bg)

        # Store the frame in the scrollable textbox
        self.textbox.window_create('end', window=self.frame)

    def create_checklist(self, jovani=False) -> None:
        '''Create the checklist of items provided.'''
        # Populate the tab first
        self.populate_tab()

        # Define the items and constraints
        items = ["Fishing hole bottle", "COO", "Jovani", "Shadow Crystal", "Clawshot", "Spinner", "B&C", "DDR", "Double Claw", "First Sword"]
        constraints = {
            "Fishing hole bottle": ["coral earring"],
            "COO": ["Shadow Crystal", "Clawshot", "Spinner"],
            "Jovani": ["Shadow Crystal"],
            "COO Floor 33": ["B&C", "DDR"],
            "COO Floor 44": ["B&C", "DDR", "Double Claw"],
            "GF": ["Double Claw"]
        }

        # Filter items based on constraints
        filtered_items = []
        for item in items:
            if jovani and item in constraints.get("Jovani", []):
                continue
            if "COO" in item and any(disallowed in item for disallowed in constraints.get("COO", [])):
                continue
            if "COO Floor 33" in item and any(disallowed in item for disallowed in constraints.get("COO Floor 33", [])):
                continue
            if "COO Floor 44" in item and any(disallowed in item for disallowed in constraints.get("COO Floor 44", [])):
                continue
            if "GF" in item and any(disallowed in item for disallowed in constraints.get("GF", [])):
                continue
            filtered_items.append(item)

        # Populate the dropdown list with filtered items
        self.dropdown_var.set("Select an item")
        self.dropdown['menu'].delete(0, 'end')
        for item in filtered_items:
            self.dropdown['menu'].add_command(label=item, command=lambda value=item: self.dropdown_var.set(value))

        # Update the label
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
