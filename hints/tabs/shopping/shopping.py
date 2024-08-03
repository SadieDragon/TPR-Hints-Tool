
# The parent class for the shopping lists and their utilities

from customtkinter import (CTkCheckBox,
                           CTkFrame,
                           CTkLabel,
                           CTkScrollableFrame,
                           IntVar)

from hints.gui_management.managers import ResetUtils
from hints.gui_management.notebook_frame import NotebookFrame


class Shopping:
    '''The parent class for all of the shopping list tabs.'''
    # The instances
    resetter: ResetUtils           # The resetter instance (passed in)
    notebook_frame: NotebookFrame  # The notebook instance (passed in)

    # The provided hint text
    hint_text: str

    # The tab name
    tab_name: str

    # The label that displays the status
    default_text: str              # The default text for the label
    status_label:CTkLabel         # The label itself

    # The rewards list
    rewards = []                # The rewards themselves
    checkboxes = []             # Holds the checkboxes
    checkbox_vars = []          # Holds the IntVars

    def __init__(self,
                 hint_text:str,
                 notebook_frame: NotebookFrame,
                 resetter: ResetUtils) -> None:
        '''Initialize the variables provided.'''
        # Store the provided information
        self.resetter = resetter
        self.notebook_frame = notebook_frame
        self.hint_text = hint_text

    def auto_fill(self) -> None:
        '''Populate the tab with the provided info.'''
        # Varies based on tab.
        pass

    def collect_item(self) -> None:
        '''What happens when an item is checked off.'''
        # Go through and check the states of the checkboxes
        checked = []
        for int_var in self.checkbox_vars:
            checked.append(int_var.get())

        # Set the text to the default text, to be safe
        self.status_label.configure(text=self.default_text)

        # If all are true, update the text
        if all(checked):
            # PEP8 compliant and readable text
            new_text = ('Congratulations!'
                        ' There is nothing left to collect here.\n'
                        'You have collected the following items from here:')
            self.status_label.configure(text=new_text)

    def create_checklist(self) -> None:
        '''Create the checklist of the provided rewards.'''
        # Clean out the vars to prevent a bug where,
        # if there are multiple children classes,
        # they each got the same copy of the var.
        self.checkbox_vars = []
        self.checkboxes = []

        # Reset, but don't reset to default
        tab = self.resetter.reset_tab(self.tab_name, False)

        # Host frame ---------------------------------------------
        # Create the frame to pass to dict
        tab_frame = CTkFrame(master=tab)
        tab_frame.pack(anchor='w',
                       expand=True,
                       fill='both',
                       padx=5,
                       pady=5)

        # Pass it to the dict
        self.notebook_frame.data_tabs[self.tab_name] = tab_frame
        # --------------------------------------------------------

        # Create the status label ----------------------------
        self.status_label = CTkLabel(master=tab_frame,
                                     text=self.default_text)
        self.status_label.pack(anchor='w', padx=5, pady=5)
        # ----------------------------------------------------

        # Create the checklist frame ---------------------------
        checklist_frame = CTkScrollableFrame(master=tab_frame)
        checklist_frame.pack(anchor='w',
                             expand=True,
                             fill='both',
                             padx=5,
                             pady=5)
        # ------------------------------------------------------

        # Go through the rewards
        for reward in self.rewards:
            # Remove the braces from the string
            reward = self.remove_braces(reward)

            # Create the IntVar for the collection status
            checkbox_variable = IntVar()

            # Create the checkbox for the reward ---------------
            checkbox = CTkCheckBox(command=self.collect_item,
                                   master=checklist_frame,
                                   text=reward,
                                   variable=checkbox_variable)
            checkbox.pack(anchor='w', pady=5)
            # --------------------------------------------------

            # Store the checkbox with its var ------------
            self.checkboxes.append(checkbox)
            self.checkbox_vars.append(checkbox_variable)
            # --------------------------------------------

    def no_rewards(self) -> None:
        '''The action for no rewards: Close the tab.'''
        self.resetter.close_tab(self.tab_name)

    def parse_rewards(self) -> bool:
        '''Autofills with the provided information.'''
        # Parse the text
        self.parse_text()

        # Test if there are rewards
        are_rewards = bool(self.rewards)

        # If there are now no rewards, close the tab.
        if not are_rewards:
            self.no_rewards()

        # Return if there are rewards
        return are_rewards

    def parse_text(self) -> None:
        '''Grab the text off the sign, and parse into the list of rewards.'''
        # Varies by tab
        pass

    def remove_braces(self, text: str) -> str:
        '''Removes the {} from a given string.'''
        return text.replace('{', '').replace('}', '')
