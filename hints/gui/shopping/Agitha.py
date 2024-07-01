
# Home to the class which handles the logic for Agitha's shopping tab

from hints.gui.shopping.Parent import ShoppingListTab
from tkinter.ttk import Notebook

# TODO: Add custom text for the happiness,
# based on how many rewards she provides.
# https://github.com/SadieDragon/TPR-Hints-Tool/issues/29

class AgithaTab(ShoppingListTab):
    '''The subclass for Agitha's tab.'''
    def __init__(self, notebook: Notebook) -> None:
        '''Initialize the tab.'''
        super().__init__(notebook, "Agitha's Castle")

    def auto_fill(self, sign_text: str) -> None:
        '''Autofill the tab based on the provided hints.'''
        # Parse the provided hint sign text into a list
        if ':' in sign_text:
            # Grab the rewards off of the intro text
            raw_rewards = sign_text.split(': ')[1]

            # Remove the braces and split into a list
            self.rewards = raw_rewards[1:-1].split(', ')

        # The default texts for Agitha's Castle
        self.bad= 'Agitha gives you GREAT... sadness...'
        self.good = 'Agitha gives you GREAT HAPPINESS:'

        # Populate the tab with the parsed information
        self.populate_tab()
