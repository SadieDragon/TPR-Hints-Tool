
# Home to the class which handles the logic for Jovani's shopping tab

from hints.gui.shopping.shopping_list_tab import ShoppingListTab
from re import findall
from tkinter.ttk import Notebook

# TODO: https://github.com/SadieDragon/TPR-Hints-Tool/issues/54
# TODO: https://github.com/SadieDragon/TPR-Hints-Tool/issues/29


# BUG: he's broken again, figure out how and why and post issue


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

        # Grab the threshold(s) and rewards(s) off of the sign text
        # Looking for 'xx souls reward: {[reward]}'
        self.rewards = findall(r'(\d+ souls reward: \{.*?\})', sign_text)

        # Create the checklist
        self.create_checklist()

        # Grab specificall the reward(s) values
        reward_qaulities = findall(r'\((.*?)\)', sign_text)

        # Assume a neutral status
        self.text = 'Jovani has these items for you:'
        # If we have rewards to parse, determine if the text should
        # be good or bad, and disable checkboxes as needed
        if reward_qaulities:
            qualities = []
            for index, quality in [*enumerate(reward_qaulities)]:
                if ('not' in quality) or (quality == 'bad'):
                    # Disable the checkbox
                    self.checkboxes[index].config(state='disabled')
                    self.checkbox_vars[index].set(1)
                    # Store this was a bad apple
                    qualities.append(0)

            # Assume bad text (it's usually bad)
            self.text = 'Jovani remains greedy, and does not pay you well.'
            # If all of the checkboxes were allowed to pass, good text
            if all(qualities):
                self.text = ('Jovani has learned,'
                             ' and rewards you with the following:')

        # Set the label text
        self.set_default_label_text()
