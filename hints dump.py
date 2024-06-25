
from os import listdir
from json import load

from os import abort

from tkinter import Tk, Checkbutton, Frame, IntVar, Label
from tkinter.ttk import Notebook

# Constants ===================================================================

default_notebook_bg = '#f9f9f9'

# =============================================================================

# Function Land ===============================================================

# An error case.
def case_not_expected():
    print('I did not expect this option, dear dev.')
    abort()


# DRY: Make label text for post completion.
def create_text_checklist(start_str: str, checklist: list):
    # Append the starting string to the checklist
    textlist = [start_str] + checklist

    # And then button it together.
    return '\n- '.join(textlist)


# DRY: Create a label with the text for post complete.
def completion_label(frame: Frame, completion_text: str):
    new_label = Label(frame,
                      text = completion_text,
                      bg = default_notebook_bg,
                      justify = 'left')

    new_label.pack(anchor='nw', padx=5, pady=5)


# DRY: The item completion and collection framework is the
# same for both Jovani and Agitha, so I'm just going to make the
# framework.
def item_collection(checkboxes: list,
                    base_checklist: list,
                    base_frame: Frame,
                    person: str):
    global default_notebook_bg

    # We will return how many are collected,
    # for future use and reducing the loop.
    collected = 0

    # Find the one that's set
    for checkbox_group in checkboxes:
        # Grab the state of the checkbox
        check_state = checkbox_group[1].get()

        # If it is 1, then that is the one we need to update
        if check_state == 1:
            # Set the state to 2 to indicate that it's set,
            # and will not be unset.
            checkbox_group[1].set(2)

            # Disable the checkbox.
            checkbox_group[0].config(state = 'disabled',
                                     relief = 'ridge',
                                     bg = '#f0f0f0')

            # And add that to the collected check
            collected += 1
        # Count all of the collected items
        elif check_state == 2:
            collected += 1

    if collected == len(checkboxes):
        # Empty the frame
        for widget in base_frame.winfo_children():
            widget.destroy()

        # Create the text we're gonna be displaying
        new_text = ('Congratulations! There is nothing left to collect here.\n'
                    f'You have collected the following from {person}:\n')

        new_text = create_text_checklist(new_text, base_checklist)

        # And create the label.
        completion_label(base_frame, new_text)


# Pass forward the information for Agitha's tab when an item is clicked
def agitha_item_get():
    global agitha_checks, agitha_checklist, agitha_frame

    item_collection(agitha_checks,
                    agitha_checklist,
                    agitha_frame,
                    'Agitha')


# Pass forward the information for Jovani's tab when an item is clicked
def jovani_item_get():
    global jovani_checks, jovani_reward_checklist, jovani_frame

    item_collection(jovani_checks,
                    jovani_reward_checklist,
                    jovani_frame,
                    'Jovani')


# DRY- create a notebook tab
def create_notebook_tab():
    global root, notebook, default_notebook_bg, current_category

    new_frame = Frame(notebook, width=450, height=450, bg=default_notebook_bg)
    new_frame.pack(padx=5, expand=True)
    notebook.add(new_frame, text=current_category)

    # This will be used to pack things into
    return new_frame


# DRY- create the checklist widgets
def create_checkbox(label: str, frame: Frame):
    global default_notebook_bg, current_category

    # Create the variable to store the state
    new_var = IntVar()

    # Create the checkbox itself
    new_check = Checkbutton(frame, text=label, variable=new_var)
    new_check.config(bg = default_notebook_bg,
                     activebackground = default_notebook_bg,
                     disabledforeground = '#aa6a62')
    new_check.pack(padx=5, anchor='w')

    # Return both the intvar, and the checkbox.
    output = [new_check, new_var]

    # Set the command
    match current_category:
        case "Agitha's Castle":
            new_check.config(command = agitha_item_get)
        case "Jovani's Poes":
            new_check.config(command = jovani_item_get)
        case _:
            case_not_expected()

    # Used later
    return output


# DRY: Remove the {} from the important texts of Jovani and Agitha.
def remove_braces(text: str) -> str:
    return text[1:-1]

# =============================================================================

# Get Hints ===================================================================

# Grab the spoiler log path and location
spoiler_log_folder = ("L:/EmuDepot/trackers/Pixie's TPR Tracker/"
                    "Pixie's TPR Tracker_Data/SpoilerLog")

spoiler_log = listdir(spoiler_log_folder)[0]

spoiler_log_path = '/'.join([spoiler_log_folder, spoiler_log])

# Grab the data
with open(spoiler_log_path, 'r') as f:
    spoiler_log_data = load(f)

# Grab the hints specifically
hints = spoiler_log_data['hints']

# Nab the hint texts
hint_texts = []
agitha_checklist = ''
jovani_checklist = []
for sign, hints_data in [*hints.items()]:
    for hint_data in hints_data:
        # Grab the hint text itself.
        hint_text = hint_data['text']

        # Grab the hint
        hint = ''

        # Normal hints
        default_starter = 'They say that '
        if default_starter in hint_text:
            hint = hint_text.replace(default_starter, '')
        # Agitha Checklist
        elif "Agitha's Castle" in hint_text:
            agitha_checklist = hint_text.split(':  ')[1]
        # Jovani Checklist
        elif 'souls reward' in hint_text:
            jovani_checklist = hint_text.split('  ')

        # Store the hints now.
        if hint:
            hint_texts.append(hint)

# =============================================================================

# Notebook Creation ===========================================================

# Root window
root = Tk()
root.geometry('500x500')
root.title('Hint Tracker Tool')
root.config(bg = '#2f3136')

# Notebook
notebook = Notebook(root, width=495, height=475)
notebook.pack(padx=5, pady=5, expand=False, anchor='nw')

# =============================================================================

# Agitha's Castle =============================================================

# DRY / easy change in the future
current_category = "Agitha's Castle"

# Create the tab for Agitha's Castle
agitha_frame = create_notebook_tab()

# Let's get the curly braces off.
agitha_checklist = remove_braces(agitha_checklist)
# Then get specifically the list of things she has for us.
agitha_checklist = agitha_checklist.split(', ')

# Create the checklist
agitha_checks = []
for agitha_item in agitha_checklist:
    agitha_checks.append(create_checkbox(agitha_item, agitha_frame))

# =============================================================================

# Jovani's Redemption =========================================================

# We are now on Jovani.
current_category = "Jovani's Poes"

# Create the tab for Jovani
jovani_frame = create_notebook_tab()

# Store the rewards for use in "woops there was nothing"
jovani_rewards = []
jovani_reward_checklist = []  # Used for the text if there is
# And create the checklist.
jovani_checks = []
for jovani_item in jovani_checklist:
    # Grab the turn in threshold and reward
    threshold, reward = jovani_item.split(': ')

    # Hacky way to fix the split:
    reward = reward.replace('} (', '}-(')

    # And further split the reward into the reward, and
    # whether or not it's required.
    reward, required = reward.split('-')

    # Remove the braces off of them.
    reward = remove_braces(reward)
    required = remove_braces(required)

    # Grab the number off the threshold ('souls reward' is redundant)
    threshold = threshold[0:2]

    # Rejoin the reward and the threshold
    reward = ': '.join([threshold, reward])

    # Store the reward for later use.
    jovani_rewards.append(reward)

    # Now. If it is not required, we're not gonna make a checklist.
    if not ('not' in required):
        # Create the checklist
        jovani_checks.append(create_checkbox(reward, jovani_frame))
        jovani_reward_checklist.append(reward)

# Should Jovani have nothing, inform the player.
if not jovani_checks:
    # Create the text for the label
    blank_text = 'Jovani remains greedy, and does not pay you well.'

    blank_text = create_text_checklist(blank_text, jovani_rewards)

    # And then create the label.
    completion_label(jovani_frame, blank_text)

# =============================================================================

root.mainloop()
