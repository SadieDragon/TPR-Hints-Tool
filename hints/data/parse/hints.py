
# Contains the base parsing for the hints

from hints.gui.shopping.agitha import AgithaTab
from hints.gui.shopping.jovani import JovaniTab
from re import sub
from tkinter.ttk import Notebook

# TODO: https://github.com/SadieDragon/TPR-Hints-Tool/issues/34
# TODO: https://github.com/SadieDragon/TPR-Hints-Tool/issues/33


def parse_hints(spoiler_log_data: dict, notebook: Notebook) -> None:
    '''Parse the hints if a spoiler log is provided.'''
    # Grab the hints specifically out of the spoiler log
    hints = spoiler_log_data['hints']

    # hint_texts = []  # Holding for the normal hints
    # Parse the hint sign data
    for sign, hints_data in hints.items():
        # Cycle through the hints
        for hint_data in hints_data:
            # Grab the hint text itself.
            hint_text = hint_data['text']

            # Replace ♂ and ♀ (special characters)
            hint_text = hint_text.replace('â™‚', 'male')
            hint_text = hint_text.replace('â™€', 'female')
            # Clean up any excess spaces
            hint_text = sub(r' +', ' ', hint_text)

            # Special handling for Agitha
            if (sign == 'Agithas_Castle_Sign'):
                AgithaTab(notebook, hint_text)
            # Special handling for Jovani
            elif sign == 'Jovani_House_Sign':
                JovaniTab(notebook, hint_text)

            # Normal hints
            # elif 'They say that ' in hint_text:
            #     hint_texts.append(hint_text.replace('They say that ', ''))
