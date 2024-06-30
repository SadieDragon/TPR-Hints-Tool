
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
    new_textbox.pack()

    return new_textbox


# Create the dungeons tab and populate it with default
def create_dungeon_tab(master: Notebook):
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
    for index, (dungeon, color) in enumerate(dungeons_and_colors.items()):
        dungeon_frame = Frame(dungeon_textbox,
                              width = 25,
                              height = 25,
                              bg = color)
        dungeon_frame.grid(row=index, column=0)


root = Tk()
root.geometry('500x500')

notebook = Notebook(root)
notebook.pack(padx=5, pady=5, expand=True, fill='both', anchor='nw')

main_page_frame = create_notebook_tab(notebook, "Main Page")

create_dungeon_tab(notebook)

root.mainloop()