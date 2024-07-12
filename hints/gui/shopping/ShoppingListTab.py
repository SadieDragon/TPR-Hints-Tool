
# Home to the parent class of the shopping list tabs

from hints.data.globals import return_default_bg
from hints.data.utils import remove_braces
from hints.gui.utils import create_notebook_tab, create_scrollable
from tkinter import Checkbutton, Frame, IntVar, Label, StringVar, END
from tkinter.ttk import Notebook


class ShoppingListTab:
    '''The parent class for Agitha and Jovani's tabs.'''

    default_bg = return_default_bg()
    notebook = None
    name = None
    tab = None

    textbox = None

    frame = None
    label = None

    label_var = None
    default_text = ''
    text = ''

    rewards = []        # The reward lists provided by the subclasses
    checkboxes = []     # The actual checkboxes
    checkbox_vars = []  # The checkbox states

    was_changed = False

    def __init__(self, notebook: Notebook, name=''):
        '''Initialize all local vars, then create the tab.'''
        # Set the local constants that were provided
        self.notebook = notebook
        self.name = name

        # Create the tab for the subclass, if it does not exist
        self.tab = create_notebook_tab(self.notebook, self.name)

        self.label_var = StringVar()

        # Create the textbox
        self.textbox = create_scrollable(self.tab, True)

    def populate_tab(self) -> None:
        '''Populate the tab with provided information.'''
        # Create the new label in the tab
        self.label = Label(self.tab,
                           bg=self.default_bg,
                           justify='left',
                           textvariable=self.label_var)
        self.label.grid(row=0, column=0, padx=5, pady=5, sticky='nw')

        # And disable it, so the user can't mess it up
        self.textbox.config(cursor='arrow', relief='flat', state='disabled')

        # Create the checklist frame itself
        self.frame = Frame(self.textbox, bg=self.default_bg)

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
                                   activebackground=self.default_bg,
                                   bg=self.default_bg,
                                   command=self.collect_item,
                                   text=reward,
                                   variable=checkbox_var)
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
        self.was_changed = True
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

    def destroy(self) -> None:
        self.tab.destroy()

    def reset(self) -> None:
        [widget.destroy() for widget in self.tab.winfo_children()]
        # Reset whatever variables might have been changed:
        self.frame = None
        self.label = None
        self.label_var = StringVar()
        self.default_text = ''
        self.text = ''
        self.rewards = []        # The reward lists provided by the subclasses
        self.checkboxes = []     # The actual checkboxes
        self.checkbox_vars = []  # The checkbox states
        self.was_changed = False
        # Restore the text box:
        self.textbox = create_scrollable(self.tab, True)

    def has_unsaved_data(self) -> bool:
        if self.label is None:
            return bool(self.textbox.get(1.0, END).strip())
        else:
            return self.was_changed
