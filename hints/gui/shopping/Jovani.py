
# Home to the class which handles the logic for Jovani's shopping tab

from hints.gui.shopping.Parent import ShoppingListTab
from re import findall
from tkinter.ttk import Notebook

# BUG / TODO: https://github.com/SadieDragon/TPR-Hints-Tool/issues/51

# TODO: https://github.com/SadieDragon/TPR-Hints-Tool/issues/32
# TODO: https://github.com/SadieDragon/TPR-Hints-Tool/issues/29

class JovaniTab(ShoppingListTab):
    '''The subclass for Jovani's tab.'''
    def __init__(self, notebook: Notebook):
        '''Initialize the tab.'''
        super().__init__(notebook, "Jovani's Poes")

    def auto_fill(self, sign_text: str) -> None:
        '''Autofill the tab based on the provided hints.'''
        # Parse the sign text into a dict
        raw_rewards = self.parse_sign(sign_text)

        # Parse the rewards in the dict
        self.rewards = []  # Ensure the list is clean?
        bad_rewards = []   # Temp holding var
        for threshold_reward, quality in [*raw_rewards.items()]:
            # Store the required and thus good rewards for initial autofill
            if quality in ['good', 'required']:
                self.rewards.append(threshold_reward)
            # Rewards which are not needed get put into the temp var
            elif ('not' in quality) or (quality == 'bad'):
                bad_rewards.append(threshold_reward)

        # The default texts for Jovani's Redemption
        self.bad = 'Jovani remains greedy, and does not pay you well.'
        self.good = 'Jovani has learned, and rewards you with the following:'

        # Populate the tab with the good rewards first
        self.populate_tab()

        # Populate the tab with the bad rewards next
        if bad_rewards:
            self.rewards = bad_rewards
            self.create_checklist(True)

    def parse_sign(self, sign_text: str) -> dict:
        '''Parse the provided hint sign text into a dict.'''
        # Split the text into the two lines (Thx jaq for this regex)
        rewards = self.findall_to_list(r'^(.*\)) +(\d+ .*)$', sign_text)

        # Parse the individual lines
        jovani_rewards = {}
        for line in rewards:
            # Split the turn in threshold off of the reward
            # (with attached quality)
            threshold, item_quality = line.split(': ')

            # Remove the {} and (), and split into reward and quality
            reward, quality = self.findall_to_list(r'\{(.*?)\} \((.*?)\)',
                                                   item_quality)

            # Combine the reward with the threshold
            threshold_reward = ': '.join([threshold, reward])

            # Then store the rewards for later handling
            jovani_rewards[threshold_reward] = quality

        return jovani_rewards

    def findall_to_list(self, regex: str, to_parse: str) -> list:
        '''Returns the findall result as a list instead of tuple.'''
        return [*findall(regex, to_parse)[0]]
