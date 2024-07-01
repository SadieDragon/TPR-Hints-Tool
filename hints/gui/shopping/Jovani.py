
# Home to the class which handles the logic for Jovani's shopping tab

from hints.gui.shopping.Parent import ShoppingListTab
from re import findall
from tkinter.ttk import Notebook

# BUG: https://github.com/SadieDragon/TPR-Hints-Tool/issues/50
# BUG: https://github.com/SadieDragon/TPR-Hints-Tool/issues/44

# TODO: https://github.com/SadieDragon/TPR-Hints-Tool/issues/32
# TODO: https://github.com/SadieDragon/TPR-Hints-Tool/issues/29

class JovaniTab(ShoppingListTab):
    '''The subclass for Jovani's tab.'''
    def __init__(self, notebook: Notebook):
        '''Initialize the tab.'''
        super().__init__(notebook, "Jovani's Poes")

    def auto_fill(self, sign_text: str) -> None:
        '''Autofill the tab based on the provided hints.'''
        # And set up to begin populating the tab
        raw_rewards = self.parse_sign(sign_text)

        # Parse the rewards that jovani gives
        bad_rewards = []
        for threshold, reward_quality in [*raw_rewards.items()]:
            # Unpack the rewards and quality
            reward, quality = reward_quality

            # Put the threshold with the reward
            threshold_reward = ': '.join([threshold, reward])

            # These rewards are NOT needed
            if ('not' in quality) or (quality == 'bad'):
                bad_rewards.append(threshold_reward)
            # These rewards ARE needed
            elif quality in ['good', 'required']:
                self.rewards.append(threshold_reward)

        # The default texts for Jovani's Redemption
        self.bad = 'Jovani remains greedy, and does not pay you well.'
        self.good = 'Jovani has learned, and rewards you with the following:'

        # Populate the tab
        self.populate_tab()

        # If he has bad rewards, make a text checklist,
        # and make a new label.
        if bad_rewards:
            # Update rewards, because I don't think it matters?
            self.rewards = bad_rewards

            # And checklist but diff
            self.create_checklist(True)

    # Take the sign text and parse it into a dict
    # representing the thresholds and rewards
    def parse_sign(self, sign_text: str) -> dict:
        '''Parse the provided hint sign text into a dict.'''
        # Split the text into the two lines (Thx jaq for this regex)
        rewards = self.findall_to_list(r'^(.*\)) +(\d+ .*)$', sign_text)

        # Get the dict itself
        jovani_rewards = {}
        for line in rewards:
            # Split the turn in threshold off of the reward
            # (with attached quality)
            threshold, item_quality = line.split(': ')

            # Remove the {} and (), and split into an array.
            item_quality = self.findall_to_list(r'\{(.*?)\} \((.*?)\)',
                                                item_quality)

            # Then store the rewards for later handling
            jovani_rewards[threshold] = item_quality

        # Spit back the rewards
        return jovani_rewards

    def findall_to_list(self, regex: str, to_parse: str) -> list:
        '''Returns the findall result as a list instead of tuple.'''
        return [*findall(regex, to_parse)[0]]