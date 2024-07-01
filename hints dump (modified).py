
from json import load
from re import findall, sub
from tkinter import Tk, Toplevel, messagebox
from tkinter import StringVar
from tkinter import Button
from tkinter.ttk import Notebook, OptionMenu

from hints.Globals import return_logs_list, return_spoiler_folder
from hints.gui.Globals import return_default_bg
from hints.gui.MainPage import create_main_reset_button, main_page_button
from hints.gui.ResetTracker import reset_tracker
from hints.gui.Utils import create_notebook_tab
from hints.gui.shopping.Agitha import AgithaTab
from hints.gui.shopping.Jovani import JovaniTab

# Global Variables ============================================================

# The default notebook color
default_notebook_bg = return_default_bg()

# This will be updated and set later on,
# and used in many places
seed_name = 'Please pick a seed.'

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
    create_main_reset_button(notebook, main_page_frame)
    # -------------------------------------------------------------------

    # And run the window plz.
    root.mainloop()
