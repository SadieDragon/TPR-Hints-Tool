from hints.gui.utils import create_notebook_tab, create_scrollable
from tkinter import Frame, END
from tkinter.ttk import Notebook


class NotepadTab:
    text_field = None

    def __init__(self, gui_parent: Notebook | Frame):
        '''Create the default notebook tab.'''
        # If we are not given a frame, make a frame
        default_page = gui_parent
        if not isinstance(gui_parent, Frame):
            default_page = create_notebook_tab(gui_parent, 'Notes')

        # Create a scrolled text notepad
        self.text_field = create_scrollable(default_page)

    def reset(self) -> None:
        self.text_field.delete(1.0, END)

    # Example for setting text - no clue if it works :P
    def set_text(self, text) -> None:
        self.reset()
        self.text_field.insert(END, text)

    def has_unsaved_data(self) -> bool:
        return bool(self.text_field.get(1.0, END).strip())
