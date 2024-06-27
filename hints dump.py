
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

# DRY
def findall_to_list(regex: str, to_parse: str) -> list:
    '''Returns the findall result as a list instead of tuple.'''
    return [*findall(regex, to_parse)[0]]


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
def create_notebook_tab(notebook: Notebook,
                        current_category: str,
                        make_label = True) -> list:
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

    new_label = ''
    if make_label:
        # And pack a Label into there for later adjusting
        new_label = Label(new_frame, bg=default_notebook_bg)
        new_label.pack(padx=5, pady=5, anchor='nw')

    # This will be used to pack things into
    return [new_label, new_frame]


# DRY
def completion_label(frame: Frame, completion_text: str) -> None:
    '''Create a label with the supplied text for when the checklist is done.'''
    new_label = Label(frame,
                      text = completion_text,
                      bg = default_notebook_bg,
                      justify = 'left')

    new_label.pack(anchor='nw', padx=5, pady=5)


# DRY
def create_checkbox(label: str, frame: Frame, command=None) -> tuple:
    '''Create the shopping lists.'''

    # Create the variable to store the state
    new_var = IntVar()

    # Create the checkbox itself
    new_check = Checkbutton(frame, text=label, variable=new_var)
    new_check.config(bg = default_notebook_bg,
                     activebackground = default_notebook_bg)
    new_check.pack(padx=5, anchor='w')

    if command:
        new_check.config(command=command)

    # Return the intvar for later parsing
    return new_var

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

    jovani_rewards = {}
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
                agitha_checklist = []
                # If she shares happiness, populate the checklist
                if (':' in hint_text):
                    # Grab the rewards for agitha's castle
                    rewards = hint_text.split(': ')[1]
                    # Remove the braces, and split into a list
                    agitha_checklist = rewards[1:-1].split(', ')

                agithas_castle(agitha_checklist)

            # Special handling for Jovani
            elif sign == 'Jovani_House_Sign':
                # Split the text into the two lines (Thx jaq for this regex)
                rewards = findall_to_list(r'^(.*\)) +(\d+ .*)$', hint_text)

                for line in rewards:
                    # Split the turn in threshold off of the reward
                    # (with attached quality)
                    threshold, item_quality = line.split(': ')

                    # Remove the {} and (), and split into an array.
                    item_quality = findall_to_list(r'\{(.*?)\} \((.*?)\)',
                                                item_quality)

                    # Then store the rewards for later handling
                    jovani_rewards[threshold] = item_quality

                # And populate the page.
                jovanis_redemption(jovani_rewards)

            # Normal hints
            elif 'They say that ' in hint_text:
                hint_texts.append(hint_text.replace('They say that ', ''))

    normal_hints_tab(hint_texts)


# Populate Agitha's Castle tab
def agithas_castle(agitha_list: list):
    global agitha_checks, agitha_frame, agitha_text

    # Make the input list a global var
    agitha_checklist = agitha_list

    # Create the tab for Agitha's Castle
    # (grabbing the label to update the text later)
    agitha_label, agitha_frame = create_notebook_tab(notebook,
                                                     "Agitha's Castle")

    # The text to be set later
    agitha_text = StringVar()
    # Should Agitha have nothing, inform the player.
    agitha_checks = {}
    if not agitha_checklist:
        # Create the text for the label
        blank_text = 'Agitha gives you GREAT... sadness...'

        # And then create the label.
        completion_label(agitha_frame, blank_text)

    # Otherwise, inform the player.
    else:
        # Create the checklist
        for agitha_item in agitha_checklist:
            # PEP 8 character limit compliance
            checkbox_var = create_checkbox(agitha_item,
                                           agitha_frame,
                                           command = agitha_item_get)
            # Store the item and the intvar for later parsing
            agitha_checks[agitha_item] = checkbox_var

    # Configure the label to use the new textvar
    agitha_label.config(textvariable=agitha_text)


# Populate Jovani's Redemption tab
def jovanis_redemption(jovani_rewards: dict):
    global jovani_checks, jovani_frame, jovani_text

    # Go through and parse the rewards that jovani gives
    bad_jovani_rewards = []
    jovani_checklist = []
    for threshold, reward_quality in [*jovani_rewards.items()]:
        # Unpack the rewards and quality
        reward, quality = reward_quality

        # Put the threshold with the reward
        threshold_reward = ': '.join([threshold, reward])

        # These rewards are NOT needed
        if ('not' in quality) or (quality == 'bad'):
            bad_jovani_rewards.append(threshold_reward)
        # These rewards ARE needed
        elif quality in ['good', 'required']:
            jovani_checklist.append(threshold_reward)

    # Create the tab for Jovani (grabbing the label to update the text later)
    jovani_label, jovani_frame = create_notebook_tab(notebook, "Jovani's Poes")

    # Text to be set later
    jovani_text = StringVar()
    # If there are at least 1, then make the checklist.
    jovani_checks = {}
    if len(jovani_checklist) != 0:
        for reward in jovani_checklist:
            # PEP 8 character limit compliance
            checkbox_var = create_checkbox(reward,
                                           jovani_frame,
                                           command = jovani_item_get)

            # Store the item and the intvar for later parsing
            jovani_checks[reward] = checkbox_var

    # Otherwise, inform the player.
    else:
        # Create the text for the label
        blank_text = 'Jovani remains greedy, and does not pay you well.'

        blank_text = create_text_checklist(blank_text, bad_jovani_rewards)

        # And then create the label.
        completion_label(jovani_frame, blank_text)

    # Configure the label to use the new textvar
    jovani_label.config(textvariable=jovani_text)


# Populate the last tab [FUTURE]
def normal_hints_tab(hints: list):
    print('hints -i am debug!-')

# =============================================================================

# Item Collection Logic =======================================================

def item_collection(checkboxes: dict,
                    base_frame: Frame,
                    person: str,
                    label_var: StringVar) -> None:
    '''The item completion and collection framework for the shopping lists.'''

    # Go through and parse the intvars without resetting
    # the base checklist, for easier parsing.
    checked = []
    for int_var in checkboxes.values():
        checked.append(int_var.get())

    # And then if all are true, update the label text
    if all(checked):
        # Could be 1 line but it's a bit easier to understand split up
        label_text = ('Congratulations!'
                      ' There is nothing left to collect here.\n'
                      f'You have collected the following from {person}:\n')
        label_var.set(label_text)

    print(base_frame.winfo_children())


def agitha_item_get() -> None:
    '''Passes item_collection() the information for Agitha'''
    global agitha_checks, agitha_frame, agitha_text

    item_collection(agitha_checks, agitha_frame, 'Agitha', agitha_text)


def jovani_item_get() -> None:
    '''Passes item_collection() the information for Jovani.'''
    global jovani_checks, jovani_frame, jovani_text

    item_collection(jovani_checks, jovani_frame, 'Jovani', jovani_text)

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
    main_page_frame = create_notebook_tab(notebook, current_category, False)[1]
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
