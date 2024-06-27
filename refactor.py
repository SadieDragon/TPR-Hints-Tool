
# THIS FILE IS NOT MEANT TO RUN. THIS IS MORESO A NOTES
# FILE FOR ME TO REFACTOR WHILE BOPPIN AROUND THE BASE
# CODE, WITHOUT BREAKING THE BASE CODE.

# I REPEAT. DO NOT TRY TO RUN THIS CODE. THX.

from re import findall
from tkinter import IntVar, StringVar
from tkinter import Checkbutton, Frame, Label
from tkinter.ttk import Notebook

default_notebook_bg = '#f9f9f9'

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

# Pass to init
# Both shopping lists will be part of the root notebook
# Both will have a unique name (agitha, jovani)

# Both will create a dict populated {reward: IntVar} (for the checklist)
# Both will have their own unique frame within the notebook,
# with a unique label with a unique StringVar to be updated

# Both will populate their notebook tab, and update
# the label to have the stringvar

# Both will use create_checkbox, custom made for them,
# the parameters being label and command
# (command being pass checks, frame, person, text)
# checks is now a self.var, frame is too, text is the stringvar
# so now all we need really is the name, which is also self!
# heyyyyy, look at that.

# And both use item_collection, which was also unique to them, which takes self.checks, self.name, and self.textvar

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
                        f' {self.name}:n')
            self.label_var.set(new_text)


# Unique to agitha: more than 2 checks (lol)
# Basically, she either gives you a list of her goodies,
# or she says nothing, and you are sad.
# her text i want to later be based on how many checks she has for you.
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
    def parse_sign(sign_text: str):
        rewards_list = []
        if ':' in sign_text:
            # Grab the rewards off of the intro
            rewards = sign_text.split(': ')[1]

            # Remove the braces and split into a list
            rewards_list = rewards[1:-1].split(', ')

        return rewards_list

# Jovani? He's a special dude. He only provides 2 rewards,
# both of which are important to show.
# Oh also he's the only one to use findall
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

    def findall_to_list(regex: str, to_parse: str) -> list:
        '''Returns the findall result as a list instead of tuple.'''
        return [*findall(regex, to_parse)[0]]