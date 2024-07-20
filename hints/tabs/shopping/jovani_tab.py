
# All of Jovani's special handling goes here.
from hints.control.program import Program
from hints.tabs.shopping.shopping import Shopping
from re import findall


class JovaniTab(Shopping):
    '''Jovani's special checklist handling.'''
    # The boolean qualities (True: required, False: not required)
    qualities = []

    def __init__(self, program: Program, hint_text: str) -> None:
        '''Initialize the tab.'''
        # Initialize the default vars ----------------------------------
        # The static vars
        super().__init__(program, hint_text)

        # The tab name
        self.tab_name = 'Poes'

        # The default text for the label
        self.default_text = ('Jovani has these items for you:\n')
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

        # Parse the qualities
        self.parse_qualities()

        # If there are no qualities (no-logic), leave.
        if not self.qualities:
            return

        # Update the checklist to disable not-required rewards
        self.update_checklist()

        # Update the label text
        self.update_label()

    def parse_text(self) -> None:
        '''Grab the text off the sign, and parse into the list of rewards.'''
        # Grab the threshold(s) and rewards(s) off of the sign text
        # Looking for 'xx souls reward: {[reward]}'
        self.rewards = findall(r'(\d+ souls reward: \{.*?\})', self.hint_text)

    def parse_qualities(self) -> None:
        '''Parses the qualities of the rewards.'''
        # Grab specifically the reward(s) values
        # [a-z] is enforcing that it grabs the quality, not quantity
        text_qaulities = findall(r'\(([a-z].*?)\)', self.hint_text)

        # Convert them into a True/False based on if they are good/bad
        for quality in text_qaulities:
            # Store if they are good are bad
            self.qualities.append((quality in ['required', 'good']))

    def update_checklist(self) -> None:
        '''Disables the bad items of the checklist.'''
        # Go through each, and disable the bad
        for index, is_required in [*enumerate(self.qualities)]:
            # If it is required, continue
            if is_required:
                continue

            # Otherwise, disable the checklist
            self.checkboxes[index].configure(state='disabled')
            self.checkbox_vars[index].set(1)

    def update_label(self) -> None:
        '''Changes the label text to match.'''
        # Assume it's bad, cause it's usually bad.
        text = ('Jovani remains greedy, and does not pay you well.')
        # If all of the qualities were good, then the text is good.
        if all(self.qualities):
            text = ('Jovani has learned, and rewards you with the following:')

        # Append a newline, to be consistent,
        # and store as default.
        self.default_text = f'{text}\n'

        # Update the label text, and default text
        self.status_label.configure(text=self.default_text)
