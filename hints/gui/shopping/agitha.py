
# Home to the class which handles the logic for Agitha's shopping tab

from hints.gui.shopping.Parent import ShoppingListTab
from tkinter.ttk import Notebook

# TODO: https://github.com/SadieDragon/TPR-Hints-Tool/issues/29
# TODO: https://github.com/SadieDragon/TPR-Hints-Tool/issues/23

class AgithaTab(ShoppingListTab):
    '''The subclass for Agitha's tab.'''
    def __init__(self, notebook: Notebook, sign_text='') -> None:
        '''Initialize the tab.'''
        super().__init__(notebook, "Agitha's Castle")

        # If text was passed, then autofill
        # Else, load default page.
        if sign_text:
            self.auto_fill(sign_text)

    def auto_fill(self, sign_text: str) -> None:
        '''Autofill the tab based on the provided hints.'''
        # Parse the provided hint sign text into a list
        if ':' in sign_text:
            # Grab the rewards off of the intro text
            raw_rewards = sign_text.split(': ')[1]

            # Remove the braces and split into a list
            self.rewards = raw_rewards[1:-1].split(', ')

        # Assume a bad state
        self.text = 'Agitha gives you GREAT... sadness...'
        # If there are rewards
        if self.rewards:
            # Populate the tab with the parsed information
            self.create_checklist()
            self.text = 'Agitha gives you GREAT HAPPINESS:'

        # Set the label text
        self.set_default_label_text()
