
# All of Jovani's special handling goes here.
from hints.control.program import Program
from hints.tabs.shopping.shopping import Shopping


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
        '''Debug state'''
        print()
