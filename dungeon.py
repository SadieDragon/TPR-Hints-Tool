
from json import load
from os import getcwd, listdir
from pathlib import Path
from tkinter import Tk
from tkinter import Frame, Label
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import Notebook, OptionMenu
from os import abort  # DEBUG

# The default notebook color
default_notebook_bg = '#f9f9f9'

# DRY *already exists*
def create_notebook_tab(master: Notebook, current_category: str) -> Frame:
    '''Turn a frame into a notebook tab.'''
    # The new frame
    new_frame = new_frame = Frame(master, bg=default_notebook_bg)
    new_frame.pack(padx=5, expand=True, fill='both')
    master.add(new_frame, text=current_category)

    # This will be used to pack things into
    return new_frame


# DRY - Copy over to the hints dump file, and update line 233
def create_scroll_window(master: Notebook):
    new_textbox = ScrolledText(master,
                               bg = default_notebook_bg,
                               relief = 'flat',
                               selectbackground = default_notebook_bg,
                               cursor = 'arrow')
    new_textbox.pack(expand=True, fill='y', anchor='e')

    return new_textbox


# Create the dungeons tab and populate it with default
def create_dungeon_tab(master: Notebook, list_of_checks: list):
    # Create the tab
    dungeon_tab = create_notebook_tab(master, 'Dungeons')

    # Create a scrolled text to shove everything into
    dungeon_textbox = create_scroll_window(dungeon_tab)

    # The dungeons, and the assumed color codes associated
    dungeons_and_colors = {
        'Forest Temple': '#aadc8c',
        'Goron Mines': '#f07878',
        'Lakebed Temple': '#4b96d7',
        "Arbiter's Grounds": '#daa877',
        'Snowpeak Ruins': '#a0b4dc',
        'Temple of Time': '#4bbd4b',
        'City in the Sky': '#dcdc82',
        'Palace of Twilight': '#c8a0dc',
        'Hyrule Castle': '#bcbcbc'
    }

    # Go through and create the individual dungeon frames
    for dungeon, color in dungeons_and_colors.items():
        # Create the frame for all the dungeon things.
        sub_dungeon_frame = Frame(dungeon_textbox)
        sub_dungeon_frame.pack(padx = 5,
                               pady = 5,
                               expand = True,
                               fill = 'both',
                               anchor = 'n')
        dungeon_textbox.window_create('end', window=sub_dungeon_frame)

        if dungeon != 'Hyrule Castle':
            dungeon_textbox.insert('end', '\n')

        # Create the label on the left side
        dungeon_label = Label(sub_dungeon_frame,
                              background = color,
                              text = dungeon,
                              width = 15,
                              height = 10)
        dungeon_label.grid(row=0, column=0)

        # Drop down frame for bk (because.. GM.)
        bk_frame = Frame(sub_dungeon_frame)
        bk_frame.pack(padx=5, pady=5, expand=True, fill='both', anchor='n')

        # The amount of times we'll do this next step
        big_keys = 1
        if dungeon == 'Goron Mines':
            big_keys = 3

        # -WORK PAUSED HERE BECAUSE I'VE GONE TO FIX UNREADABLE-

    # Make it so the user can't mess with this textbox in any way
    dungeon_textbox['state'] = 'disabled'

# This is mimicking the main file ====================================
root = Tk()
root.geometry('500x500')
# I have found this to be the best minimum.
root.minsize(300, 300)

notebook = Notebook(root)
notebook.pack(padx=5, pady=5, expand=True, fill='both', anchor='nw')

spoiler_log_folder = Path(getcwd()) / 'SpoilerLog'
# ==================================================================

spoiler_log = spoiler_log_folder / listdir(spoiler_log_folder)[0]
with open(spoiler_log, 'r') as f:
    spoiler_log_data = load(f)

check_names = [*spoiler_log_data['itemPlacements'].keys()]

main_page_frame = create_notebook_tab(notebook, "Main Page")

create_dungeon_tab(notebook, check_names)

root.mainloop()