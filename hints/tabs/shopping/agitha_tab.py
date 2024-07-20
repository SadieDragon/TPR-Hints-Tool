
# All of Agitha's special handling goes here.
from hints.control.program import Program
from hints.tabs.shopping.shopping import Shopping


class AgithaTab(Shopping):
    '''Agitha's special checklist handling.'''
    def __init__(self, program: Program, hint_text: str) -> None:
        '''Initialize the tab.'''
        # Initialize the default vars -----------------------------
        # The static vars
        super().__init__(program, hint_text)

        # The tab name
        self.tab_name = 'Bugs'

        # The default text for the label
        self.default_text = 'Agitha gives you GREAT HAPPINESS:\n'
        # ---------------------------------------------------------

        # Check if there's any hints.
        # If there are, then we'll move forward.
        if ':' in self.hint_text:
            self.auto_fill()
        # Otherwise, just close the tab.
        else:
            self.no_rewards()

    def parse_rewards(self) -> None:
        '''Grab the text off the sign, and parse into the list of rewards.'''
        # Split off of the intro text
        raw_rewards = self.hint_text.split(': ')[1]

        # Remove the braces, and split into a list
        self.rewards = self.remove_braces(raw_rewards).split(', ')
