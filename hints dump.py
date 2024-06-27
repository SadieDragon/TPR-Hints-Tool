
from pathlib import Path
from os import listdir, getcwd
from json import load

from os import abort

from tkinter import Tk, Checkbutton, Frame, IntVar, Label
from tkinter.ttk import Notebook

from re import findall

# Globals =====================================================================

default_notebook_bg = '#f9f9f9'

# Hacky Collection Tally Pool
agitha_collected = 0
jovani_collected = 0
collected_items = []

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
    global agitha_collected
    global jovani_collected
    global collected_items

    # The test for if everything is collected for this person
    all_collected = False

    # Find the one that's set
    for index, checkbox_group in [*enumerate(checkboxes)]:
        # Grab the state of the checkbox
        check_state = checkbox_group[1].get()

        # Grab the item this goes with
        item_being_checked = base_checklist[index]

        # If it is 1, then that is the one we need to update
        # if it is not already marked as collected
        if ((check_state == 1) and
            (not (item_being_checked in collected_items))):

            # Store the item
            collected_items.append(item_being_checked)

            # Disable the checkbox.
            checkbox_group[0].config(state = 'disabled')

            # Update the collected counters
            match person:
                case 'Agitha':
                    agitha_collected += 1
                    all_collected = (agitha_collected == len(checkboxes))
                case 'Jovani':
                    jovani_collected += 1
                    all_collected = (jovani_collected == len(checkboxes))

            # No longer need to continue the loop
            break

    # Update the box if all is collected
    if all_collected:
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
                     activebackground = default_notebook_bg)
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


# DRY: Returns the findall result as a list instead of tuple
def findall_to_list(regex: str, to_parse: str) -> list:
    return [*findall(regex, to_parse)[0]]

# =============================================================================

# Get Hints ===================================================================

# Grab the spoiler log path and location
spoiler_log_folder = Path(getcwd()) / 'SpoilerLog'

spoiler_log = listdir(spoiler_log_folder)[0]

spoiler_log_path = spoiler_log_folder / spoiler_log

# Grab the data
with open(spoiler_log_path, 'r') as f:
    spoiler_log_data = load(f)

# Grab the hints specifically
hints = spoiler_log_data['hints']

# Nab the hint texts
hint_texts = []
agitha_checklist = ''
jovani_rewards = {}
for sign, hints_data in [*hints.items()]:
    # Cycle through the hints
    for hint_data in hints_data:
        # Grab the hint text itself.
        hint_text = hint_data['text']

        # Special handling for Agitha
        if sign == 'Agithas_Castle_Sign':
            # TODO: agitha is currently broken again
            agitha_checklist = hint_text.split(':  ')[1]
        # Special handling for Jovani
        elif sign == 'Jovani_House_Sign':
            # Split the text into the two lines (Thx jaq for this regex)
            rewards = findall_to_list('^(.*\)) +(\d+ .*)$', hint_text)

            for line in rewards:
                # Split the turn in threshold off of the reward
                # (with attached quality)
                threshold, item_quality = line.split(': ')

                # Remove the {} and (), and split into an array.
                item_quality = findall_to_list('\{(.*?)\} \((.*?)\)',
                                               item_quality)

                # Then store the rewards for later handling
                jovani_rewards[threshold] = item_quality
        # Normal hints
        elif 'They say that ' in hint_text:
            hint_texts.append(hint_text.replace('They say that ', ''))

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

agitha_checks = []
# Should Jovani have nothing, inform the player.
if not agitha_checklist:
    # Create the text for the label
    blank_text = 'Agitha gives you sadness and nothingness.'

    # And then create the label.
    completion_label(agitha_frame, blank_text)
else:
    # Let's get the curly braces off.
    agitha_checklist = remove_braces(agitha_checklist)
    # Then get specifically the list of things she has for us.
    agitha_checklist = agitha_checklist.split(', ')

    # Create the checklist
    for agitha_item in agitha_checklist:
        agitha_checks.append(create_checkbox(agitha_item, agitha_frame))

# =============================================================================

# Jovani's Redemption =========================================================

# We are now on Jovani.
current_category = "Jovani's Poes"

# Create the tab for Jovani
jovani_frame = create_notebook_tab()

# Go through and parse the rewards that jovani gives
bad_jovani_rewards = []
jovani_reward_checklist = []
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
        jovani_reward_checklist.append(threshold_reward)

# If there are at least 1, then make the checklist.
jovani_checks = []
if len(jovani_reward_checklist) != 0:
    for reward in jovani_reward_checklist:
        jovani_checks.append(create_checkbox(reward, jovani_frame))
# Otherwise, inform the player.
else:
    # Create the text for the label
    blank_text = 'Jovani remains greedy, and does not pay you well.'

    blank_text = create_text_checklist(blank_text, bad_jovani_rewards)

    # And then create the label.
    completion_label(jovani_frame, blank_text)

# =============================================================================

root.mainloop()
