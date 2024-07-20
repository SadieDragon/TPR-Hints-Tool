
# All of agitha's special handling goes here.
from customtkinter import  CTkCheckBox, CTkFrame, CTkLabel, IntVar
from hints.control.program import Program


class AgithaTab:
    '''Agitha's special checklist handling.'''
    # The tab name for agitha
    tab_name = 'Bugs'

    # Default label text
    default_text = 'Agitha gives you GREAT HAPPINESS:\n'

    # The label for the status
    status_label = None

    # The program provided
    program = None

    # Hint text provided
    hint_text = ''

    # The list that will hold the rewards
    rewards = []

    # The checkboxes and their vars
    checkboxes = []
    checkbox_vars = []

    def __init__(self, program: Program, hint_text: str) -> None:
        '''Initialize the checklist.'''
        # Store the program
        self.program = program

        # Store the hint text
        self.hint_text = hint_text

        # Check if there's any hints.
        # If there are, then we'll move forward.
        if ':' in self.hint_text:
            self.auto_fill()
        # Otherwise, just close the tab.
        else:
            self.no_rewards()

    def auto_fill(self) -> None:
        '''Autofills with the provided information.'''
        # Parse the text
        self.parse_rewards()

        # If there are now no rewards, close the tab.
        if not self.rewards:
            self.no_rewards()
            return

        # Create the checklist of the rewards.
        self.create_checklist()

    def collect_item(self) -> None:
        '''Debug state'''
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
                        'You have collected the following items from'
                        f' Agitha:')
            self.status_label.configure(text=new_text)


    def create_checklist(self) -> None:
        '''Create the checklist of the provided rewards.'''
        # Reset, but don't reset to default
        tab = self.program.reset_tab(self.tab_name, False)

        # Create the status label ----------------------------
        self.status_label = CTkLabel(master=tab,
                                     text=self.default_text)
        self.status_label.pack(anchor='w', padx=5, pady=5)
        # ----------------------------------------------------

        # Create the checklist frame ---------------------
        checklist_frame = CTkFrame(master=tab)
        checklist_frame.pack(anchor='w', padx=5, pady=5)
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
        '''Grab the text off the sign, and parse into the list of rewards.'''
        # Split off of the intro text
        raw_rewards = self.hint_text.split(': ')[1]

        # Remove the braces, and split into a list
        self.rewards = self.remove_braces(raw_rewards).split(', ')

    def remove_braces(self, text: str) -> str:
        '''Removes the {} from a given string.'''
        return text.replace('{', '').replace('}', '')
