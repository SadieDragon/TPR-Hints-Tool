
# Home to the class which handles the logic for Jovani's shopping tab

from hints.gui.shopping.Parent import ShoppingListTab
from re import findall
from tkinter.ttk import Notebook

# TODO: https://github.com/SadieDragon/TPR-Hints-Tool/issues/32
# TODO: https://github.com/SadieDragon/TPR-Hints-Tool/issues/29

class JovaniTab(ShoppingListTab):
    '''The subclass for Jovani's tab.'''
    def __init__(self, notebook: Notebook, sign_text=''):
        '''Initialize the tab.'''
        super().__init__(notebook, "Jovani's Poes")

        # If text was passed, then autofill
        # Else, load default page.
        if sign_text:
            self.auto_fill(sign_text)

    def auto_fill(self, sign_text: str) -> None:
        '''Autofill the tab based on the provided hints.'''
        # Ensure that rewards is made
        self.rewards = []

        # Split the text into the two lines (Thx jaq for this regex)
        rewards = self.findall_to_list(r'^(.*\)) +(\d+ .*)$', sign_text)

        # Parse the individual lines
        for line in rewards:
            # Split the turn in threshold off of the reward
            # (with attached quality)
            threshold, item_quality = line.split(': ')

            # Remove the {} and (), and split into reward and quality
            reward, quality = self.findall_to_list(r'\{(.*?)\} \((.*?)\)',
                                                   item_quality)

            # Combine the reward with the threshold
            threshold_reward = ': '.join([threshold, reward])

            # The holding var to append (reward : to_disable)
            to_append = [threshold_reward, False]

            # Rewards which are not needed get the flag to disable
            if ('not' in quality) or (quality == 'bad'):
                to_append[1] = True

            # Append the list to the rewards array
            self.rewards.append(to_append)

        # The default texts for Jovani's Redemption
        self.bad = 'Jovani remains greedy, and does not pay you well.'
        self.good = 'Jovani has learned, and rewards you with the following:'

        # Populate the tab
        self.populate_tab(True)

    def findall_to_list(self, regex: str, to_parse: str) -> list:
        '''Returns the findall result as a list instead of tuple.'''
        return [*findall(regex, to_parse)[0]]
