
# The parent class for the shopping lists
from customtkinter import  CTkCheckBox, CTkLabel, CTkScrollableFrame, IntVar
from hints.control.program import Program


class Shopping:
    # The tab name
    tab_name = ''

    # The label that displays the status
    default_text = ''    # The default text for the label
    status_label = None  # The label itself

    # The rewards list
    rewards = []        # The rewards themselves
    checkboxes = []     # Holds the checkboxes
    checkbox_vars = []  # Holds the IntVars

    # The provided info
    program = None  # The program we're running in
    hint_text = ''  # The provided hint text

    def __init__(self, program: Program, hint_text: str) -> None:
        '''Initialize the variables provided.'''
        # Store the provided information
        self.program = program
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
        # Clean out the vars.
        # Jovani was getting Agitha's, for *some reason.*
        self.checkbox_vars = []
        self.checkboxes = []

        # Reset, but don't reset to default
        tab = self.program.reset_tab(self.tab_name, False)

        # Create the status label ----------------------------
        self.status_label = CTkLabel(master=tab,
                                     text=self.default_text)
        self.status_label.pack(anchor='w', padx=5, pady=5)
        # ----------------------------------------------------

        # Create the checklist frame ---------------------
        checklist_frame = CTkScrollableFrame(master=tab)
        checklist_frame.pack(anchor='w',
                             expand=True,
                             fill='both',
                             padx=5,
                             pady=5)
        # ------------------------------------------------

        # Go through the rewards
        for reward in self.rewards:
            # Remove the braces from the string
            reward = self.remove_braces(reward)

            # Create the IntVar for the collection status
            checkbox_variable = IntVar()

            # Create the checkbox for the reward
            checkbox = CTkCheckBox(command=self.collect_item,
                                   master=checklist_frame,
                                   text=reward,
                                   variable=checkbox_variable)
            checkbox.pack(anchor='w', pady=5)

            # Store the checkbox with its var
            self.checkboxes.append(checkbox)
            self.checkbox_vars.append(checkbox_variable)

    def no_rewards(self) -> None:
        '''The action for no rewards: Close the tab.'''
        self.program.close_tab(self.tab_name)

    def parse_rewards(self) -> None:
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
