
from json import load
from os import listdir, getcwd, abort
from pathlib import Path
from re import findall, sub
from tkinter import Tk
from tkinter import IntVar, StringVar
from tkinter import Checkbutton, Frame, Label, OptionMenu, Button
from tkinter.ttk import Notebook

# Global Variables ============================================================

# The default notebook color
default_notebook_bg = '#f9f9f9'

# =============================================================================

# Utility Functions ===========================================================

# An error case. (I like adding things and forgetting that I did.)
def case_not_expected() -> None:
    '''An error handling for debug purposes.'''
    print('I did not expect this option, dear dev.')
    abort()


# DRY
def create_text_checklist(start_str: str, checklist: list) -> str:
    '''Make label text for post completion.'''
    # Append the starting string to the checklist
    textlist = [start_str] + checklist

    # And then button it together.
    return '\n- '.join(textlist)

# =============================================================================

# GUI Functions ===============================================================

# DRY
def create_notebook_tab(notebook: Notebook, current_category: str) -> Frame:
    '''Turn a frame into a notebook tab.'''

    # Grab a list of the previous frames
    previous_frames = notebook.winfo_children()

    # Refresh the frames
    if (len(previous_frames) > 1) and (current_category == "Agitha's Castle"):
        # Remove everything that isn't the main frame
        for child in previous_frames[1:]:
            child.destroy()

    # The new frame
    new_frame = Frame(notebook, width=450, height=450, bg=default_notebook_bg)
    new_frame.pack(padx=5, expand=True)
    notebook.add(new_frame, text=current_category)

    # This will be used to pack things into
    return new_frame


# DRY
def completion_label(frame: Frame, completion_text: str) -> None:
    '''Create a label with the supplied text for when the checklist is done.'''
    new_label = Label(frame,
                      text = completion_text,
                      bg = default_notebook_bg,
                      justify = 'left')

    new_label.pack(anchor='nw', padx=5, pady=5)

# =============================================================================

# Hint Parsing ================================================================

# Run when the spoiler log is picked.
def dump_spoiler_log(spoiler_log: StringVar):
    global spoiler_log_folder

    # Figure out which log was chosen
    chosen_log = spoiler_log.get()

    # Get the path
    spoiler_log_path = spoiler_log_folder / chosen_log

    # Dump the data
    with open(spoiler_log_path, 'r') as f:
        spoiler_log_data = load(f)

    # Move on to parse the hints
    parse_hints(spoiler_log_data)


# Run after log data is dumped
def parse_hints(spoiler_log_data):
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
                AgithaTab(notebook, hint_text)
            # Special handling for Jovani
            elif sign == 'Jovani_House_Sign':
                JovaniTab(notebook, hint_text)

            # Normal hints
            elif 'They say that ' in hint_text:
                hint_texts.append(hint_text.replace('They say that ', ''))

    normal_hints_tab(hint_texts)


# Populate the last tab [FUTURE]
def normal_hints_tab(hints: list):
    print('hints -i am debug!-')

# =============================================================================

# Item Collection: Shopping Class =============================================

# The parent class for Agitha and Jovani
class ShoppingListTab():
    # Initializing
    def __init__(self, notebook, name):
        # Set the local constants of notebook and name
        self.notebook = notebook
        self.name = name

        # Create the dict to be populated {reward: IntVar}
        self.checkboxes = {}

        # And prepare the Frame and Label to be populated
        self.frame = None
        self.label = None
        self.label_var = StringVar()

    # A modification of create_notebook_tab, unique to these
    def create_tab(self):
        # Create the notebook tab
        self.frame = create_notebook_tab(self.notebook, self.name)

        # Create the new label in that tab, with the var
        self.label = Label(self.frame,
                           bg = default_notebook_bg,
                           textvariable = self.label_var,
                           justify = 'left')
        self.label.pack(padx=5, pady=5, anchor='nw')

    # create_checkbox was only really used for this,
    # and can be even more DRY across the two.
    def create_checklist(self, rewards):
        # Go through the item list
        for reward in rewards:
            # Create the IntVar for the state
            checkbox_var = IntVar()

            # Create the checkbox itself
            checkbox = Checkbutton(self.frame,
                                   text = reward,
                                   variable = checkbox_var,
                                   bg = default_notebook_bg,
                                   activebackground = default_notebook_bg,
                                   command = self.collect_item)
            checkbox.pack(padx=5, anchor='w')

            # And store the reward and new intvar
            self.checkboxes[reward] = checkbox_var

    # And collect_item, which was unique to them
    def collect_item(self):
        # Go through and check the states of the checkboxes
        checked = []
        for int_var in self.checkboxes.values():
            checked.append(int_var.get())

        # If all are true, update the text
        if all(checked):
            # (which is so long I create a new var)
            new_text = ('Congratulatins!'
                        ' There is nothing left to collect here.\n'
                        'You have collected the following items from'
                        f' {self.name}:')
            self.label_var.set(new_text)


# Agitha's subclass
class AgithaTab(ShoppingListTab):
    # Inherit the overall init, with the added param of
    # the hint sign text
    def __init__(self, notebook, sign_text):
        super().__init__(notebook, "Agitha's Castle")

        # Create the tab
        self.create_tab()

        # The default text for Agitha's Castle is
        self.label_var.set('Agitha gives you GREAT... sadness...')

        # And then set up the list to begin populating the tab
        rewards = self.parse_sign(sign_text)
        # If there is a list of rewards, make a checklist
        if rewards:
            # Then create the checklist
            self.create_checklist(rewards)

            # TODO: put a better label text here
            self.label_var.set('Agitha gives you GREAT HAPPINESS:')

    # Take the sign text and parse it down into a list
    # of the rewards
    def parse_sign(self, sign_text: str):
        rewards_list = []
        if ':' in sign_text:
            # Grab the rewards off of the intro
            rewards = sign_text.split(': ')[1]

            # Remove the braces and split into a list
            rewards_list = rewards[1:-1].split(', ')

        return rewards_list

# Jovani's subclass
class JovaniTab(ShoppingListTab):
    def __init__(self, notebook, sign_text):
        # Inherit the overall init, with the added param of
        # the hint sign text
        super().__init__(notebook, "Jovani's Poes")

        # Create the tab
        self.create_tab()

        # And set up to begin populating the tab
        rewards = self.parse_sign(sign_text)

        # Parse the rewards that jovani gives
        bad_rewards = []
        good_rewards = []
        for threshold, reward_quality in [*rewards.items()]:
            # Unpack the rewards and quality
            reward, quality = reward_quality

            # Put the threshold with the reward
            threshold_reward = ': '.join([threshold, reward])

            # These rewards are NOT needed
            if ('not' in quality) or (quality == 'bad'):
                bad_rewards.append(threshold_reward)
            # These rewards ARE needed
            elif quality in ['good', 'required']:
                good_rewards.append(threshold_reward)

        # By default his text is
        self.label_var.set('Jovani remains greedy, and does not pay you well.')

        # If he actually has something good..
        if good_rewards:
            # Make the checklist
            self.create_checklist(good_rewards)

            # TODO: put a better label text here
            self.label_var.set(('Jovani has learned,'
                               'and rewards you with the following:'))

        # If he has bad rewards, make a text checklist,
        # and make a new label.
        if bad_rewards:
            for reward in bad_rewards:
                new_label = Label(self.frame,
                                  text = reward,
                                  bg = default_notebook_bg,
                                  justify = 'left')
                new_label.pack(anchor='nw', padx=5, pady=5)

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
    root.geometry('500x500')
    root.title('Hint Tracker Tool')
    root.config(bg='#2f3136')
    # -------------------------------

    # Set up the notebook ------------------------------------
    notebook = Notebook(root, width=495, height=475)
    notebook.pack(padx=5, pady=5, expand=False, anchor='nw')
    # --------------------------------------------------------

    # Obtain currrent location -------------------------
    # Get the root folder
    spoiler_log_folder = Path(getcwd()) / 'SpoilerLog'

    # Grab a list of available spoiler logs
    spoiler_logs = listdir(spoiler_log_folder)

    # If there are none, break and inform the user.
    if not spoiler_logs:
        print('Please supply a spoiler log.')
        abort()
    # --------------------------------------------------

    # Intro Page ------------------------------------------------------
    # DRY / easy change in the future
    current_category = "Main Page"
    main_page_frame = create_notebook_tab(notebook, current_category)
    # -----------------------------------------------------------------

    # Pick a spoiler log ------------------------------------------------------
    # The frame for this so I can grid it in
    spoiler_log_frame = Frame(main_page_frame, bg=default_notebook_bg)
    spoiler_log_frame.grid(row=0, column=0, padx=5, pady=5)

    # The variable that will hold the spoiler log choice
    spoiler_log = StringVar()
    spoiler_log.set(spoiler_logs[0])

    # The drop down to actually pick the spoiler log
    spoiler_log_dropdown = OptionMenu(spoiler_log_frame,
                                      spoiler_log,
                                      *spoiler_logs)
    spoiler_log_dropdown.pack(padx=5, pady=5)

    # Confirmation button
    confirm_spoiler_log = Button(spoiler_log_frame,
                                 text='Confirm',
                                 command=lambda: dump_spoiler_log(spoiler_log))
    confirm_spoiler_log.pack(padx=5, pady=5)
    # -------------------------------------------------------------------------

    # And run the window plz.
    root.mainloop()
