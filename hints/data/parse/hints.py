
# Contains the base parsing for the hints

from hints.gui.shopping.agitha_tab import AgithaTab
from hints.gui.shopping.jovani_tab import JovaniTab
from re import sub
from tkinter.ttk import Notebook


def parse_hints(spoiler_log_data: dict, notebook: Notebook) -> None:
    '''Parse the hints if a spoiler log is provided.'''
    # Grab the hints specifically out of the spoiler log
    hints = spoiler_log_data['hints']

    # Parse the hint sign data
    for sign, hints_data in hints.items():
        # Cycle through the hints
        for hint_data in hints_data:
            # Grab the hint text itself.
            hint_text = hint_data['text']

            # Clean up any excess spaces
            hint_text = sub(r' +', ' ', hint_text)

            # Special handling for Agitha
            if (sign == 'Agithas_Castle_Sign'):
                AgithaTab(notebook, sign_text=hint_text)
            # Special handling for Jovani
            elif sign == 'Jovani_House_Sign':
                JovaniTab(notebook, sign_text=hint_text)
