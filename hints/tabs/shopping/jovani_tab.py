
# All of Jovani's special handling goes here.
from hints.control.program import Program
from hints.tabs.shopping.shopping import Shopping
from re import findall


class JovaniTab(Shopping):
    '''Jovani's special checklist handling.'''
    def __init__(self, program: Program, hint_text: str) -> None:
        '''Initialize the tab.'''
        # Initialize the default vars ----------------------------------
        # The static vars
        super().__init__(program, hint_text)

        # The tab name
        self.tab_name = 'Poes'

        # The default text for the label
        self.default_text = ('Jovani has learned,'
                             ' and rewards you with the following:\n')
        # --------------------------------------------------------------

        # If we had any text, then autofill.
        # Else, close the tab.
        if hint_text:
            self.auto_fill()
        else:
            self.no_rewards()

    def auto_fill(self) -> None:
        '''Populate the tab with the provided info.'''
        # Parse the rewards
        are_rewards = self.parse_rewards()

        # If there are no rewards, then leave
        if not are_rewards:
            return

        # If there are, create the checklist
        self.create_checklist()

    def parse_text(self) -> None:
        '''Debug state'''
        # Grab the threshold(s) and rewards(s) off of the sign text
        # Looking for 'xx souls reward: {[reward]}'
        self.rewards = findall(r'(\d+ souls reward: \{.*?\})', self.hint_text)
        print(self.rewards)
