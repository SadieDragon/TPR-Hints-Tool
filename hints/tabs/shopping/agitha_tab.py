
# All of Agitha's special handling and utilities.

from hints.tabs.shopping.shopping import Shopping
from hints.utils.constants import tab_names

from hints.gui_management.managers import ResetUtils


class AgithaTab(Shopping):
    '''Agitha's special checklist handling.'''
    def __init__(self,
                 hint_text:str,
                 resetter: ResetUtils) -> None:
        '''Initialize the tab.'''
        # Initialize the default vars -----------------------------
        # The static vars
        super().__init__(hint_text, resetter)

        # The tab name
        self.tab_name = tab_names.agitha_tab_name

        # The default text for the label
        self.default_text = 'Agitha gives you GREAT HAPPINESS:\n'
        # ---------------------------------------------------------

        # Check if there are any hints.
        # If there are, then we'll move forward.
        if ':' in self.hint_text:
            self.auto_fill()
        # Otherwise, just close the tab.
        else:
            self.no_rewards()

    def auto_fill(self) -> None:
        '''Populate the tab with the provided info.'''
        # Parse the rewards
        are_rewards = self.parse_rewards()

        # Create the checklist itself, if rewards
        if are_rewards:
            self.create_checklist()

    def parse_text(self) -> None:
        '''Grab the text off the sign, and parse into the list of rewards.'''
        # Split off of the intro text
        raw_rewards = self.hint_text.split(': ')[1]

        # Remove the braces, and split into a list
        self.rewards = self.remove_braces(raw_rewards).split(', ')
