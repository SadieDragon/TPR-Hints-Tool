
from json import load
from re import findall, sub
from tkinter import Tk, Toplevel, messagebox
from tkinter import StringVar
from tkinter import Button
from tkinter.ttk import Notebook, OptionMenu

from hints.Globals import return_logs_list, return_spoiler_folder
from hints.gui.Globals import return_default_bg
from hints.gui.Utils import create_notebook_tab
from hints.gui.shopping.Agitha import AgithaTab
from hints.gui.shopping.Parent import ShoppingListTab

# Global Variables ============================================================

# The default notebook color
default_notebook_bg = return_default_bg()

# This will be updated and set later on,
# and used in many places
seed_name = 'Please pick a seed.'

# =============================================================================

# Utility Functions ===========================================================

# DRY: Reset the tool.
def reset_tracker(notebook: Notebook) -> None:
    # Get the widgets.
    current_tabs = notebook.winfo_children()

    # If there's only 1 tab, we do not need to reset
    if len(current_tabs) > 1:
        print(current_tabs[1].winfo_children())
        # Remove all but the first tab's contents
        for widget in current_tabs[1:]:
            for child in widget.winfo_children():
                child.destroy()


# Verify Reset
def verify_reset(notebook: Notebook):
    # A warning of "are you sure, mate?" PEP8 compliance
    warning = 'Are you sure? This will wipe everything.'
    if messagebox.askokcancel('Verify Reset', warning):
        reset_tracker(notebook)

# =============================================================================

# GUI Functions ===============================================================

# Create the pop up for picking the spoiler log
def spoiler_pop_up(files: list, notebook: Notebook):
    global pop_up

    # The pop up window specifically
    pop_up = Toplevel(root, bg=default_notebook_bg)
    pop_up.title('Pick a spoiler log')
    pop_up.geometry('500x90')

    # The var that will hold the spoiler log choice
    spoiler_log = StringVar()

    # Grab the longest file name
    longest_spoiler_name = max(files, key=len)
    # And then the length of it, +5 for a buffer
    longest = len(longest_spoiler_name) + 5

    spoiler_logs = return_logs_list()

    # The drop down to actually pick the spoiler log
    spoiler_log_dropdown = OptionMenu(pop_up,
                                      spoiler_log,
                                      files[0],
                                      *spoiler_logs)
    spoiler_log_dropdown.config(width=longest)
    spoiler_log_dropdown.pack(padx=5, pady=10)

    # PEP8 compliant command
    c = lambda: dump_spoiler_log(spoiler_log, notebook)
    # Confirmation button
    confirm_spoiler_log = Button(pop_up,
                                 text = 'Confirm',
                                 command = c)
    confirm_spoiler_log.pack(padx=5, pady=5)


# DRY: set up buttons on the main page
def main_page_button(notebook: Notebook,
                     text: str,
                     row_column: list,
                     command=None) -> None:
    row, column = row_column
    new_button = Button(notebook, text=text, command=command)
    new_button.grid(padx=5, pady=5, row=row, column=column)

# =============================================================================

# Hint Parsing ================================================================

# Run when the spoiler log is picked.
def dump_spoiler_log(spoiler_log: StringVar, notebook: Notebook):
    global seed_name

    # Let go of the window
    pop_up.destroy()

    # Reset the tracker
    reset_tracker(notebook)

    # Figure out which log was chosen
    chosen_log = spoiler_log.get()

    # Set the seed name, which is encased in -- --
    seed_name = findall(r'\-\-(.*?)\-\-', chosen_log)[0]

    # Set the title of the window
    root.title(f'Hint Tracker Tool: {seed_name}')

    # Get the path
    spoiler_log_folder = return_spoiler_folder()
    spoiler_log_path = spoiler_log_folder / chosen_log

    # Dump the data
    with open(spoiler_log_path, 'r') as f:
        spoiler_log_data = load(f)

    # Move on to parse the hints
    parse_hints(spoiler_log_data)


# Run after log data is dumped
def parse_hints(spoiler_log_data):
    global agitha, jovani
    # Grab the hints specifically out of the spoiler log
    hints = spoiler_log_data['hints']

    # Nab the hint texts
    hint_texts = []
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
                agitha.auto_fill(hint_text)
            # Special handling for Jovani
            elif sign == 'Jovani_House_Sign':
                jovani.auto_fill(hint_text)

            # Normal hints
            elif 'They say that ' in hint_text:
                hint_texts.append(hint_text.replace('They say that ', ''))

    normal_hints_tab(hint_texts)


# Populate the last tab [FUTURE]
def normal_hints_tab(hints: list):
    print('hints -i am debug!-')

# =============================================================================

# Item Collection: Shopping Class =============================================

# Jovani's subclass
class JovaniTab(ShoppingListTab):
    def __init__(self, notebook):
        # Inherit the overall init, with the added param of
        # the hint sign text
        super().__init__(notebook, "Jovani's Poes")

    def auto_fill(self, sign_text):
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

        # And disable the box *now*
        self.textbox['state'] = 'disabled'

    # Take the sign text and parse it into a dict
    # representing the thresholds and rewards
    def parse_sign(self, sign_text):
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

# =============================================================================

# Script Execution ============================================================

# There should always be a main guard for things that are
# not run locally by me, because things could be different.
if __name__ == '__main__':
    # Set up the window -------------
    root = Tk()
    root.title(seed_name)
    root.geometry('500x500')
    root.config(bg='#2f3136')
    # -------------------------------

    # Set up the notebook ------------------------------------
    notebook = Notebook(root, width=495, height=475)
    notebook.pack(padx=5, pady=5, expand=False, anchor='nw')
    # --------------------------------------------------------

    # Intro Page ------------------------------------------------------
    main_page_frame = create_notebook_tab(notebook, "Main Page")
    # -----------------------------------------------------------------

    # Pick a spoiler log ---------------------------------------------------
    # PEP8 compliance and readability
    command = lambda: spoiler_pop_up(return_logs_list(), notebook)
    # Create the button
    main_page_button(main_page_frame, 'Pick Spoiler Log', [0, 0], command)
    # ----------------------------------------------------------------------

    # Make Agitha and Jovani -----
    agitha = AgithaTab(notebook)
    jovani = JovaniTab(notebook)
    # ----------------------------

    # Reset Button ------------------------------------------------------
    # PEP8 compliance and readability
    command = lambda: verify_reset(notebook)
    main_page_button(main_page_frame, 'Reset Tracker', [0, 1], command)
    # -------------------------------------------------------------------

    # And run the window plz.
    root.mainloop()
